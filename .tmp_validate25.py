import re, glob, os

fence = re.compile(r"```.*?```", re.S)
span = re.compile(r"`[^`\n]*`")

notes = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob("knowledge-graph/*.md")}
print("vault files:", len(notes))

bad = 0
for p in sorted(glob.glob("knowledge-graph/*.md")):
    s = open(p, encoding="utf-8").read()
    s2 = span.sub("", fence.sub("", s))
    for m in re.finditer(r"\[\[([^\]]+)\]\]", s2):
        t = m.group(1).split("|")[0].split("#")[0].strip()
        if t not in notes:
            print("BROKEN LINK", os.path.basename(p), "->", t)
            bad += 1
    if s.count("```") % 2:
        print("ODD FENCE", p); bad += 1
    if re.search(r"[\u4e00-\u9fff]", s):
        print("CJK", p); bad += 1
    if not s.startswith("---\n"):
        print("NO FRONTMATTER", p); bad += 1
    elif "copyright" not in s.split("---")[1]:
        print("NO COPYRIGHT FM", p); bad += 1
    if not s.rstrip().endswith("All rights reserved."):
        print("NO FOOTER", p); bad += 1

print("vault issues:", bad)

# duplicate consecutive lines and table headers
dup = 0
for p in glob.glob("**/*.md", recursive=True):
    lines = open(p, encoding="utf-8").read().split("\n")
    for i in range(len(lines) - 2):
        a, b, c = lines[i], lines[i + 1], lines[i + 2]
        if a.startswith("|") and b.strip() == "" and c == a:
            print("DUP HDR", p, i + 1); dup += 1
    for i in range(len(lines) - 1):
        a, b = lines[i].strip(), lines[i + 1].strip()
        if len(a) > 40 and a == b and not a.startswith("|"):
            print("DUP LINE", p, i + 1, a[:60]); dup += 1
print("dups:", dup)

# stale group ids above 08
stale = [(p, m.group(0)) for p in glob.glob("**/*.md", recursive=True)
         for m in re.finditer(r"(?<![\d\-])(09|1[0-9])-(\d)(?!\d)", open(p, encoding="utf-8").read())]
print("stale ids:", stale)

# readlist structure
s = open("readlist.md", encoding="utf-8").read()
heads = re.findall(r"^## (.+)$", s, re.M)
print("readlist headings:", len(heads))
print("  first:", heads[0], "| last:", heads[-1])
print("  entries:", len(re.findall(r"^- \*\*\[", s, re.M)))
for h in heads:
    if re.match(r"^0?\d+", h):
        pass
print("  section order:", [h.split(" ·")[0] for h in heads if re.match(r"^\d", h)])

# new note stats
p = "knowledge-graph/02-5 WLAN - STA-AP Discovery, Authentication and Association.md"
s = open(p, encoding="utf-8").read()
print("new note lines:", s.count("\n"), "| mermaid:", len(re.findall(r"```mermaid", s)),
      "| refs:", len(re.findall(r"^\d+\. ", s, re.M)))
