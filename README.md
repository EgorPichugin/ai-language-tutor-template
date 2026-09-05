# AI language tutor template

A reusable AI language tutor template for progressing from beginner A1 to independent B1.

[Русская версия](README.ru.md) · [Quick start / Быстрый старт](QUICKSTART.md) · [German route](routes/german/README.md)

Open this folder in a file-capable AI assistant, set up your course, and continue with one command. Your goals, topic evidence, recurring errors, and review dates live in readable Markdown files, so a new conversation can pick up where you stopped.

## Start learning

1. Download the repository with **Code → Download ZIP**, then extract it. Open the extracted folder in Codex or Claude Code. You need your own working AI client with permission to read and edit this folder; this repository does not supply an account or model.
2. Write `Set up my language course` (or `Настрой мой языковой курс`). The tutor asks seven short questions one at a time, then offers a brief diagnostic. You may skip personal questions. If your client supports creating chats, choose separate topic chats once; an existing choice is remembered.
3. Open the prepared topic chat and write `Let's start` (or `Начнём`). If chats must be created manually, the tutor supplies one exact title and command. For later lessons, `Start my next lesson` works from any course chat. The German route has 42 topics across A1, A2, and B1.

No package installation, server, API key configuration, or programming is needed for the template. See [QUICKSTART.md](QUICKSTART.md) if instructions do not load or file writing is unavailable.

## What you get

- A complete German topic route for everyday life in Germany/Austria, work, job search, and simple software/KI project explanations.
- Personal 60-minute or 15–20-minute lessons generated from your needs and previous evidence, rather than a fixed lesson script.
- An explicit end-of-topic decision, with separate topic chats prepared automatically after your one-time request when the client supports it.
- Smaller per-chat context: a short core, only the procedure needed now, selected progress rows and one topic card.
- Nine private progress files created in `courses/current/` during setup. Back up that folder privately to move to another computer; downloading the public template alone does not restore your progress.
- A [fictional sample course](examples/demo-course/README.md), [lesson examples](examples/README.md), and a [quality report](docs/QA.md).

Voice is optional and depends on the client. Text practice remains useful, but listening and spoken pronunciation cannot be certified from typed answers. Without suitable audio, the tutor records those skills as unassessed and continues available practice.

## How review works

At the end of a lesson, the tutor runs a final check, saves the result and clearly says either “Topic complete — ready to move on” or “We will continue this topic here”. A later review can still be needed. Unassessed oral skills are stated separately; finishing text practice does not complete the whole topic.

With your recorded request for automatic topic chats, the tutor creates the next topic's chat in the same local project folder and gives you its real destination. It waits for you to write `Let's start`; it does not run more lessons in the background. No separate management chat is needed. If the topic needs more practice, it stays in its existing chat.

Weak topics return through `REVIEW_QUEUE.md`. The tutor points to the existing topic chat, or prepares it if missing and creation is available. Several weak topics can use `DE-R01 — Mixed review`. If chat tools are unavailable, the fallback is one exact title and one starter command; the course remains usable with any file-capable client.

## Find your way

| File or folder | Purpose |
| --- | --- |
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | The single entry point; it loads small procedure modules only when needed |
| [curriculum/](curriculum/README.md) | Transferable level goals and topic crosswalks |
| [routes/german/](routes/german/README.md) | Complete German A1–B1 topic cards |
| [templates/state/](templates/state/README.md) | Clean progress templates |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | File ownership and course portability |
| [docs/PEDAGOGY.md](docs/PEDAGOGY.md) | Teaching rationale |
| [docs/PRIVACY.md](docs/PRIVACY.md) | Keep learner data out of the public repository |
| [docs/SOURCES.md](docs/SOURCES.md) | Official references and what they support |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | Improve or adapt the template |

This is an independently authored learning aid, not an official course, certification, replacement for a teacher, or guarantee of B1. Its curriculum uses CEFR descriptors as references; it has not undergone external expert alignment or learner validation. See [limitations](docs/LIMITATIONS.md). The material is released under the [MIT License](LICENSE); linked third-party materials retain their own rights.
