"""Read-only, standard-library checks for the public Markdown template.

Run from any working directory with Python 3.10+. No learner data is read.
This verifies structural contracts, not CEFR alignment or model behavior.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from datetime import date, timedelta
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
counts = {}

def check(condition, message):
    if not condition:
        errors.append(message)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

STATE = ["PROFILE", "PLAN", "TOPICS", "ERRORS", "PHRASES",
         "REVIEW_QUEUE", "LOG", "ASSESSMENTS", "HOMEWORK"]
required = ["README.md", "README.ru.md", "QUICKSTART.md", "INSTRUCTIONS.md",
            "AGENTS.md", "CLAUDE.md", "LICENSE", ".gitignore", ".gitattributes",
            "curriculum/README.md", "routes/german/README.md", "courses/README.md",
            "examples/README.md", "examples/demo-course/README.md"]
required += [f"docs/{name}.md" for name in
             ["PEDAGOGY", "ARCHITECTURE", "PRIVACY", "LIMITATIONS", "CONTRIBUTING", "SOURCES", "QA"]]
required += [f"{folder}/{name}.md" for folder in ["templates/state", "examples/demo-course"] for name in STATE]
required += [f"{folder}/{level}.md" for folder in ["curriculum", "routes/german"] for level in ["A1", "A2", "B1"]]
required += [f"instructions/{name}.md" for name in ["SETUP", "LESSONS", "ASSESSMENTS", "STATE", "HANDOFF"]]
required += [f"routes/german/topics/DE-{level}-{number:02d}.md" for level in ["A1", "A2", "B1"] for number in range(1, 15)]
for name in required:
    check((ROOT/name).is_file(), f"Missing required file: {name}")
if errors:
    print("\n".join(errors))
    sys.exit(1)

# Scan only public content, never courses/current or ignored/private directories.
files = list(ROOT.glob("*.md"))
for folder in ["curriculum", "routes", "templates", "examples", "docs"]:
    files += list((ROOT/folder).rglob("*.md"))
files += [ROOT/"courses/README.md"]
files = sorted(set(files))
texts = {p: p.read_text(encoding="utf-8") for p in files}
counts["markdown_files"] = len(files)
core_bytes=(ROOT/"INSTRUCTIONS.md").stat().st_size
check(core_bytes <= 10_000, f"Tutor core exceeds 10 KB budget: {core_bytes} bytes")
counts["tutor_core_bytes"] = core_bytes
for name in ["SETUP", "LESSONS", "ASSESSMENTS", "STATE", "HANDOFF"]:
    size=(ROOT/f"instructions/{name}.md").stat().st_size
    check(size <= 6_000, f"Instruction module exceeds 6 KB budget: {name} = {size} bytes")

def anchors(text):
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    seen = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        number = seen.get(slug, 0)
        seen[slug] = number + 1
        result.add(slug if not number else f"{slug}-{number}")
    return result

link_count=0
for path, text in texts.items():
    check(len(text.strip()) > 80, f"Empty/formal-only document: {path.relative_to(ROOT)}")
    check("\ufffd" not in text, f"Invalid replacement character: {path.relative_to(ROOT)}")
    # All authored links use ordinary inline syntax; code samples have no pseudo-links.
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
        parts=urlsplit(target.strip("<>"))
        if parts.scheme or parts.netloc:
            continue
        link_count += 1
        destination=(path.parent/unquote(parts.path)).resolve() if parts.path else path
        check(destination.is_relative_to(ROOT), f"Link escapes project: {path.relative_to(ROOT)} -> {target}")
        check(destination.exists(), f"Broken link: {path.relative_to(ROOT)} -> {target}")
        if parts.fragment and destination.is_file():
            check(unquote(parts.fragment) in anchors(destination.read_text(encoding="utf-8")),
                  f"Missing anchor: {path.relative_to(ROOT)} -> {target}")
counts["internal_links"] = link_count

cards={}
deps={}
fields=["Can-do", "Situation", "Chunks and patterns", "Grammar in service of the task",
        "Listening goal", "Speaking goal", "Practical success", "Dependencies",
        "Return to review", "Thematic chat"]
for path in sorted((ROOT/"routes/german/topics").glob("DE-*.md")):
    text=path.read_text(encoding="utf-8")
    match=re.search(r"^# (DE-(A1|A2|B1)-\d{2}) — (.+)$",text,re.M)
    check(bool(match), f"Topic card heading missing: {path.name}")
    if not match:
        continue
    code,level,title=match.groups()
    check(path.stem==code, f"Topic filename/code mismatch: {path.name}")
    check(code not in cards, f"Duplicate topic: {code}")
    cards[code]=title
    for field in fields:
        check(bool(re.search(r"\*\*"+re.escape(field)+r":\*\*\s+\S",text)), f"{code}: missing {field}")
    check(f"`{code} — {title}`" in text, f"Chat title mismatch: {code}")
    dep_match=re.search(r"\*\*Dependencies:\*\* (.+)",text)
    deps[code]=re.findall(r"DE-(?:A1|A2|B1)-\d{2}",dep_match.group(1)) if dep_match else []

topic_sizes=[p.stat().st_size for p in (ROOT/"routes/german/topics").glob("DE-*.md")]
check(bool(topic_sizes) and max(topic_sizes) <= 3_000, "A topic card exceeds the 3 KB context budget")
counts["largest_topic_card_bytes"] = max(topic_sizes) if topic_sizes else 0

for level in ["A1", "A2", "B1"]:
    level_index=read(f"routes/german/{level}.md")
    check((ROOT/f"routes/german/{level}.md").stat().st_size <= 4_000, f"{level} index exceeds 4 KB context budget")
    level_ids=re.findall(rf"^\| (DE-{level}-\d{{2}}) \|",level_index,re.M)
    check(len(level_ids)==14 and len(set(level_ids))==14, f"{level}: expected 14 unique index rows")
    generic=read(f"curriculum/{level}.md")
    generic_ids=re.findall(r"^\| (A1-\d{2}|A2-\d{2}|B1-\d{2}) \|",generic,re.M)
    check(len(generic_ids)==14 and len(set(generic_ids))==14, f"Framework {level}: expected 14 unique rows")

for code,parents in deps.items():
    check(code not in parents,f"Self dependency: {code}")
    for parent in parents:
        check(parent in cards,f"Unknown dependency {parent} in {code}")
seen=set()
visiting=set()
def visit(code):
    if code in visiting:
        errors.append(f"Dependency cycle at {code}")
        return
    if code in seen or code not in cards:
        return
    visiting.add(code)
    for parent in deps[code]:
        visit(parent)
    visiting.remove(code)
    seen.add(code)
for code in cards:
    visit(code)
counts["topic_cards"] = len(cards)
counts["dependency_edges"] = sum(map(len,deps.values()))

index=read("routes/german/README.md")
index_rows=re.findall(r"^\| (DE-(?:A1|A2|B1)-\d{2}) \| `([^`]+)`",index,re.M)
check(len(index_rows)==42 and len({r[0] for r in index_rows})==42,"Route index must have 42 unique rows")
for code,title in index_rows:
    check(title==f"{code} — {cards.get(code)}",f"Index title mismatch: {code}")

valid_status={"not_started","learning","unstable","usable","stable"}
topic_table=read("examples/demo-course/TOPICS.md")
topic_rows=[]
for line in topic_table.splitlines():
    if re.match(r"\| DE-(?:A1|A2|B1)-\d{2} \|",line):
        cols=[c.strip() for c in line.strip("|").split("|")]
        check(len(cols)==7,f"Wrong topic table width: {cols[0]}")
        topic_rows.append(cols)
check(len(topic_rows)==42 and len({r[0] for r in topic_rows})==42,"Demo must have 42 unique topic rows")
for row in topic_rows:
    code,status,title=row[:3]
    check(code in cards,f"Unknown demo topic: {code}")
    check(status in valid_status,f"Unknown status: {code} = {status}")
    check(title==f"{code} — {cards.get(code)}",f"Demo title mismatch: {code}")

log=read("examples/demo-course/LOG.md")
assessments=read("examples/demo-course/ASSESSMENTS.md")
sessions=re.findall(r"^## (S\d{3}) — (\d{4}-\d{2}-\d{2})$",log,re.M)
assessment_ids=re.findall(r"^## (A\d{3}) —",assessments,re.M)
evidence_ids={s for s,d in sessions}|set(assessment_ids)
check(len(sessions)==4 and len({s for s,d in sessions})==4,"Demo must contain four unique session evidence records")
check(log.count("- completed: yes; save_state: complete")==4,"Four demo sessions must be completed and saved")
for name in STATE:
    t=read(f"examples/demo-course/{name}.md")
    for code in re.findall(r"\bDE-(?:A1|A2|B1)-\d{2}\b",t):
        check(code in cards,f"Unknown topic in demo {name}: {code}")
    for evid in re.findall(r"\b[SA]\d{3}\b",t):
        check(evid in evidence_ids,f"Missing evidence in demo {name}: {evid}")

entity_files={"E":"ERRORS", "P":"PHRASES", "Q":"REVIEW_QUEUE", "H":"HOMEWORK"}
defined=set(evidence_ids)
for prefix,name in entity_files.items():
    ids=re.findall(r"^\| ("+prefix+r"\d{3}) \|",read(f"examples/demo-course/{name}.md"),re.M)
    check(len(ids)==len(set(ids)),f"Duplicate IDs in demo {name}")
    defined.update(ids)
# Historical homework is stored in the log once it leaves the current homework file.
defined.update(re.findall(r"\bH\d{3}\b",log))
for name in ["TOPICS","ERRORS","PHRASES","REVIEW_QUEUE","HOMEWORK"]:
    for eid in re.findall(r"\b[EPQH]\d{3}\b",read(f"examples/demo-course/{name}.md")):
        check(eid in defined,f"Missing entity reference in demo {name}: {eid}")

queue=read("examples/demo-course/REVIEW_QUEUE.md")
queue_rows=[]
for line in queue.splitlines():
    if re.match(r"\| Q\d{3} \|",line):
        cols=[c.strip() for c in line.strip("|").split("|")]
        check(len(cols)==9,"Wrong queue table width")
        queue_rows.append(cols)
open_keys=[(r[1],r[2]) for r in queue_rows if r[7] in {"open","waiting_for_audio"}]
check(len(open_keys)==len(set(open_keys)),"Duplicate open topic/focus queue item")
dates=dict(sessions)
check((date.fromisoformat(dates['S002'])-date.fromisoformat(dates['S001'])).days==7,"Demo retained introduction interval is not seven days")
check((date.fromisoformat(dates['S002'])+timedelta(days=30)).isoformat() in queue,"Demo stable retrieval date incorrect")
check(any(r[1]=='DE-A2-03' and r[3]=='regression' and r[5]=='next_session' for r in queue_rows),"Demo regression queue entry missing")

for name in STATE:
    text=read(f"templates/state/{name}.md")
    check(not re.search(r"^\| (?:DE-(?:A1|A2|B1)-\d{2}|[EPQH]\d{3}) \|",text,re.M), f"Template contains learner row: {name}")
    check("- completed: yes" not in text,f"Template contains completed evidence: {name}")
for adapter in ["AGENTS.md","CLAUDE.md"]:
    text=read(adapter)
    check(len(text.splitlines())<=12,f"Adapter too long: {adapter}")
    check("INSTRUCTIONS.md" in text and "courses/current/" in text,f"Adapter missing startup reference: {adapter}")

ignore=read('.gitignore')
check('/courses/current/' in ignore and '/courses/backups/' in ignore,"Private course/backup ignore rules missing")
# This is a simple accidental-data check, not a comprehensive secret scanner.
for path,text in texts.items():
    check(not re.search(r"(?:[A-Za-z]:[\\/]Users[\\/]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|BEGIN (?:RSA )?PRIVATE KEY)",text),
          f"Possible private path/credential: {path.relative_to(ROOT)}")
counts['demo_sessions']=len(sessions)
counts['clean_state_templates']=len(STATE)
if errors:
    print(f"FAIL: {len(errors)} issue(s)")
    for error in errors:
        print('- '+error)
    sys.exit(1)
print("PASS: structural checks")
for key,value in counts.items():
    print(f"{key}: {value}")
print("Not assessed by this tool: teaching quality, actual audio, live-client behavior, external URLs, CEFR validity.")
