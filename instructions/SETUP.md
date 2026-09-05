# Course setup — load only for setup

Return to [the core](../INSTRUCTIONS.md) after this procedure. For a fresh course, copy the nine clean files from `templates/state/` to `courses/current/`, excluding README. Never overwrite surviving state. If any state file exists, create only missing files, recover the stage from evidence and ask only for necessary unknowns. A missing PROFILE must not reset the other eight files.

Set `setup_stage: questions`. Send one numbered questionnaire containing items 1–7 below and item 8 when no earlier explicit chat choice exists. Ask the learner to answer all relevant numbers in one message; `unknown`, `skip` and omitted optional items are valid. Do not split the questionnaire across turns.

1. Native/preferred explanation language.
2. Target language.
3. What the learner can already do; rough beginner/A1/A2/B1 self-report.
4. Practical goal and country/setting.
5. Realistic lesson length and days per week.
6. Interests and broad work area for examples.
7. First priority: speaking, listening, exam, work or everyday interaction.
8. Chat preference: a separate topic chat created automatically when supported, separate chats created manually, or one continuing chat.

After the reply, map and save every supplied answer together. Mark optional omissions as unknown/not provided. Set `setup_questionnaire: answered` and `setup_missing_required: none`. If the target language is missing or ambiguous, use `partial` and `target_language`, then send one compact follow-up containing only that required item; never repeat the full questionnaire. A free-form combined reply is valid even without matching number labels when its meaning is clear.

Default, only if time is unspecified: propose 20 minutes three times weekly and label it adjustable. Ask an exact exam name later if relevant; do not assume Goethe or legal requirements. Never request addresses, identity documents, employer secrets or API keys; aliases and fictional details are welcome.

Set `setup_stage: diagnostic`, then read [ASSESSMENTS.md](ASSESSMENTS.md) and run its diagnostic. Build PLAN through A1–B1 from the route and dependencies, with provisional skill profile, first focus and next three topics/reasons; do not promise a finish date. Experienced learners can sample ahead while untested prerequisites remain visible.

German uses `routes/german/README.md`; populate TOPICS with all 42 exact codes/titles, initially `not_started` except genuinely sampled topics. For another language, adapt `curriculum/` into `courses/current/CURRICULUM.md` with complete cards/index, point PLAN to it, populate TOPICS from that index and mark it provisional pending competent teacher review. Do not relabel German cards as another language.

Chat choice: preserve an explicit earlier learner request and do not ask item 8 again. Store PROFILE `chat_mode` as `auto_topics`, `manual_topics` or `in_place`, plus the actual authorization. Choosing automatic separate topic chats is ongoing course authorization; do not ask at every topic. If creation is unavailable, keep the requested preference for a future capable client and explain the manual fallback. Default to `manual_topics` if item 8 is omitted. Blank templates/examples are never authorization.

Set `setup_stage: ready` only after all nine files, route references and first target are consistent and the save is verified through [STATE.md](STATE.md). Then read [HANDOFF.md](HANDOFF.md) to prepare the first topic. Setup is not a counted lesson. If interrupted, retain the exact stage and resume it.
