# Course setup — load only for setup

Return to [the core](../INSTRUCTIONS.md) after this procedure. For a fresh course, copy the nine clean files from `templates/state/` to `courses/current/`, excluding README. Never overwrite surviving state. If any state file exists, create only missing files, recover the stage from evidence and ask only for necessary unknowns. A missing PROFILE must not reset the other eight files.

Set `setup_stage: questions`. Ask these one at a time, save each answer immediately and allow unknown/skip or an already-combined answer:

1. Native/preferred explanation language.
2. Target language.
3. What the learner can already do; rough beginner/A1/A2/B1 self-report.
4. Practical goal and country/setting.
5. Realistic lesson length and days per week.
6. Interests and broad work area for examples.
7. First priority: speaking, listening, exam, work or everyday interaction.

Default, only if time is unspecified: propose 20 minutes three times weekly and label it adjustable. Ask an exact exam name later if relevant; do not assume Goethe or legal requirements. Never request addresses, identity documents, employer secrets or API keys; aliases and fictional details are welcome.

Set `setup_stage: diagnostic`, then read [ASSESSMENTS.md](ASSESSMENTS.md) and run its diagnostic. Build PLAN through A1–B1 from the route and dependencies, with provisional skill profile, first focus and next three topics/reasons; do not promise a finish date. Experienced learners can sample ahead while untested prerequisites remain visible.

German uses `routes/german/README.md`; populate TOPICS with all 42 exact codes/titles, initially `not_started` except genuinely sampled topics. For another language, adapt `curriculum/` into `courses/current/CURRICULUM.md` with complete cards/index, point PLAN to it, populate TOPICS from that index and mark it provisional pending competent teacher review. Do not relabel German cards as another language.

Chat choice: preserve an explicit earlier learner request. Store PROFILE `chat_mode` as `auto_topics`, `manual_topics` or `in_place`, plus the actual authorization. If no choice exists and creation is available, ask once whether to create a separate chat for every topic in this same local project folder. A yes is ongoing course authorization; do not ask at every topic. If unavailable, keep the requested preference for a future capable client and explain the manual fallback. Default to `manual_topics` if no preference is known. Blank templates/examples are never authorization.

Set `setup_stage: ready` only after all nine files, route references and first target are consistent and the save is verified through [STATE.md](STATE.md). Then read [HANDOFF.md](HANDOFF.md) to prepare the first topic. Setup is not a counted lesson. If interrupted, retain the exact stage and resume it.
