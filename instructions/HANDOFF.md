# Topic-chat handoff — load only when routing

Return to [the core](../INSTRUCTIONS.md). Route only after a verified state save. There is no required management chat: any course chat can select the next action.

Use PROFILE `chat_mode` and actual authorization. `auto_topics` authorizes separate chats only within its recorded scope. Never infer authorization from templates. Respect a request to stop without preparing a chat.

## Automatic mode

1. Resolve the due/ready topic or mode. Exact thematic title comes from TOPICS; mixed-review title/codes from PLAN. Check PLAN's chat-location registry and actual client listing if available. Reuse a verified existing destination for this course/topic. A matching title alone is insufficient if multiple course copies exist.
2. Use the same saved project and local course directory. In Codex inspect projects and choose its local environment. Do not choose a worktree, clone, cloud task or projectless folder: ignored private progress may be absent. If same-folder placement cannot be ensured, use the manual fallback.
3. Before creating, add registry state `creating` with target and source event. Make one creation call with exact title and the short prompt below. Do not fork/send the old conversation or select another model unless requested.
4. Store the returned real project/chat ID or link; set `ready` only after confirmed creation. A setup/client ID is not a ready chat ID. If uncertain/interrupted, mark `unknown`, inspect existing tasks before retrying and never blindly duplicate.
5. Show the actual client link/card if available, otherwise the confirmed exact title. Say: “Откройте этот чат и напишите «Начнём».” Stop. The destination waits for the learner and becomes the only writer after starting.

Creation prompt, with actual substitutions:

```text
Prepare the next language lesson in this same local project folder.
Read INSTRUCTIONS.md and use its progressive startup. Target: [code(s)].
Mode: [lesson/review/checkpoint]. Title: [exact title].
This is preparation only: do not route/create chats, teach, write progress or count a lesson.
Briefly name the goal and wait for “Начнём” or “Let's start”. On that reply,
reread current state, resolve pending saves/due checks, and begin with one task
in the learner's preferred explanation language.
```

The preparation restriction ends after the learner starts. An explicit `Start topic CODE` or `Review topic CODE for 15 minutes` binds the destination and prevents routing another copy on arrival. For an incomplete theme, remain in its current chat. A due review reuses that topic chat where possible; mixed review uses its PLAN entry.

## Manual or unavailable mode

Give exactly one fallback: exact title plus `Start topic CODE`; review uses `Review topic CODE for 15 minutes`; mixed review uses `Start a mixed review`. Tell the learner to create/open it in the same project folder. Do not invent links/IDs or claim creation. Remember current-session unavailability; do not repeatedly probe or ask permission. In `in_place`, keep the explicit closing decision and resume on the learner's next message.

Creation failure does not undo the lesson save. A pending/failed save blocks handoff until recovered. If completion makes a checkpoint due, route that before a new topic. At B1 route end, create no B2 chat.
