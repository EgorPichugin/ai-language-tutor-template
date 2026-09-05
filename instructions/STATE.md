# State loading and saving

Return to [the core](../INSTRUCTIONS.md) after the required operation.

## Progressive startup

Check that these nine files exist in `courses/current/`: PROFILE, PLAN, TOPICS, ERRORS, PHRASES, REVIEW_QUEUE, LOG, ASSESSMENTS, HOMEWORK. Fresh/partial setup follows [SETUP.md](SETUP.md).

Read PROFILE, PLAN, active REVIEW_QUEUE rows and current HOMEWORK. Scan LOG headings/date/completed/save_state and ASSESSMENTS headings/date/kind/triggers/covered counts. Fully read any pending record. Determine local date (ask if unavailable), unfinished work, last activity, completed count and due checks. Then select a target and load only its TOPICS/prerequisite/review rows, related ERRORS/PHRASES rows and evidence IDs. Use headings/search/ranges for large files; read a full affected file if targeted access is unavailable or inconsistent.

Never rely on another chat's history. Before saving, reread every file being changed. If latest IDs changed since the initial read, stop, explain and reconcile; do not overwrite another writing session.

## File ownership

| File | Sole authority |
| --- | --- |
| PROFILE | Setup answers, preferences, capabilities, chat mode/actual authorization |
| PLAN | Route, skill-placement pointer, next order, deferred checks, mixed-review titles and actual chat-location registry |
| TOPICS | Current topic status, exact thematic title and evidence pointers |
| ERRORS | Recurring error patterns/lifecycle |
| PHRASES | Selected active chunks/retrieval state |
| REVIEW_QUEUE | All review triggers, due dates/stages/resolution |
| LOG | Lesson evidence/completion and save-recovery journal |
| ASSESSMENTS | Diagnostic/checkpoint evidence, skill profile and covered thresholds |
| HOMEWORK | Current assignments/follow-up |

Route files own content; LOG/ASSESSMENTS own observed evidence. Other files reference evidence rather than copying it. Dates for reviews exist only in REVIEW_QUEUE.

## Verified save

Use next unused S001/A001 etc.; upsert existing E/P/Q/H IDs and preserve history.

1. Reread affected files. Add/update LOG journal with `save_state: pending`, session/assessment ID, actual evidence (or ASSESSMENTS pointer), and exact intended changes to topics/errors/phrases/queue/homework/plan.
2. Write evidence to LOG for lessons or ASSESSMENTS for diagnostics/checkpoints. Update only warranted state files. PROFILE changes only for preferences/setup. A partial session is `completed: no`; no invented final task or promotion.
3. Reread affected files and verify IDs, status evidence, dates and intended changes. Mark journal complete and replace the temporary plan with a short completion summary. Claim saved only now.
4. If interrupted, leave pending. Next startup applies only missing changes by ID; never duplicate a session, count or homework. Missing evidence remains unknown and cannot promote status.

If writing is unavailable, say “Progress is not saved” and provide complete changed Markdown files for manual saving. Do not substitute chat memory.

Error lifecycle: `watch` after one noteworthy occurrence; `recurring` after the same pattern in two sessions; `resolving` after later independent reuse; `resolved` after delayed reuse of at least seven days. A recurrence reopens the same ID. Phrase states: `introduced`, `retrieving`, `active`; active requires independent changed-detail reuse.
