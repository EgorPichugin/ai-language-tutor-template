# How the files fit together

The project has three layers: shared tutor rules, reusable learning content, and private learner state. It runs through ordinary file reading and editing, with no server or database.

```text
AGENTS.md / CLAUDE.md / explicit user command
                    ↓
        INSTRUCTIONS.md (small router/core)
                    ↓
        one scoped instruction module
                    ↓
       relevant state + one topic card
                    ↓
        observed evidence → verified save
```

## Ownership

[INSTRUCTIONS.md](../INSTRUCTIONS.md) is the only entry point and contains rules needed throughout teaching. It routes setup, lessons, assessments, state and handoff to small files in `instructions/`. [STATE.md](../instructions/STATE.md) contains the canonical ownership table and save protocol. PROFILE holds preferences, PLAN the route, TOPICS current statuses/chat titles, ERRORS patterns, PHRASES chunks, REVIEW_QUEUE dates, LOG lesson evidence, ASSESSMENTS checkpoint evidence, HOMEWORK the current assignment. Do not introduce another summary file that silently becomes a competing authority.

Curriculum files are shared reference content. They never acquire a learner's current status. TOPICS links to the route and evidence instead of copying whole cards. The fictional demo is a separate documentation snapshot; clean templates have no learner observations.

## Identifiers and location

- Topics: language prefix + level + stable number, for example `DE-A2-03`. Renaming a topic's English label must preserve the ID and update all chat-title references together.
- Lesson evidence: S001, S002, …; checkpoints: A001, A002, …. Allocate the next unused ID, never reuse one after a partial session.
- Errors, phrases, review items and homework use E001, P001, Q001 and H001 respectively. Mixed chats use DE-R01 and are registered in PLAN.
- File paths in links are relative to the file containing them. State in both `templates/state/` and `courses/current/` is two directories below the root, so `../../INSTRUCTIONS.md` resolves in each place.
- One active course lives at `courses/current/` per project copy. Another language can use a separate copy. No hidden active-course selector is needed.
- PROFILE owns the chosen chat mode and the learner's actual authorization. PLAN's chat-location registry owns verified client/project/chat identifiers and creation state; it references topic codes, whose exact titles remain in TOPICS.

Each reference must resolve to an existing topic or evidence record. If a model only knows an ID from chat, it reads the file record before relying on it. Top-level adapters are intentionally short and do not contain copies of the tutor policy.

## Smaller startup context

The root adapters are about 0.5 KB each. The always-read tutor core is about 8 KB; the former monolithic version was about 34 KB. A normal lesson additionally loads STATE and LESSONS (about 3 KB each), one topic card (typically about 1–2 KB), relevant learner rows and HANDOFF only when a destination is needed. Setup and assessment procedures stay out of ordinary lesson context.

Topic content is stored as 42 files under `routes/german/topics/`; A1/A2/B1 are compact indexes. Large lesson histories are scanned by headings/metadata and loaded by evidence reference rather than in full. This changes retrieval, not ownership; no competing summary or cached score is introduced. Broader reads remain necessary when state is inconsistent. Byte sizes show structural reduction, not guaranteed billing: tokenizer, caching and client context handling vary.

## Topic handoff

The learner gets an explicit completion decision after the final check and verified save. With auto_topics and the learner's recorded request, the tutor reuses an existing destination or creates one topic chat, using the same saved local project directory. It sends a compact preparation prompt rather than forking the full conversation. The destination waits for learner input and cannot create another chat during preparation.

PLAN records creating before the call and ready only after confirmation; uncertain results require lookup before retry. The parent completes registry updates before the destination writes any progress. Creation failure does not discard the saved lesson. This remains a cooperative protocol; tools and permissions differ between clients. Automatic creation is optional and a precise manual title/command always remains available.

The same-directory choice matters: [Codex documents that worktrees use separate directories and may lack untracked files](https://learn.chatgpt.com/docs/environments/local-environment). A separate worktree must not silently start a blank course when private progress exists in the saved project.

## Recovery and concurrency

Markdown cannot provide a database transaction or automatic lock. The pending-save journal in LOG makes interrupted work inspectable: intent is recorded first, evidence and state are updated by ID, then the changed files are reread before completion is claimed. This is a cooperative convention, not an atomic filesystem guarantee.

Use one writing session at a time. If a file changed unexpectedly, reconcile before saving. A partial lesson retains observed attempts but earns no fabricated final result. If a single state file is lost, reconstruct only that file from surviving evidence and ask about unknown preferences. Never copy nine blank templates over an existing course.

## Portability

Move the repository together with its private `courses/current/` folder. Open that same folder in the new client, read INSTRUCTIONS and course state, then use the usual lesson command. Neither the previous model's memory nor chat creation APIs are required. A ZIP of the public template does not contain your personal progress.

The adapters follow the documented convention of root instruction files in [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Claude Code](https://code.claude.com/docs/en/memory). Client policy, trust settings and access permissions can affect whether files load; [QUICKSTART](../QUICKSTART.md) includes an explicit read command. Documentation review does not guarantee execution in every client version.

## Extension

For another language author a new route index and full cards, then point PLAN to it. For a later level add another curriculum/route file and new topic IDs; existing state roles remain unchanged. No higher-level materials are included in this release. Keep new features optional and file-based; do not turn the core into a scheduling or chat-management application.
