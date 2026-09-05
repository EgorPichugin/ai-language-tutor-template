# Quick start / Быстрый старт

## 1. Open the folder / Откройте папку

Download ZIP, extract it, and open the folder that contains this file in your existing Codex or Claude Code client. On Windows, open the extracted folder, not the ZIP. Use a local project that can read and edit files. Allow normal project access when your client asks. Do not disable its security settings.

Скачайте ZIP, распакуйте и откройте папку с этим файлом в уже настроенном AI-клиенте. Используйте одну и ту же локальную папку для всех занятий. Отдельные рабочие копии проекта могут иметь другой прогресс.

## 2. Set up / Настройте курс

Write either command:

```text
Set up my language course
```

```text
Настрой мой языковой курс
```

The tutor asks one question at a time: native language, target language, approximate level, goal, available time, interests/work, and priorities. Unknown answers are fine. The default complete example is German; another language needs an explicitly provisional adapted route.

Преподаватель задаёт вопросы по одному. Можно ответить «не знаю» или пропустить личные сведения. Затем он предложит диагностику примерно на 10–15 минут и сохранит ваш маршрут. Проверка аудирования возможна только при доступном звуке.

If your client can create chats, the tutor asks once whether to create a separate chat for each topic in this same local project folder, unless you already requested that. You can also say: `Create a separate chat for each topic in this same local project folder` / `Создавай отдельный чат для каждой темы в этой же локальной папке проекта`. The choice is remembered for the course.

After the nine files are saved, the tutor prepares your first topic chat or gives the manual fallback below. Your native language controls explanations; the English command does not lock the course into English.

Если вы уже попросили отдельные чаты, AI не спрашивает разрешение заново перед каждой темой. После настройки он готовит первый чат и показывает, куда перейти. Откройте его и напишите `Начнём`.

## 3. Continue / Продолжайте

| English command | Русская команда | Result / Результат |
| --- | --- | --- |
| `Let's start` / `Continue` | `Начнём` / `Дальше` | Begin the prepared lesson or resume the current topic |
| `Start my next lesson` | `Начни следующее занятие` | Follow your route and due reviews |
| `Start a 20-minute lesson` | `Начни занятие на 20 минут` | One smaller practical goal |
| `Review this topic for 15 minutes` | `Повтори эту тему за 15 минут` | Use the chat's topic; ask for its code if unknown |
| `Start a mixed review` | `Начни смешанное повторение` | Work on up to three weak topics |
| `Check my progress` | `Проверь мой прогресс` | Evidence summary; offer a short assessment if needed |
| `I am back after a break` | `Я вернулся после перерыва` | Gentle return and fresh sampling |
| `Finish and save this lesson` | `Заверши и сохрани занятие` | Save observed results, even if partial |

You do not need to decide when a topic is done. The tutor ends the lesson after a final check, saves the result, and clearly says whether to move on or keep practising this topic. With automatic topic chats enabled and supported, it prepares one next destination and gives you the real link/card when available. Open it and write `Let's start`. The new chat waits for you; it cannot complete another lesson or create a chain of chats by itself.

AI сам сообщает, когда тема завершена. Если нужно продолжение — остаётесь в этом чате. Если можно двигаться дальше — открываете подготовленный чат следующей темы. «Тема завершена» не означает, что повторение больше никогда не потребуется. При непроверенной устной части AI называет этот пробел явно.

There is no required management chat. `Start my next lesson` works from any course chat. A due review/checkpoint can come before a new topic; the tutor explains the next action. Stop early with `Finish and save this lesson`; an unfinished final check does not count as topic completion.

## Manual fallback / Если создание чатов недоступно

The tutor gives one exact title and one starter command. Create/open that chat in this same local project folder. Example title:

```text
DE-A1-01 — Meeting people
```

Starter command: `Start topic DE-A1-01`. It identifies the topic even when the model cannot see the chat title. For a review use the code-specific command the tutor gives, such as `Review topic DE-A2-03 for 15 minutes`. If you explicitly prefer one chat, say so; the completion messages and saved progress work there too.

## If the tutor does not start / Если запуск не сработал

Paste this explicit fallback:

```text
Read INSTRUCTIONS.md in this folder. Follow its startup procedure.
Read courses/current/ if it exists. Set up my language course if it does not.
Otherwise start my next lesson. Ask one question at a time.
```

```text
Прочитай INSTRUCTIONS.md в этой папке и выполни процедуру запуска.
Если есть courses/current/, прочитай мой прогресс и начни следующее занятие.
Если папки нет, настрой курс. Задавай по одному вопросу.
```

If the client cannot edit files, it must say progress is **not saved** and give complete updated Markdown files for you to save manually. Without either file writing or manual saving, progress will not persist. If it cannot read files, provide INSTRUCTIONS.md, your nine course files, the route overview and current topic/dependency cards manually; for a fresh setup provide the nine clean templates and selected route files too. The tutor should name missing files rather than invent their contents. This fallback is less convenient.

Если файлы не сохраняются, попросите клиента показать причину. Можно сохранить подготовленные файлы вручную. Не рассчитывайте на память другого чата. Не запускайте два занятия с записью прогресса одновременно.

## Try the demo safely / Посмотрите пример

Read [the fictional demo](examples/demo-course/README.md). It is documentation, never your active course. To rehearse without touching personal state, ask: `Simulate the next lesson using examples/demo-course, without changing any files`.
