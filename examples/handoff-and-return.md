# No-history handoff, recovery and return

These are file-flow simulations, not proof of real client execution.

## A new model on the next day

Assume the [demo snapshot](demo-course/README.md) and a simulated date of 2026-08-13. With no earlier chat history, the model reads INSTRUCTIONS and compact current state, scans session/assessment metadata, and loads relevant rows, evidence and cards through the progressive startup procedure. It identifies four completed sessions, no seven-lesson check yet, E001 recurring, Q002 due next_session and the exact thematic title in TOPICS. It can prepare the [weak-topic review](weak-topic-review.md) using files alone. Missing chat-preference fields in this older snapshot do not imply authorization to create tasks.

For an actual learner, perform this same procedure in `courses/current/`, not the demo. Never quietly replace the real local date with this example date.

## A month later

Assume the same unchanged snapshot and simulated date 2026-09-12. Last lesson was 2026-08-12: a 31-day gap. The diagnostic was on 2026-08-01 and no monthly check is recorded. Return and monthly triggers coincide; offer one gentle combined check rather than two exams.

Ask first whether goals/time changed, then sample DE-A1-01, DE-A1-05 and DE-A2-03 with support adjusted to actual attempts. Do not assume three usable topics: only the introduction was stable. Record cold results before teaching. If the greeting still succeeds, preserve it; if a specific skill regresses, queue it. Old dates alone cannot downgrade it.

Use A002 for the combined return/monthly assessment; record return and monthly triggers, four completed lessons covered, and no seven-lesson threshold. A checkpoint is not itself a counted lesson. A separately completed return lesson would need its own S005 evidence. If the learner has only five minutes, save a partial assessment and defer remaining sampling without inventing a result.

## An interrupted save

Suppose an actual LOG session has save_state pending with a recorded goal, observed response and intended updates for DE-A2-03, E001, Q002 and H005. TOPICS was updated but the queue was not. The new model rereads all affected files, matches the IDs, applies the missing queue/homework changes from the recorded intent, then rereads and marks complete. It does not duplicate the session or recount it twice.

If the pending journal has no actual final-task evidence, a proposed usable status must not be applied. Preserve unknowns, retain supported state and ask for missing information only if it cannot be recovered. If PROFILE alone is missing, create only PROFILE and recover preferences from known sources or the learner, preserving all surviving course data.

## Read-only client

If the model can read but cannot write, it says “Progress is not saved”, then provides the complete updated files for manual saving. It does not end with “saved” or trust another chat to remember. Without file reading, the manual handoff also needs route/topic content and dependencies, not only the progress summary.
