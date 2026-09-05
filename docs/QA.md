# Quality report

Review date: 2026-09-05. Scope: public Markdown template, 42 German topic cards, nine clean state files, a fictional demo and lesson examples. No publication, push, uploads of project files, real learner data or API keys were involved.

## What this review establishes

For the original edition, three independent AI reviewers examined (1) the pedagogy/evidence rules, (2) CEFR scope and the German route, and (3) first use plus Codex/Claude portability. The later topic-handoff update was reviewed locally through the additional scenarios below; it was not re-reviewed by those agents. These are static reviews and fictional scenario simulations, not external teacher validation, live-client integration tests or real audio/learner trials.

The optional read-only [repository checker](../tools/check_repository.py) validates file structure and references. It passed against the completed files; details are below.

## Ten required scenarios

| # | Scenario and simulated input | Trace and expected observable outcome | Review outcome |
| --- | --- | --- | --- |
| 1 | New user downloads/extracts project and types Set up my language course | README/QUICKSTART → adapter → INSTRUCTIONS. courses/current absent; create nine missing files, ask native language first, wait for reply | Walkthrough passed; no code installation required |
| 2 | Learner answers setup questions and attempts diagnosis | PROFILE stage questions → diagnostic; prompts arrive one at a time; A001 owns observations; PLAN/TOPICS use pointers; untested skills/topics stay unknown/not_started | Walkthrough passed; interrupted setup resumes at next question |
| 3 | First short lesson in a text-only client | A1 example requests an attempt, then corrects/reuses; reading is explicitly reading; spoken_output/listening not_assessed; topic learning with modality gap | Walkthrough passed; no false audio or stable claim |
| 4 | Learner finishes a lesson and progress is saved | Pending LOG entry records evidence and intended edits; changed tables use existing IDs; files reread before complete; partial sessions do not count as finished | File-flow simulation passed; cooperative Markdown procedure, not atomic transaction |
| 5 | Old error returns | Demo S003 success → S004 recurring E001 with help/reuse/transfer failure; DE-A2-03 becomes unstable; Q002 updated rather than duplicated | Cross-file evidence and date review passed |
| 6 | Tutor directs learner to a thematic review chat | TOPICS owns DE-A2-03 — Talking about yesterday; auto_topics reuses/prepares an authorized destination; manual mode gives exact title and code-specific command | File-flow walkthrough passed; fallback needs no chat API or old chat history |
| 7 | New model has no history, simulated date 2026-08-13 | Progressive reads across current state, history metadata and referenced records recover four completed lessons, E001, Q002 due next_session, exact title and foundation gaps | Same next step reconstructed; original independent review read all nine files, updated local walkthrough uses targeted reads |
| 8 | Return after a month, simulated date 2026-09-12 | Demo last session 2026-08-12 gives 31-day gap; initial diagnostic 2026-08-01 makes monthly check due; one combined return/monthly sample; preserve untested gaps | Walkthrough passed; no blanket downgrade or double-counted lesson |
| 9 | Codex project startup | Root AGENTS.md points to INSTRUCTIONS and courses/current; explicit read command available if discovery fails | Documentation/static compatibility passed; no separate live Codex learning trial performed |
| 10 | Claude Code project startup | Root CLAUDE.md points to the same instruction/state files; no reliance on proprietary memory or automatic chat creation | Documentation/static compatibility passed; Claude Code was not launched for this review |

Detailed scenarios: [setup](../examples/setup-and-diagnostic.md), [first lesson](../examples/a1-short-lesson.md), [weak review](../examples/weak-topic-review.md), [handoff/return/recovery](../examples/handoff-and-return.md), [populated demo](../examples/demo-course/README.md).

## Additional edge cases inspected

- Lost PROFILE with eight surviving files: create only the missing file, recover preferences/stage and preserve observed history.
- Interrupted pending save: update only missing actions by ID; never count a session twice or promote without its evidence.
- Check deferred at lesson seven: the uncovered threshold stays due at counts eight and nine. A combined monthly/seven-lesson assessment covers both triggers once.
- Stable retention: requires a cold independent success before any refresher and a sufficient interval; a post-repair success supports usable, not retrospective retention.
- No audio: one waiting_for_audio item per topic/focus; written practice continues and old dated evidence remains distinct from new unassessed modalities.
- Alternative language: create an adapted route and populate its own index, not the German topic codes; mark provisional pending qualified review.
- Concurrent edits or read-only access: pause conflicting writes; report unsaved progress with complete manual file contents if necessary.
- Multiple weak topics: registered mixed-review title, separate topic evidence and queue items, one completed session count.

## Issues found and corrected before final review

| Issue | Correction |
| --- | --- |
| Missing PROFILE could trigger a blanket copy of templates | Fresh setup requires no surviving state; repair creates only missing files |
| Delayed retention could be confused with relearning at a later session | Added explicit cold-before-teaching evidence requirement |
| A deferred seven-lesson check could be missed after the counter moved past seven | Defined the largest reached uncovered threshold and covered-threshold fields |
| Universal setup wording could populate German topics for another language | Restricted German population and added adapted-index population |
| Return procedure assumed several usable topics already existed | Added smaller sampling of previously attempted topics |
| Manual no-read fallback omitted route content | Listed required route/cards/dependencies and clean setup templates |
| B1 KI return criterion partly assessed AI knowledge instead of language | Scenario supplies facts; check ability to express the stated limitation and checking need |
| B1 comparison/complaint criteria could grade choice quality or imply an unclear agreement | Grade expressed reasons; allow explicit unresolved points with a confirmed next action |
| A1 rubric could count reasonable question rephrasing as a hint | Allowed recorded support that does not supply answer wording |
| Demo audio used origin towns while the card specified a country | Clarified the card as place of origin, town or country |
| Demo phrase states lacked explicit evidence and one example muddied error counting | Added P003/P005 observations and made the sequence error example a single clear target error |

## Automated verification

Command run: `python tools/check_repository.py`. Result: **PASS** on 2026-09-05. The checker is read-only and scans public content only, excluding private learner files.

| Check | Result |
| --- | --- |
| Required files and substantive public Markdown documents | 92 Markdown files present; no empty documents or replacement-character corruption |
| Internal file links and fragments | 375 resolved successfully |
| German card count and required fields | 42 cards, 14 per level; all ten content fields present |
| Topic graph | 100 prerequisite edges; all resolve, no self-dependencies or cycles |
| Route index and demo TOPICS | 42 unique rows each; codes and exact chat titles match cards |
| State templates | Nine clean templates; no learner rows or completed evidence |
| Fictional evidence | Four distinct completed sessions; referenced topic/session/error/phrase IDs resolve |
| Review dates | Seven-day cold introduction interval and 30-day follow-up date agree; recurrent past-topic item due next_session |
| Adapters | Both short, point to the shared instructions and current course |
| Accidental data scan | No matching personal Windows home paths, common key patterns or private-key headers in public Markdown; not a full secret scanner |

Git was initialized locally on branch `main`. `git check-ignore` confirmed the private current course, private backup, `.env` and sample audio paths are excluded. No remote is configured, and no commit, push or publication was performed. The actual learner folder was not created; the public template remains clean.

The independent pedagogy reviewer reread the corrected demo and the final weak-topic/return examples and found no remaining substantial inconsistencies. The CEFR review's topic-level corrections were applied; its conclusion remains a plausible author-designed A1–B1 sequence, not external validation.

## Topic-handoff update — 2026-09-05

The update makes the closing decision explicit, adds authorized automatic topic-chat preparation, retains a manual fallback and uses progressive file reads. The independent reviews above refer to the original edition; the following are local instruction-flow simulations. No real course or lesson task was created to test these branches.

| Scenario | Checked outcome |
| --- | --- |
| Full topic goal passes, no checkpoint due | Final task → verified save → explicit topic-complete message → at most one next topic chat; no need to wait for stable |
| Final task still needs models | Explicit continue-here message; retain learning/unstable as appropriate; no duplicate thematic chat |
| Text-only success on an unassessed topic | Clearly incomplete oral evidence; no invented usable status; progression with gaps remains possible |
| Old usable/stable topic, no audio today | Preserve earlier valid evidence/status; state today's limited check; no downgrade solely for missing access |
| New destination executes initial prompt | Preparation only, no progress writes or routing, waits for learner; on real learner input rereads state and begins |
| Existing destination or repeated start | Match actual course/location and target, reuse the chat, never create a second copy just because the session is new |
| Unsupported tool or wrong directory/worktree | Exact manual title/command; do not copy private data or start a blank course elsewhere |
| Uncertain creation or interrupted registry update | Retain creating/unknown, inspect actual tasks before retry; do not invent identifiers or blindly duplicate |
| Lesson save pending or failed | No creation until progress is verified; recover actual evidence first |
| Completion makes checkpoint due | Recompute count and choose the checkpoint action before another new theme |
| Early stop / end of B1 | Save partial evidence or report final route outcome as appropriate; no invented completion or B2 chat |
| Older course lacks new preference fields | Add missing fields without overwriting progress; unknown authorization is not consent |

Worked closing messages and transitions: [topic-transition example](../examples/topic-transition.md). Chat creation is optional client behavior, not a built-in Markdown runtime. Token savings were not measured. The existing structural checker was rerun; no synthetic test claims actual external chat creation occurred.

## Context-size update — 2026-09-05

The monolithic tutor instruction file was replaced by an 8,001-byte core plus five action-specific modules. The former file measured 33,652 bytes. German level files became compact indexes; each of the 42 complete cards now has its own file. A representative DE-A1-01 card is 1,223 bytes, while the former A1 level file was 15,884 bytes. These byte comparisons establish smaller default reads; they do not predict exact tokens, cache behavior or account charges.

The checker was updated to require all modules/cards, enforce size budgets (10 KB core, 6 KB per scoped module, 4 KB per level index and 3 KB per topic card), and validate card fields, links, dependencies and demo references. Final result: **PASS**, 92 Markdown files, 375 internal links, 42 topic cards and 100 valid dependency edges. Core size is 8,001 bytes; the largest topic card is under the 3 KB limit. No live client billing measurement or real lesson was run.

## Remaining limits

No external educator has validated the German sequence or its CEFR correspondence. No model adherence guarantee, real-learner outcome, audio quality result, formal examination equivalence, concurrent-write safety or complete secret-audit guarantee follows from these checks. Official source pages were opened during research; external link availability is not part of the offline checker. See [LIMITATIONS.md](LIMITATIONS.md) and [SOURCES.md](SOURCES.md).
