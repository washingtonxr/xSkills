---
title: Linux Embedded Development - Drivers, Applications and Core Subsystems
domain: systems
tags:
  - linux
  - embedded
  - kernel
  - device-driver
  - device-tree
  - ipc
  - networking
  - virtualization
  - real-time
  - build-systems
aliases:
  - Embedded Linux
  - Linux device drivers
  - Linux IPC
  - Linux networking stack
  - KVM and containers
  - Yocto
  - Buildroot
last-updated: 2026-10-22
---

# Linux Embedded Development — Drivers, Applications and Core Subsystems

This note is the systems layer under everything else in the vault. Protocol stacks, dataplanes, AI runtimes and orchestration agents all run *on* the things described here. When an interviewer asks "how would you actually build and ship this on a board", this is the note that answers.

The organising idea: **embedded Linux work is three nested contracts.**

| Layer | Contract you must honour | Failure looks like |
| --- | --- | --- |
| Boot / BSP / build | Reproducible image from source, matching hardware description | Board won't boot, image not reproducible, BSP drift |
| Kernel / driver | Correct hardware abstraction, no crashes, no ABI breaks | Oops, deadlock, use-after-free, race, broken DT binding |
| User space | Right IPC/IO model for the latency and isolation budget | Tail latency, priority inversion, fd leaks, OOM |

## 1. The embedded Linux system architecture

### 1.1 Boot chain — know it end to end
A typical ARM/ARM64/RISC-V boot:

```
ROM (SoC mask ROM / BootROM)
  └─> SPL / MLO / FSBL        (SRAM-limited, sets up DDR, clocks, pinmux)
       └─> U-Boot proper      (loads kernel + DTB + initramfs/ramdisk)
            └─> Linux kernel  (head.S → start_kernel() → rest_init())
                 └─> PID 1    (systemd / BusyBox init / OpenRC)
                      └─> rootfs mount → services → application
```

Key facts to be able to state:
- **U-Boot** passes a **device tree blob (DTB)** address and a kernel command line; on ARM64 with **UEFI/EDK2** or **arm64 boot protocol**, ACPI may replace DT on server-class hardware.
- **`bootargs` / `chosen` node** carries `console=`, `root=`, `rootfstype=`, `init=`, `mem=`, `isolcpus=`, `nohz_full=`, `rcu_nocbs=`, `cma=`, `intel_iommu=off`.
- **TF-A (Trusted Firmware-A)** and **OP-TEE** sit below Linux on ARM TrustZone platforms: BL31 (secure monitor) and a secure-world OS. Linux runs in the normal world; SMC calls cross the boundary.
- **Early boot debugging**: serial console (most useful), `earlycon`/`earlyprintk`, JTAG, U-Boot `md`/`mw` for register pokes, LED/gpio heartbeats.

### 1.2 Board Support Package (BSP) contents
- **Kernel** source + defconfig + patches, often with a vendor BSP layer.
- **Device tree** sources (`.dts`/`.dtsi`) for the board and the SoC.
- **Bootloader** (U-Boot) with board defconfig and SPL.
- **Toolchain / SDK** (cross gcc, glibc or musl, sysroot).
- **Root filesystem** built by [[13-1 Programming Languages Toolchain and Performance Engineering]] toolchains (Buildroot/Yocto/OpenWrt).
- **Firmware blobs** (Wi-Fi/BT, GPU, NPU, modem) — a recurring licensing and OTA pain point.

### 1.3 Root filesystem and storage
| Choice | Consider when |
| --- | --- |
| **initramfs / initrd** | Early userspace, small, RAM-resident; used for mounting the real root or for recovery |
| **SquashFS / EROFS** | Read-only compressed rootfs (routers, CPE — see [[04-3 WLAN Ecosystem - WFA, EasyMesh and prpl]]); paired with an overlay for writes |
| **ext4** | Read-write, journaling, mainstream for eMMC/SD |
| **UBIFS** | Raw NAND with UBI volume management; handles bad blocks and wear levelling |
| **JFFS2** | Legacy raw NOR/NAND, largely superseded |
| **overlayfs** | Read-only base + writable upper; the basis of container image layers and of A/B-style runtime overlays |

- **Flash wear**: use `f2fs`/UBIFS on raw flash, minimise writes, log to RAM or rotate sparingly, keep the filesystem read-only where possible.
- **MTD vs block layer**: raw flash is MTD (`/dev/mtd*`, `flash_erase`, `nandwrite`), not a block device. Confusing the two is a classic interview trip-up.

### 1.4 Init system and lifecycle
- **systemd** on larger systems: units, targets, dependencies, socket activation, journald, `systemd-analyze`, watchdog integration (`RuntimeWatchdogSec`).
- **BusyBox init** on small targets: `/etc/inittab`, rc scripts, ~100 KB footprint.
- **Supervision**: PID 1 reaps orphans; a supervised service is restarted, a daemonised one is not. Prefer a supervisor (systemd/runit/s6) over hand-rolled double-fork daemons.
- **OTA update**: A/B partitions with a bootloader slot selector is the robust pattern; **RAUC**, **SWUpdate**, **Mender**, **OSTree** implement it. Rollback must be automatic on failed boot (`bootcount`).
- **Watchdog**: hardware watchdog fed by a userspace daemon; `systemd` `WatchdogSec` + `sd_notify(0, "WATCHDOG=1")` ties the feed to service health, not just to "the process exists".

## 2. Build systems and cross toolchain

### 2.1 Buildroot vs Yocto vs OpenWrt
| | Buildroot | Yocto / OpenEmbedded | OpenWrt |
| --- | --- | --- | --- |
| Model | Makefile + Kconfig, one build | BitBake recipes + layers | Buildroot-derived, package feeds |
| Output | rootfs image + toolchain | full distro, package feeds, SDK | router firmware, `opkg` packages |
| Learning curve | Low | High | Medium |
| Reproducibility | Good | Excellent (with locked layers) | Good |
| Best for | Single product, small team, fast iteration | Long-lived product lines, many variants, BSP ecosystem, SBOM/compliance | Networking devices, CPE |

Practical rule: choose **Buildroot** for "one board, one image, ship it"; choose **Yocto** when you need package feeds, multiple hardware variants, a maintained BSP layer model, or long-term maintenance across SoC generations.

### 2.2 Cross-compilation essentials
- **Tuple**: `aarch64-linux-gnu-` / `arm-linux-gnueabihf-` / `riscv64-linux-gnu-`; set `ARCH=` and `CROSS_COMPILE=` for kernel builds, or use a CMake toolchain file.
- **Sysroot discipline**: never let host headers leak in. Use `--sysroot`, `-I`/`-L` pointing at the target sysroot, and build out-of-tree.
- **C library choice**: **glibc** (full featured, larger), **musl** (small, static-friendly, correct-but-different behaviour), **uclibc-ng** (legacy embedded). Differences show up in DNS resolution, thread stack sizes, and `malloc` behaviour.
- **Version pinning**: pin toolchain, kernel, and all package versions for reproducible builds; record them (SBOM is now a compliance requirement in many sectors).

### 2.3 Kernel build workflow
```
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- defconfig   # or vendor defconfig
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- menuconfig
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j$(nproc) Image dtbs modules
make ARCH=arm64 INSTALL_MOD_PATH=/path/to/rootfs modules_install
```
- `make savedefconfig` produces a minimal defconfig — always commit that, never the full `.config`.
- Out-of-tree module build: `make -C /lib/modules/$(uname -r)/build M=$PWD modules`.
- **Signing / lockdown**: distributions with Secure Boot require signed modules; `CONFIG_MODULE_SIG` and kernel lockdown restrict `devmem`, kexec and unsigned modules. This matters when debugging on customer hardware.

## 3. Kernel and driver development

### 3.1 Module basics
- Entry/exit: `module_init()`/`module_exit()`; `MODULE_LICENSE()` (a non-GPL module **taints** the kernel and cannot use `EXPORT_SYMBOL_GPL` symbols); `MODULE_DEVICE_TABLE()` for hotplug/DT matching.
- Loading: `insmod` (raw), `modprobe` (dependency-aware via `modules.dep`), `depmod`, `modinfo`, `lsmod`, `rmmod`, `modprobe -r`.
- Parameters: `module_param(name, type, perm)` exposes `/sys/module/<name>/parameters/`.
- **Vermagic / `CONFIG_MODVERSIONS`**: a module built against a different kernel source/CRC set will refuse to load. This is why out-of-tree drivers need DKMS or a per-kernel rebuild.

### 3.2 Linux device model
- **Bus → device → driver**: `struct bus_type`, `device_register()`, `driver_register()`; match happens via the bus's `match()` (DT `compatible`, ACPI ID, PCI/USB ID table, or `platform` name match).
- **`platform_device` / `platform_driver`** for SoC-integrated, non-discoverable peripherals — the bread and butter of embedded drivers.
- **kobject / kset / ktype** are the reference-counted glue behind sysfs; sysfs is one value per file.
- **uevent + udev/mdev/eudev**: the kernel emits `add`/`remove`/`change` events; userspace creates `/dev` nodes and applies permissions. Rules live in `/etc/udev/rules.d/`.
- **Managed resources (`devm_*`)**: `devm_ioremap_resource`, `devm_request_threaded_irq`, `devm_kzalloc` bind lifetime to the device, so `.remove()` and error paths need no manual teardown. Prefer them — most driver bugs are teardown bugs.

### 3.3 Device tree
- **DTS → DTB** compiled with `dtc`; `dtc -I dtb -O dts` to decompile a running blob from `/sys/firmware/fdt`; `dtc -@` for symbols enabling overlays.
- Key properties: `compatible` (matches `of_device_id`), `reg` (address/length), `interrupts` + `interrupt-parent`, `clocks`, `gpios`, `pinctrl-*`, `status`, `#address-cells`/`#size-cells`, `phandle` and references like ` <&gic 0 8 IRQ_TYPE_LEVEL_HIGH>`.
- **Overlays** allow runtime extension (HATs, add-on boards), applied via the configfs interface `/sys/kernel/config/device-tree/overlays/` or loaded by U-Boot before boot.
- **Bindings are ABI.** A `compatible` string and its binding properties must be documented (`Documentation/devicetree/bindings/`) and reviewed; changing them breaks existing DTBs. The upstream rule: **an existing binding cannot be changed in a way that breaks old device trees.** Treat DT as a hardware description, not a configuration dump — encode hardware topology, not policy.
- Driver-side OF APIs: `of_property_read_u32()`, `of_get_named_gpio()`, `of_irq_get()`, `of_parse_phandle()`, `of_device_get_match_data()`, `of_platform_populate()`.

```c
static const struct of_device_id my_of_match[] = {
    { .compatible = "vendor,my-ip", .data = &my_variant_a },
    { /* sentinel */ }
};
MODULE_DEVICE_TABLE(of, my_of_match);

static int my_probe(struct platform_device *pdev)
{
    struct device *dev = &pdev->dev;
    void __iomem *base;

    base = devm_platform_ioremap_resource(pdev, 0);   /* devm: auto-unmapped */
    if (IS_ERR(base))
        return PTR_ERR(base);

    return devm_request_threaded_irq(dev, platform_get_irq(pdev, 0),
                                     my_hardirq, my_thread,
                                     IRQF_ONESHOT, dev_name(dev), dev);
}

static struct platform_driver my_driver = {
    .probe  = my_probe,
    .driver = { .name = "my-ip", .of_match_table = my_of_match },
};
module_platform_driver(my_driver);
MODULE_LICENSE("GPL");
```

### 3.4 Character device drivers
- `alloc_chrdev_region()` → `cdev_init()` → `cdev_add()`; create the node with `device_create()` (needs a `class`) so udev/mdev gives you `/dev/mydev` with the right major/minor.
- `struct file_operations` is the contract: `open`, `release`, `read`, `write`, `llseek`, `unlocked_ioctl`, `compat_ioctl` (32-bit userspace on 64-bit kernel), `mmap`, `poll`, `fasync`.
- `filp->private_data` + `container_of(inode->i_cdev, ...)` is the standard way to reach per-device state.
- **Never dereference `__user` pointers.** Use `copy_to_user()`/`copy_from_user()` and check the return; larger/long-lived transfers use `mmap` or a DMA buffer instead.
- `ioctl` discipline: use `_IOC(dir, type, nr, size)` encoding, never bare integers; validate `size`/`nr`; 64-bit-safe structs (`__u64`, explicit padding) so 32-bit and 64-bit userspace agree.

```c
static int my_open(struct inode *inode, struct file *filp)
{
    filp->private_data = container_of(inode->i_cdev, struct my_dev, cdev);
    return 0;
}

static const struct file_operations my_fops = {
    .owner          = THIS_MODULE,
    .open           = my_open,
    .read           = my_read,
    .write          = my_write,
    .unlocked_ioctl = my_ioctl,
    .compat_ioctl   = my_ioctl,     /* if the arg layout is 32/64-neutral */
    .poll           = my_poll,
    .mmap           = my_mmap,
    .release        = my_release,
};
```

### 3.5 Concurrency and locking in the kernel
| Primitive | Sleeps? | Use when |
| --- | --- | --- |
| `spinlock_t` | No (busy-wait, disables preemption) | Very short critical sections, interrupt context, shared with IRQ handler |
| `mutex` | Yes | Process-context critical sections that may sleep (most driver state) |
| `rt_mutex` | Yes, priority-inheritance | PREEMPT_RT; what spinlocks become |
| `rwlock` / `seqlock` | No | Read-mostly data with brief write bursts |
| `RCU` | Readers never block | Read-mostly pointer structures, list traversal |
| `atomic_t` / `refcount_t` | No | Counters and reference counts |
| `completion` | Yes | "Wait for one specific event" |
| `local_lock_t` | No (RT: sleeping per-CPU lock) | Per-CPU data protected from preemption/migration |

Rules that interviewers probe:
- **You cannot sleep in atomic context** — no `mutex_lock`, `kmalloc(GFP_KERNEL)`, `copy_from_user`, or `schedule()` while holding a spinlock or in a hard IRQ handler.
- **Interrupt-disabling spinlocks must be used only when the lock is also taken in the IRQ handler**; otherwise use the plain form.
- **Lock ordering** must be documented and consistent; `lockdep` (`CONFIG_PROVE_LOCKING`) finds inversions at runtime and is the single highest-value kernel debug option.
- **On PREEMPT_RT**, most spinlocks become sleeping RT-mutexes; code that assumed a spinlock disables interrupts will break. This is exactly why `raw_spinlock_t` exists.

### 3.6 Memory allocation
- `kmalloc(size, flags)` — physically contiguous, fast, limited size; `vmalloc()` — virtually contiguous only; `kmem_cache_create()` — slab cache for fixed-size hot objects.
- **GFP flags**: `GFP_KERNEL` (may sleep, normal), `GFP_ATOMIC` (never sleeps — interrupt context), `GFP_DMA`/`GFP_DMA32` (addressable by the device), `GFP_ZERO`, `__GFP_NOWARN`.
- **`devm_kzalloc()`** ties lifetime to the device; prefer it so remove paths cannot leak.
- **Kernel stack is small** (commonly 8 KB on 32-bit, 16 KB on arm64): no large stack arrays, no deep recursion, no big `struct` by value.
- **No floating point** in kernel code (FPU state is not saved; `kernel_fpu_begin()`/`kernel_fpu_end()` only where explicitly allowed).
- **User/kernel address spaces are separate**; `virt_to_phys()` is only valid for directly-mapped lowmem, never for `vmalloc` or user addresses.

### 3.7 Interrupts
- `request_irq()` / `devm_request_threaded_irq()`; `IRQF_SHARED` requires a valid `dev_id` and a handler that checks its own device; `IRQF_ONESHOT` for threaded handlers on level-triggered lines; `IRQF_NO_THREAD` to opt out of forced threading.
- **Top half**: acknowledge/mask, minimal work, wake the bottom half. **Bottom halves**:
  - **softirq** — static, cannot sleep, runs on the raising CPU; used by networking and block layers.
  - **tasklet** — dynamic, serialised per tasklet, cannot sleep; being de-emphasised.
  - **workqueue** — runs in a kernel thread, may sleep; the default choice for driver work.
  - **threaded IRQ** — the interrupt handler becomes a schedulable thread; the default under PREEMPT_RT, and the cleanest model for most embedded drivers.
- **irqdomain** maps hardware IRQ numbers to Linux virtual IRQs; the GIC (ARM) or PLIC/AIA (RISC-V) is described in DT and handled by the irqchip driver.
- **MSI/MSI-X** converts an interrupt into a memory write — essential for PCIe devices and for pinning interrupts to specific CPUs.
- Affinity: `/proc/irq/<n>/smp_affinity`, `irqbalance` off on dataplane systems — see [[08-1 DPDK User Plane and 5G UPF]].

### 3.8 Timers and deferred work
- `timer_setup()` + `mod_timer()` — jiffies-resolution, low-res timer API.
- **hrtimers** (`hrtimer_start()`) — nanosecond resolution, `CLOCK_MONOTONIC`; the base for `timerfd`, `nanosleep`, and scheduling deadlines.
- `schedule_work()` / `queue_delayed_work()` / `schedule_work_on()`; allocate a dedicated `alloc_workqueue()` with `WQ_UNBOUND`, `WQ_HIGHPRI`, `WQ_CPU_INTENSIVE` when the default `system_wq` would throttle you.

### 3.9 Blocking I/O and async notification
```c
static DECLARE_WAIT_QUEUE_HEAD(my_wq);

static ssize_t my_read(struct file *f, char __user *buf, size_t n, loff_t *p)
{
    if (wait_event_interruptible(my_wq, data_ready()))
        return -ERESTARTSYS;          /* signal arrived: let VFS retry */
    if (copy_to_user(buf, kbuf, n))
        return -EFAULT;
    return n;
}
/* from the interrupt / completion path: */
wake_up_interruptible(&my_wq);
```
- `poll_wait()` + returning `EPOLLIN`/`EPOLLOUT` makes a driver work with `select`/`poll`/`epoll`.
- `fasync_helper()` + `kill_fasync()` sends **SIGIO** to a registered process — the kernel-side of signal-driven I/O.
- `wake_up()` variants: `wake_up` (all exclusive+nonexclusive), `wake_up_interruptible`, `wake_up_all`; choose deliberately.

### 3.10 MMIO, barriers and ordering
- `ioremap()`/`devm_platform_ioremap_resource()` → `void __iomem *`; access only with `readl()`/`writel()`/`readb()`/`writeb()`.
- **Barriers**: `mb()`/`rmb()`/`wmb()` for device ordering, `smp_mb()` family for CPU ordering, `READ_ONCE()`/`WRITE_ONCE()` to force a single access, `barrier()` for compiler-only ordering. `volatile` is **not** a substitute and is discouraged in kernel code.
- **Relaxed vs non-relaxed accessors** (`readl_relaxed()` vs `readl()`) — know the difference, and default to the safe one.
- On many SoCs, MMIO regions must be marked **non-cacheable / device memory**; getting this wrong produces "works until the cache evicts" bugs.

### 3.11 DMA and cache coherency
- **Coherent (consistent) memory**: `dma_alloc_coherent()` — uncached or hardware-coherently cached, valid for the whole driver lifetime, expensive, limited size.
- **Streaming mappings**: `dma_map_single()` / `dma_unmap_single()`, `dma_map_sg()` — map a normal buffer for the duration of a transfer; **ownership must be transferred explicitly**.
- **Non-coherent platforms** need explicit sync: `dma_sync_single_for_cpu()` before the CPU reads, `dma_sync_single_for_device()` before the device reads. Missing these is the #1 DMA bug on ARM32/SoC platforms.
- **Cache maintenance**: outer/inner cache, `ARCH_DMA_MINALIGN` alignment for DMA buffers, avoid cache-line sharing between CPU-written and device-written fields.
- **DMA mask**: `dma_set_mask_and_coherent(dev, DMA_BIT_MASK(32|40|48))` — the device tells the kernel what it can address; failure causes silent fallback or allocation failure.
- **CMA** provides large contiguous buffers for multimedia/NPU; `swiotlb` provides bounce buffering for devices that cannot reach the buffer.
- **dma-buf** is the cross-subsystem/share-across-devices buffer framework (GPU ↔ VPU ↔ camera ↔ NPU, and into userspace via a file descriptor) — this is the primitive that matters for zero-copy AI pipelines.
- **IOMMU** (ARM SMMU, Intel VT-d, AMD-Vi) gives device address translation and isolation; it is also the mechanism behind **VFIO** device assignment (§7).

### 3.12 Bus subsystems and kernel frameworks
Don't write a raw driver when a framework already exists:
| Framework | Use |
| --- | --- |
| **regmap** | Abstract register access over I²C/SPI/MMIO with caching and locking — write this instead of hand-rolling `i2c_transfer` |
| **IIO** | ADC, DAC, IMU, sensors; `sysfs` + char device + buffered capture |
| **hwmon** | Temperature, voltage, fan |
| **gpio / pinctrl** | GPIO control (`gpiod_*`, descriptor API, not the legacy integer API) and pin muxing |
| **clk / regulator / phy** | Clock, power rail and PHY providers — model dependencies instead of poking registers |
| **netdev** | `struct net_device`, `ndo_start_xmit`, NAPI `poll`, `skb` handling, ethtool |
| **SocketCAN** | CAN bus as a network interface (`can0`, `candump`, `cansend`) |
| **USB gadget / host** | FunctionFS, gadget drivers, `usb_f_*` |
| **PCI / platform / SPI / I²C** | `spi_sync()`, `i2c_transfer()`, `devm_regmap_init_spi()` |

Reusing frameworks is not laziness — it is how you get power management, sysfs ABI, and upstream acceptance for free.

### 3.13 Kernel-to-userspace interfaces — which to choose
| Interface | Rule of thumb |
| --- | --- |
| **sysfs** | One value per file, stable ABI, hardware/state attributes; never for bulk data or control protocols |
| **debugfs** | Debug only, **no ABI guarantees**, may be absent under lockdown |
| **procfs** | Legacy process/system info; new interfaces should not go here except process-related data |
| **configfs** | User-driven kernel object creation (e.g. DT overlays, USB gadgets) |
| **netlink** | Network configuration and events, multicast, extensible attributes — the right choice for networking control planes |
| **ioctl** | Device-specific commands that do not fit the file model; last resort, must be versioned |
| **char device + read/write/mmap** | Streaming data, zero-copy via `mmap` |
| **UIO / VFIO** | Userspace drivers for special hardware — see §3.14 |

The upstream rule to remember: **"don't break userspace" is kernel policy, not a suggestion.** Once an interface ships, it is ABI.

### 3.14 Userspace drivers: UIO vs VFIO
- **UIO** — minimal: exposes MMIO and interrupt to userspace via `/dev/uioX` and `read()` blocking on the IRQ. No DMA/IOMMU support. Good for simple, low-throughput hardware; increasingly discouraged.
- **VFIO** — the modern path: uses the IOMMU to build a secure, isolated IOVA mapping for a userspace driver or a VM-assigned device. Supports DMA, MSI, and device reset. This is what DPDK uses for real NIC access — see [[08-1 DPDK User Plane and 5G UPF]].

### 3.15 Kernel debugging toolbox
| Tool | Finds |
| --- | --- |
| `printk` / `pr_debug` / `dev_dbg` + **dynamic debug** | Runtime tracing without recompiling (`echo 'file foo.c +p' > /sys/kernel/debug/dynamic_debug/control`) |
| **ftrace** (`function`, `function_graph`, `trace_printk`, `trace-cmd`) | Call paths, latency, irqsoff/preemptoff/ wakeup latency tracers |
| **perf** (`perf top/record/report`, `perf probe`, `perf kmem`) | Hot paths, cache misses, allocator behaviour |
| **lockdep** | Lock inversions and deadlock potential |
| **KASAN** | Use-after-free, out-of-bounds (memory-hungry, test builds) |
| **UBSAN** | Undefined behaviour |
| **KCSAN** | Data races |
| **kmemleak** | Kernel memory leaks |
| **devmem2 / `/dev/mem`** | Register reads from userspace (blocked under lockdown) |
| **KGDB / kdb / JTAG** | Live kernel debugging; JTAG is the only option for early-boot hangs |
| **kdump / crash / vmcore** | Post-mortem analysis of a panic |
| `WARN_ON`, `BUG_ON`, `dev_WARN` | Deliberate assertions; `BUG_ON` panics, so use it sparingly in production paths |

Reading an **Oops**: get the PC, the symbolised call trace, and the "Code:" line; `scripts/decode_stacktrace.sh` or `addr2line`/`objdump -S` against the matching `vmlinux` (keep it around — this is why you build with debug info on debug images).

### 3.16 Driver development method (how to actually work)
1. **Read the datasheet and the existing DT binding** before writing code. Confirm register map, interrupt type (level vs edge), DMA capabilities and reset behaviour.
2. **Start from the closest upstream driver**, not from a blank file.
3. **Prove the hardware independently first** — `i2c-tools` (`i2cdetect`, `i2cget`), `spidev_test`, `devmem2`, a logic analyser. Separate "my driver is wrong" from "the board is wrong".
4. **Build a minimal skeleton**: probe → `devm` resources → sysfs attribute → read a known register (ID/version). Boot it.
5. **Add one mechanism at a time**: IRQ → workqueue → DMA → userspace interface.
6. **Instrument for the failure modes**: dynamic debug, `lockdep` on, `DEBUG_ATOMIC_SLEEP` on during development.
7. **Test remove/rebind**: `echo -n <dev> > /sys/bus/platform/drivers/.../unbind` repeatedly — leaks and races surface here.
8. **Upstream it.** Out-of-tree drivers rot; the review process is also free design review.

## 4. Linux application development for embedded targets

### 4.1 Process model
- `fork()` (copy-on-write), `vfork()` (no COW, suspends parent), `clone()` (the real primitive; `fork`/pthreads are wrappers), `posix_spawn()` (fast fork+exec for constrained systems).
- `execve()` replaces the image; file descriptors survive unless `O_CLOEXEC` (always set it — the classic fd-leak-into-child bug).
- **Zombies and orphan reaping**: `waitpid()`, `SIGCHLD`, double-fork daemonisation, or let a supervisor own it.
- **PID 1 semantics**: no default signal handlers, reaps orphans; a container's PID 1 that ignores `SIGTERM` is a well-known shutdown bug.
- **Threads**: `pthread_create`, `pthread_attr_setstacksize` (default 8 MB is huge on embedded — set it explicitly), `pthread_setname_np`, `pthread_setaffinity_np`.
- **Thread vs process** decision: process for isolation and independent restart, thread for shared memory and low-latency handoff. On embedded Linux with a small core count, a thread pool plus an event loop usually beats a process-per-connection design.

### 4.2 Signals
- `sigaction()` over `signal()`; never do real work in a handler — only set a `volatile sig_atomic_t` flag, write to a pipe, or `write()` to a self-pipe.
- **Async-signal-safety**: only a small function list is safe. `malloc`, `printf`, and most library calls are **not**.
- **Self-pipe trick** and **`signalfd()`** convert a signal into a file-descriptor event so it can be handled inside the `epoll` loop — this is the pattern production daemons use.
- `sigprocmask()`/`pthread_sigmask()` to block signals in threads; real-time signals (`SIGRTMIN+n`) are queued and carry a value, unlike standard signals.
- `SIGKILL` and `SIGSTOP` cannot be caught — relevant to graceful-shutdown design.

### 4.3 File and device I/O
- Blocking vs `O_NONBLOCK` vs `O_ASYNC`; `poll`/`select`/`epoll` for readiness.
- **Zero-copy and reduction**: `sendfile()` (file→socket), `splice()`/`tee()`/`vmsplice()` (pipe-based), `mmap()` for shared buffers, `io_uring` for batched async.
- **`O_DIRECT`** bypasses the page cache but imposes alignment and does *not* imply durability.
- **Durability**: `fsync()`/`fdatasync()`/`sync_file_range()`; know the difference (metadata vs data) before promising persistence.
- **`close()` does not mean "written"** — a power-loss path must call `fsync` + rename.
- `posix_fadvise()` / `madvise()` / `readahead()` to hint access patterns; `FALLOC_FL_*` to preallocate.
- **`inotify`/`fanotify`** for filesystem event watching; inotify does not recurse and has queue limits.
- **io_uring** (since 5.1) is now the default high-performance choice for both storage and sockets: submission/completion rings, `IORING_SETUP_SQPOLL`, registered buffers/files, and zero-copy receive. Compare with the kernel-bypass options in [[13-1 Programming Languages Toolchain and Performance Engineering]].

### 4.4 Time
- `clock_gettime()` with `CLOCK_MONOTONIC` for intervals, `CLOCK_MONOTONIC_RAW` for drift-free, `CLOCK_REALTIME` for wall-clock (can jump), `CLOCK_BOOTTIME` to include suspend, `CLOCK_PROCESS_CPUTIME_ID` for CPU accounting.
- `timerfd_create()` turns a timer into an `epoll`-able fd — the standard way to embed timers in an event loop.
- `nanosleep`/`clock_nanosleep(TIMER_ABSTIME)` — absolute sleeps avoid drift accumulation in periodic loops.
- **PTP / hardware timestamping**: `SO_TIMESTAMPING`, `ethtool -T`, `phc2sys`, `linuxptp` (`ptp4l`) synchronise to sub-microsecond; `CLOCK_TAI` and `adjtimex()` for the offset. Relevant to TSN and to any RAN timing argument.

### 4.5 Scheduling, priorities and isolation
- Policies: `SCHED_OTHER` (default, EEVDF), `SCHED_BATCH`, `SCHED_IDLE`, `SCHED_FIFO`, `SCHED_RR`, `SCHED_DEADLINE` (CBS, `(runtime, period, deadline)` triple — the only Linux policy with an admission test).
- **RT throttling**: by default RT tasks are limited to 95% of CPU (`/proc/sys/kernel/sched_rt_runtime_us`) so a runaway RT loop cannot wedge the box.
- **Priority inversion**: a low-priority task holding a lock blocks a high-priority one. Fixes: **priority inheritance** (`PTHREAD_PRIO_INHERIT` mutexes, and RT-mutexes in the kernel under PREEMPT_RT), priority ceilings, or lock-free designs.
- **Isolation**: `isolcpus=`, `nohz_full=`, `rcu_nocbs=`, `irqaffinity=`, `sched_setaffinity()`, cpusets, `taskset`. Required for deterministic dataplane and radio work.
- **EEVDF** replaced CFS as the default scheduler in 6.6; **sched_ext** (§9) lets you replace the policy itself with a BPF program.

### 4.6 Memory in userspace
- `malloc` uses `brk` for small and `mmap` for large allocations; **virtual memory overcommit** means allocation succeeds and the failure arrives later as an OOM kill — control it with `vm.overcommit_memory`, cgroup limits, and by preallocating pools in latency-critical daemons.
- **`mlockall(MCL_CURRENT|MCL_FUTURE)`** locks pages to avoid fault latency in RT paths; needs `RLIMIT_MEMLOCK`.
- **Huge pages**: `hugetlbfs` and THP reduce TLB pressure; mandatory for DPDK ([[08-1 DPDK User Plane and 5G UPF]]).
- **RSS vs VSZ**: VSZ is nearly meaningless on embedded; watch RSS/PSS and slab/unreclaimable kernel memory.
- Leak/limit tooling: `valgrind` (slow, dev only), ASan/LSan, `mtrace`, `smem`, `/proc/<pid>/smaps`, cgroup `memory.events`.
- **Fragmentation on long-running devices**: prefer pools/arenas preallocated at startup for embedded daemons that must run for months.

### 4.7 Production hygiene for embedded daemons
- Structured logging with rotation and size caps; log to RAM or a size-limited partition on flash.
- Core dumps: `core_pattern`, `coredumpctl`, or a custom handler that captures to a debug partition.
- Health signalling: `sd_notify()` readiness + watchdog, or a simple `/run/<service>.pid` heartbeat.
- Crash-only design: fail fast, restart under the supervisor, persist only durable state.

## 5. Inter-Process Communication (IPC)

The single most useful way to answer an IPC question is along these axes: **direction**, **number of copies**, **does it cross the kernel**, **latency order**, **persistence**, **fd/credential passing**.

### 5.1 Mechanism comparison
| Mechanism | Direction | Copies | Kernel crossing | Typical use | Notes |
| --- | --- | --- | --- | --- | --- |
| **Pipe / FIFO** | Unidirectional (pipe) / named (FIFO) | 1–2 | Yes (ring buffer in kernel) | Shell pipelines, producer/consumer | `pipe2(O_CLOEXEC\|O_NONBLOCK)`, capacity via `F_SETPIPE_SZ`; FIFO has a filesystem name |
| **Signal** | Async notification | 0 payload | Yes | Lifecycle, interrupts | Cannot carry data safely; use `sigqueue`/`SIGRTMIN` for a small value |
| **SysV message queue** | Bidirectional, typed | 2 | Yes | Legacy | Kernel-persistent (`ipcs`/`ipcrm`), no fds → awkward with `epoll` |
| **POSIX mqueue** | Bidirectional, priority | 2 | Yes | Real-time messaging | `mq_open("/name")`, `mq_timedreceive`, IS fd-based → `epoll`-able, priority-ordered |
| **Shared memory (shm)** | Bidirectional | **0** after setup | Setup only | Large data, zero-copy | `shm_open` + `mmap`, or `memfd_create` + `mmap`; **needs its own synchronisation** |
| **Semaphore** | Synchronisation | 0 | Yes | Mutual exclusion | POSIX (`sem_open`) or SysV; the pairing to shared memory |
| **Unix domain socket** | Bidirectional | 1 (or 0 with SCM_RIGHTS) | Yes | Local services, daemon control | `SOCK_STREAM`/`DGRAM`/`SEQPACKET`; **passes file descriptors** and credentials |
| **eventfd** | Counter notification | 0 | Yes | Wake an `epoll` loop | Perfect for "pollable doorbell" between threads/processes |
| **signalfd / timerfd / pidfd** | fd-ified kernel events | 0 | Yes | Event loops | Turns signals/timers/processes into pollable fds |
| **futex** | Fast userspace sync | 0 in uncontended case | Only on contention | Lock implemented over shared memory | The primitive under `pthread_mutex` |
| **netlink** | Kernel ↔ userspace | 1 | Yes | Network config, uevents | Also usable between processes (`NETLINK_USERSOCK`) |
| **D-Bus** | Bidirectional RPC | 2 + marshalling | Yes (daemon) | Desktop/system service bus | Method calls + signals; introspection; overhead is real |
| **Binder** | RPC + shared buffer | 1 (mapped) | Yes (driver) | Android | `binderfs`; one-copy via mmap'd transaction buffer |
| **MQTT / HTTP / gRPC** | Network protocol | — | Yes (network) | Distributed, not local IPC | Don't reach for these for on-box communication |

### 5.2 Choosing an IPC mechanism — the decision logic
1. **Just a wakeup?** → `eventfd` (cheapest pollable notification).
2. **Small messages, want priority and fd-compatibility?** → POSIX message queue or Unix domain socket.
3. **Large or high-rate data?** → shared memory + a futex/ring, or Unix socket passing an fd to the shared buffer.
4. **Need to hand over a resource (fd, mmap'd buffer, dmabuf)?** → Unix domain socket with `SCM_RIGHTS`. This is the only clean way.
5. **Need peer identity?** → Unix socket `SO_PEERCRED` (`struct ucred`: pid/uid/gid) — the standard local authentication primitive.
6. **Kernel needs to talk to you (config or events)?** → netlink or generic netlink.
7. **Cross-machine?** → then it is a network protocol problem; see §6 and [[10-2 Agent Systems and Edge Orchestration]].

### 5.3 Zero-copy pattern: shared memory + futex doorbell
The canonical high-performance local pipeline:
```
producer                         consumer
  memfd_create / shm_open  ──►   mmap the same fd
  write into ring slot
  futex_wake / eventfd_write ──► epoll_wait returns
                                 read ring slot
                                 futex_wait for next
```
- **Why**: no syscalls on the steady-state path, no copies, and the kernel only gets involved on contention or wakeup.
- **The hard parts**: cache-line alignment of head/tail indices (false sharing), memory ordering (`atomic_load_acquire`/`atomic_store_release`, not bare `volatile`), and what happens when one side dies holding the lock (use robust futexes or an external supervisor).
- This is the same shape as the ring buffers in DPDK and as the L1↔L2 interface in a modem — see [[12-1 RISC-V for Communication Infrastructure]].

### 5.4 Passing a file descriptor
```c
struct msghdr msg = { 0 };
char control[CMSG_SPACE(sizeof(int))];
union { struct cmsghdr align; char buf[256]; } u;   /* keep alignment safe */

msg.msg_control    = control;
msg.msg_controllen = sizeof(control);
struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msg);
cmsg->cmsg_level = SOL_SOCKET;
cmsg->cmsg_type  = SCM_RIGHTS;
cmsg->cmsg_len   = CMSG_LEN(sizeof(int));
memcpy(CMSG_DATA(cmsg), &fd_to_send, sizeof(int));
sendmsg(sock, &msg, 0);
```
The receiving process gets a *new* fd number pointing at the same file — this is how a privileged daemon hands a NIC, a dmabuf, or a memfd to an unprivileged worker without re-opening anything.

### 5.5 Abstract namespace and socket paths
- Filesystem path sockets (`/run/foo.sock`) are permission-controlled by the filesystem — good, because POSIX ACLs apply.
- **Abstract namespace** (`\0my-socket`) has no filesystem entry and disappears on close — convenient, but no permission control beyond credentials. Prefer filesystem paths for anything security-relevant.

## 6. Linux networking for embedded systems

### 6.1 Socket API essentials
- `socket()` → `bind()` → `listen()`/`connect()`; `accept4(SOCK_CLOEXEC)`; `shutdown()` vs `close()`.
- Options that matter in embedded/networked products:
  - `SO_REUSEADDR` (bind in `TIME_WAIT`) vs `SO_REUSEPORT` (multiple listeners, load spread) — they are different things.
  - `TCP_NODELAY` (disable Nagle) and `TCP_CORK` (coalesce) — pick per message pattern; Nagle + delayed-ACK interaction is a classic latency bug.
  - `SO_RCVBUF`/`SO_SNDBUF` (kernel doubles them; autotuning usually beats manual setting).
  - `SO_KEEPALIVE`, `TCP_USER_TIMEOUT`, `TCP_KEEPIDLE/INTVL/CNT` — dead-peer detection on links that fail silently (very relevant for NTN and lossy backhaul — see [[01-4 Cellular IoT RedCap eRedCap and NTN]]).
  - `SO_BUSY_POLL`, `SO_INCOMING_CPU` — latency vs CPU trade-off.
  - `SO_TIMESTAMPING` for hardware/software timestamps (PTP).
- **Non-blocking discipline**: every `read`/`write` must handle `EAGAIN`/`EWOULDBLOCK` and `EINTR`; partial writes on non-blocking sockets are normal.

### 6.2 Event loops: epoll in practice
```c
int ep = epoll_create1(EPOLL_CLOEXEC);
struct epoll_event ev = { .events = EPOLLIN | EPOLLET, .data.fd = fd };
epoll_ctl(ep, EPOLL_CTL_ADD, fd, &ev);

for (;;) {
    int n = epoll_wait(ep, events, MAX_EVENTS, timeout_ms);
    for (int i = 0; i < n; i++) {
        if (events[i].events & (EPOLLHUP | EPOLLERR)) { /* handle close */ }
        /* Edge-triggered: drain until read() returns EAGAIN */
        while ((r = read(fd, buf, sizeof buf)) > 0) { /* process */ }
        if (r < 0 && errno == EAGAIN) break;
    }
}
```
- **Level-triggered**: simpler, safe, slightly more syscalls.
- **Edge-triggered**: must drain fully; a missed drain permanently stalls the fd. Use it only when you control the whole loop.
- **Thundering herd**: many threads in `epoll_wait` on the same fd all wake. Fix with `EPOLLONESHOT`, `SO_REUSEPORT` (one socket per thread), or a single acceptor distributing work.
- **Timer integration**: `timerfd` and `eventfd` in the same epoll set — the standard single-threaded reactor.

### 6.3 The kernel receive path (know this diagram)
```
NIC DMA → RX ring (descriptor + skb buffer)
   └─> hard IRQ: schedule NAPI
        └─> NAPI poll() (softirq NET_RX_SOFTIRQ): build sk_buffs, GRO aggregation
             └─> ip_rcv() → netfilter PREROUTING → routing decision
                  └─> tcp_v4_rcv() → TCP state machine → sock receive queue
                       └─> wake the process sleeping in epoll_wait/read
```
- **`sk_buff`** is the central data structure: head/data/tail/end pointers enable cheap header push/pull, and it is the reason zero-copy reshuffles are possible.
- **Offloads**: TSO/GSO (segmentation), GRO/LRO (aggregation), checksum offload, scatter-gather — they trade CPU for wire behaviour and confuse packet captures (`tcpdump` sees pre-TSO super-packets).
- **qdisc / tc**: `tc qdisc`, `fq_codel` (default for reducing bufferbloat), `tc-taprio` and `tc-etf` for **TSN** scheduled traffic; `tc filter` with `cls_bpf` for programmable classification.
- **Netfilter**: hooks PREROUTING → INPUT/FORWARD → OUTPUT → POSTROUTING; **`nftables` is the iptables successor** (in-kernel since 3.13) with `nft` as the user tool; `conntrack` underpins NAT and stateful firewalling.

### 6.4 Kernel ↔ userspace networking control plane
- **netlink** is the right interface: `NETLINK_ROUTE` (rtnetlink: links, addresses, routes), `NETLINK_KOBJECT_UEVENT`, `NETLINK_NETFILTER`, and **generic netlink** for custom families. `ip`, `ss`, `tc`, and `ethtool` all speak it.
- **nl80211 / cfg80211 / mac80211** is the Wi-Fi control path: `iw`, `hostapd`, `wpa_supplicant` drive the stack through nl80211. This is the Linux counterpart of everything in [[04-1 WLAN - Wi-Fi Generations Evolution]] and [[04-3 WLAN Ecosystem - WFA, EasyMesh and prpl]].
- **AF_PACKET / `PF_PACKET`** raw sockets for sniffing and raw L2 injection (`tcpdump`, custom protocols); classic BPF filters attach to these.
- **AF_XDP** exposes the NIC ring to userspace through an `XSK` UMEM — bypass without giving up the kernel stack; see the bypass comparison in [[13-1 Programming Languages Toolchain and Performance Engineering]].
- **eBPF attach points**: XDP (driver-level, pre-`skb`), tc ingress/egress, cgroup/skb, sockops, `sk_msg`. Constrained by the **verifier** (bounded loops, no arbitrary memory access) — which is precisely why it is safe to load into a running kernel.
- **io_uring** zero-copy Rx/Tx is now a serious alternative to a full DPDK deployment for moderate rates.

### 6.5 Virtual network plumbing
| Construct | Purpose |
| --- | --- |
| **network namespace** | Independent interfaces, routes, iptables, `/proc/net` — the basis of containers and of network-function isolation |
| **veth** | Virtual ethernet pair connecting two namespaces |
| **bridge** | L2 forwarding (also used for VMs and containers) |
| **macvlan / ipvlan** | Give a namespace a MAC/IP on a parent interface without a bridge |
| **tun / tap** | Userspace L3 (tun) or L2 (tap) endpoint — VPNs, user-space dataplanes, mobile tunnelling |
| **VLAN / VRF** | Segmentation and multiple routing tables |
| **bonding / team** | Link aggregation and failover across backhaul interfaces |
| **VRF + policy routing** | Multi-homed gateways (e.g. cellular + fibre) with clean separation |

This is the toolkit behind a containerised UPF or a virtualised RAN element — see [[08-1 DPDK User Plane and 5G UPF]] and [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]].

### 6.6 Networking debugging checklist
`ip link/addr/route` → `ss -tulpn` (replaces `netstat`) → `ethtool -S` (drop counters, offloads) → `tcpdump`/`tshark` → `nstat`/`/proc/net/snmp` (protocol counters) → `dropwatch` (where skbs are freed) → `perf`/`bpftrace` for latency → `traceroute`/`mtr` for path. Always check **interface counters and qdisc drops first**; they localise the problem faster than any capture.

## 7. Virtualization and isolation

### 7.1 Types
| | Type-1 (bare metal) | Type-2 (hosted) |
| --- | --- | --- |
| Runs on | Hardware directly | A host OS |
| Examples | Xen, Jailhouse, Bao, ACRN, VMware ESXi | KVM (as a kernel module), VirtualBox |
| Typical use | Mixed-criticality consolidation, safety partitions | Cloud, CI, general server consolidation |

**KVM** is the interesting hybrid: it is a kernel module turning Linux into a hypervisor (so: hosted in deployment, type-1-like in performance and architecture), with **QEMU** in userspace providing device emulation.

### 7.2 Containers vs virtual machines
| Axis | Containers | VMs |
| --- | --- | --- |
| Isolation boundary | Namespaces + cgroups + capabilities + seccomp (shared kernel) | Hardware-assisted (separate kernel) |
| Startup | Milliseconds | Hundreds of ms to seconds |
| Overhead | ~0 | Memory + exit costs; near-zero CPU with HW virt |
| Kernel | One shared kernel — one kernel CVE affects all | Independent guest kernels |
| Best for | Microservices, stateless network functions, CI | Multi-OS, strong isolation, legacy/untrusted guests |

Container primitives to know precisely:
- **Namespaces**: `mnt`, `pid`, `net`, `ipc`, `uts`, `user`, `cgroup`, `time`. `unshare`/`nsenter` for debugging; `/proc/<pid>/ns/*` are the handles.
- **cgroups v2**: unified hierarchy; `cpu`, `memory`, `io`, `pids`, `cpuset`, `hugetlb`; delegated via systemd slices. This is the same mechanism you use to pin and budget dataplane cores ([[08-1 DPDK User Plane and 5G UPF]]).
- **capabilities**: drop `CAP_SYS_ADMIN`; keep only what is needed (`CAP_NET_RAW` for raw sockets, `CAP_NET_ADMIN` for netlink config, `CAP_SYS_NICE` for RT priority).
- **seccomp-bpf**, **LSM (SELinux/AppArmor)**, **no_new_privs** — defence in depth after capabilities.
- **rootfs**: `pivot_root`/`chroot`, `overlayfs` layered images, OCI runtime spec, `runc`/`crun`.

### 7.3 Device virtualization and assignment
| Approach | Mechanism | Trade-off |
| --- | --- | --- |
| **Full emulation** | QEMU emulates a well-known device (e1000, rtl8139) | Portable, slow |
| **Para-virtualization (virtio)** | Guest knows it is virtualized; vring descriptor rings, `virtio-net`, `virtio-blk`, `virtio-console` | Fast, needs guest driver |
| **vhost-net / vhost-user** | Move the virtio dataplane into the kernel or into a userspace process (e.g. DPDK) | Removes QEMU from the hot path |
| **VFIO device assignment** | IOMMU + `vfio-pci`; guest or userspace gets the real device | Near-native, device cannot be shared |
| **SR-IOV (PF/VF)** | A physical device exposes multiple Virtual Functions | Near-native *and* shareable; needs NIC + IOMMU support |
| **Mediated device (mdev/vfio-mdev)** | Vendor-mediated partial device (GPU, some NICs) | Shares one device with a controlled interface |

For a vRAN or UPF deployment the usual answer is: **SR-IOV or VFIO passthrough for the dataplane NIC, hugepages, CPU pinning, and NUMA-local memory**; virtio only for control/management interfaces.

### 7.4 Hardware virtualization extensions
- **x86**: Intel VT-x (VMX, EPT, VPIDs, preemption timer) / AMD-V (SVM, NPT, AVIC); IOMMU = VT-d / AMD-Vi.
- **ARM**: EL2 hypervisor mode, two-stage translation, Virtualization Host Extensions (VHE) letting the host kernel run at EL2; **TrustZone** (EL3/secure world) is a *separate* isolation mechanism, not virtualization.
- **RISC-V**: the **H extension** (ratified v1.0, December 2019) adds HS-mode plus VS/VU guest modes and two-stage address translation; it is **mandatory in the RVA23 application profile**, so application-class RISC-V is expected to support it. KVM is upstream, and QEMU has supported RISC-V virtualization since 7.0. Interrupt virtualization comes from the **AIA**, and device assignment from the **IOMMU**. This matters for [[12-1 RISC-V for Communication Infrastructure]]: a RISC-V baseband or edge box can be virtualized the same way an ARM one can.
- Nested virtualization, and paravirt interfaces (`virtio`, PV timers, PV spinlocks), reduce exit frequency.

### 7.5 Partitioning hypervisors and mixed criticality
- **Static partitioning** (Jailhouse, Bao, ACRN's pre-launched VMs, Xen with `dom0-less` + cpupools) assigns CPUs, memory and devices exclusively at boot — no hypervisor scheduling, so no scheduler-induced jitter. This is the argument for running a real-time control loop beside Linux on the same SoC.
- **The caveat to state honestly**: static core assignment removes *scheduler* interference but not *temporal* interference through the shared last-level cache, memory controller and interconnect. The interference argument is narrowed, not closed.
- **Project status, stated accurately**: the public Siemens Jailhouse repository's latest tag is v0.12 (Feb 2020) with the last commits in January 2023 — treat it as a design worth studying, not an actively maintained supplier position, and verify any vendor fork separately (`VERIFY` before citing it in a safety context).
- For **Linux + RTOS on one SoC**, the more common shipping pattern is heterogeneous: OpenAMP with **remoteproc** (lifecycle, firmware load) and **rpmsg** (messaging, exposed as `/dev/rpmsg*` and `/sys/class/remoteproc/`), e.g. Linux on the A-cores plus an RTOS/bare-metal core for the deterministic loop — see [[07-1 Embedded Systems RTOS and Hardware Interfaces]].

### 7.6 Where virtualization meets this vault
- Network functions (UPF, vCU/vDU, RIC) packaged as containers or VMs with SR-IOV dataplane NICs.
- Edge AI: partition an SoC so the inference engine gets dedicated cores and memory while Linux keeps the rest — the partitioning analogue of [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]].
- Test infrastructure: QEMU/KVM for CI of kernel and rootfs images without hardware, plus hardware-in-the-loop for the parts that actually touch the radio.

## 8. Real-time Linux

- **PREEMPT_RT** was merged into mainline in **Linux 6.12** (November 2024) after ~20 years out of tree, initially selectable on **x86 (32/64-bit), arm64 and RISC-V**; **LoongArch** followed in 6.13 and **32-bit ARM** in 7.1.
- What it changes: spinlocks → sleeping RT-mutexes, interrupt handlers threaded by default, RCU callbacks in threads, `local_lock` per-CPU sleeping locks, and a redesigned `printk` that no longer blocks.
- **Four preemption models**, mutually exclusive in `kernel/Kconfig.preempt`: `PREEMPT_NONE`, `PREEMPT_VOLUNTARY`, `PREEMPT` (full), `PREEMPT_RT`. Switching requires a rebuild and reboot, not a module load. Verify with `zcat /proc/config.gz | grep CONFIG_PREEMPT_RT`.
- **Verify, don't assume**: measure with **`cyclictest`** (rt-tests). On tuned hardware, worst-case wakeup latency is tens of microseconds; RTOS designs bound latency *by construction* to single-digit microseconds. RT Linux is validated empirically; an RTOS is argued structurally. Honest framing for interviews: PREEMPT_RT gives a *measured* bound, not a proved one.
- **Userspace must cooperate**: an RT kernel alone gives you nothing. You need `SCHED_FIFO`/`SCHED_RR` (or `SCHED_DEADLINE`), core isolation, `mlockall()`, priority-inheritance mutexes, and no page faults on the hot path.
- **Companion knobs**: `NO_HZ_FULL`, `CPUSETS`, `CPU_ISOLATION`, `HZ_1000`, `threadirqs` (forced IRQ threading), `hwlat_detector`, `osnoise` tracer (finds the *source* of latency, not just its magnitude).
- Related: [[07-1 Embedded Systems RTOS and Hardware Interfaces]] for when Linux is the wrong answer.

## 9. Recent kernel capabilities worth citing in interviews

- **EEVDF** replaced CFS as the default scheduler in **6.6** — lower wakeup-latency jitter, and it invalidates old CFS tuning knobs (`sched_latency_ns`, `sched_min_granularity_ns`).
- **sched_ext** (merged **6.12**, formally part of **7.0**): scheduling policy implemented as a BPF program, loadable and hot-swappable at runtime, with a watchdog fallback to the fair scheduler. Per-cgroup sub-schedulers and the fixed `ops.dequeue()` callback landed in **7.1**. Directly relevant to "how do I give a workload its own policy" questions.
- **Rust in the kernel**: introduced in 6.1 as experimental and graduated from experimental status in **7.0** (April 2026) — a peer language for *new* drivers, not a rewrite of C.
- **Wi-Fi 8 (802.11bn) groundwork** landed in the Linux wireless stack in 7.0 — the Linux counterpart of [[04-1 WLAN - Wi-Fi Generations Evolution]].
- **eBPF progression**: from packet filtering to tracing, networking, security and now scheduling — the single most leveraged kernel skill for observability and dataplane work.

## 10. The "can you actually do this" checklist

Skills to be able to demonstrate, in increasing order of difficulty:

1. Cross-compile a kernel and rootfs, boot a board, get a serial console.
2. Add a device tree node and make an existing driver bind to it.
3. Write and load an out-of-tree module; add a sysfs attribute; debug an Oops.
4. Write a character driver with blocking `read`, `poll`, and `mmap`.
5. Handle an interrupt correctly with a threaded handler and a workqueue.
6. Do a DMA transfer correctly on a non-coherent platform (sync points, alignment, DMA mask).
7. Build a multi-process daemon set with Unix sockets, fd passing, and an epoll reactor.
8. Measure and reduce tail latency: `perf`, ftrace `wakeup` tracer, `osnoise`, cyclictest.
9. Isolate cores, pin interrupts, enable PREEMPT_RT, and *measure the result*.
10. Package the whole thing: reproducible image, A/B OTA with rollback, watchdog, signed artifacts.

## Anchors — verified facts (check before repeating)

- **Kernel versions as of October 2026**: mainline 7.3 (18 Oct 2026); maintained LTS branches 6.18, 6.12, 6.6, 6.1, 5.15, 5.10.
- **PREEMPT_RT** merged into mainline in **6.12** (Nov 2024) for x86 (32/64-bit), arm64 and RISC-V; **LoongArch in 6.13**; **32-bit ARM in 7.1** (April 2026). Verify a running system with `zcat /proc/config.gz | grep CONFIG_PREEMPT_RT`; validate with `cyclictest`.
- **EEVDF** replaced CFS as the default scheduler in **6.6**.
- **Linux 7.0** released **12 April 2026**: Rust support graduated from experimental, sched_ext formally included, XFS self-healing, AccECN on by default, Wi-Fi 8 (802.11bn) groundwork in the wireless stack.
- **sched_ext**: merged 6.12; `ops.dequeue()` fixed and per-cgroup sub-schedulers landed in **7.1**.
- **Yocto Project**: current LTS **6.0 "Wrynose"** (April 2026, supported to April 2030); **6.1 "Blacksail"** in active development; previous LTS **5.0 "Scarthgap"** supported to April 2028.
- **Buildroot** **2026.08** released 4 September 2026; LTS branch **2025.02.x** through March 2028.
- **RISC-V H extension** v1.0, ratified **December 2019**; HS/VS/VU modes plus two-stage address translation; mandatory in the **RVA23** application profile; KVM upstream and QEMU RISC-V virtualization support since **7.0**.
- **Jailhouse** public repository: latest tag v0.12 (Feb 2020), last public commits January 2023 — `VERIFY` current status with any vendor before relying on it.
- **nftables** is the in-kernel successor to iptables (available since 3.13); `conntrack` underpins NAT and stateful firewalling.
- **io_uring** was introduced in 5.1 (2019); **XDP** in 4.8 and **AF_XDP** in 4.18 — useful when dating a "modern" kernel feature in a design discussion.

## Related

- [[07-3 Embedded Software Architecture - Patterns, Layering and Wireless System Structure]] — the architecture layer: HAL/BSP separation, execution models, OTA/rollback design, safety and partitioning rationale
- [[13-1 Programming Languages Toolchain and Performance Engineering]] — build systems, kernel-bypass options, profiling method
- [[13-2 C and C++ Programming - Language Features, STL and Systems Practice]] — kernel C conventions, `container_of`, user-space C/C++ for drivers' tools and daemons
- [[07-1 Embedded Systems RTOS and Hardware Interfaces]] — when RTOS beats Linux; OpenAMP/rpmsg/remoteproc heterogeneous pairing
- [[08-1 DPDK User Plane and 5G UPF]] — VFIO, hugepages, core isolation, NAPI bypass
- [[12-1 RISC-V for Communication Infrastructure]] — H extension, AIA, IOMMU on RISC-V targets
- [[08-2 Cloud-Edge-End Collaboration and Heterogeneous Computing]] — partitioning, memory pooling, NUMA
- [[04-1 WLAN - Wi-Fi Generations Evolution]] and [[04-3 WLAN Ecosystem - WFA, EasyMesh and prpl]] — nl80211/cfg80211/mac80211 as the Linux side of Wi-Fi
- [[10-2 Agent Systems and Edge Orchestration]] — IPC and sandboxing model for on-device agents
- [[01-4 Cellular IoT RedCap eRedCap and NTN]] — keepalive and lossy-link socket tuning
