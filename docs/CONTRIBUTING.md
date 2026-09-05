# Contributing

Keep this a small portable collection of Markdown instructions, topic cards and progress files. Improvements should make a lesson easier to run or its evidence easier to trust.

## Before proposing a change

1. Read [INSTRUCTIONS.md](../INSTRUCTIONS.md), then only the scoped instruction module affected by your change; see [ARCHITECTURE.md](ARCHITECTURE.md) for ownership.
2. Use fictional data only. Do not submit `courses/current/`, private backups, real lesson transcripts, account details or audio recordings.
3. For a curriculum change, state the communicative purpose, level assumptions, prerequisite impact and a task that demonstrates success. Cite current primary sources where they support a claim; distinguish your design choices.
4. Keep AGENTS.md and CLAUDE.md as tiny adapters. Put always-needed rules in INSTRUCTIONS and action-specific rules in one `instructions/` module; do not duplicate them. Adjust templates/examples when the data contract changes.

## Topic and language changes

Each topic needs an ID, can-do result, situation, useful chunks, relevant grammar, listening and speaking objectives, success criterion, prerequisites, review trigger and exact chat title. Keep IDs stable. Check both forward prerequisites and references in the demo/lesson examples. Include familiar written interaction and simple mediation, not only grammar and monologues.

A new language requires its own appropriate phrases, sound/grammar targets and context. Literal translation of the German cards is not sufficient. State who reviewed the language and what remains provisional. Do not advertise official CEFR alignment without external evidence.

## Verify the change

Walk through the ten scenarios in [QA.md](QA.md). Check cold versus supported evidence, voice versus text, interrupted saves and a new model with no chat history. Confirm all internal links and all codes/chat names still agree. If Python is already installed, the optional maintainer check is:

```text
python tools/check_repository.py
```

This read-only check requires no additional packages. Learners never need to run it. It checks links, required files, topic fields/dependencies, template/demo state and evidence references; it cannot validate teaching quality or a CEFR level. Record actual checks and unresolved limitations in QA rather than marking untested behavior as passed.

For any proposed public contribution, inspect the changed files for private information and respect rights to linked materials. The MIT license applies to original repository material, not third-party content. No automation in this project submits or publishes a contribution for you.
