# Fictional setup walkthrough

The learner types `Set up my language course` in a fresh folder. The agent reads the adapter, INSTRUCTIONS and templates, creates missing private files and sends one questionnaire:

```text
Ответьте одним сообщением. Можно написать «не знаю» или пропустить необязательный пункт.

1. На каком языке вам удобнее получать объяснения?
2. Какой язык вы хотите изучать?
3. Что уже умеете и как примерно оцениваете свой уровень?
4. Для чего нужен язык и в какой стране или ситуации?
5. Сколько минут и дней в неделю реально заниматься?
6. Какие интересы или сферу работы использовать в примерах?
7. Что сейчас важнее: разговор, аудирование, экзамен, работа или бытовое общение?
8. Как вести темы: отдельные чаты автоматически, отдельные чаты вручную или один общий чат?
```

The learner replies once: “1. Русский. 2. Немецкий. 3. Могу представиться и немного рассказать о дне, примерно A1. 4. Для жизни в Австрии и общения на работе. 5. По 20 минут три раза в неделю. 6. Программирование и прогулки. 7. Разговор. 8. Создавай отдельный чат для каждой темы автоматически.” The tutor maps and saves all supplied answers together. Optional omissions remain unknown; only a missing or ambiguous target language triggers a compact follow-up.

The tutor saves setup_stage diagnostic and gives one task: “Stell dich bitte kurz vor.” It waits for an attempt. It does not display a German model introduction first. If the learner cannot answer, it teaches a short phrase after that attempt and records the support.

A successful introduction permits a routine sample. A past-event sample is offered only if appropriate; difficulty stops escalation. A short reading notice and a written reply are separate observations. In a text-only session the tutor records listening/spoken_output not_assessed and does not claim pronunciation or global A1 mastery.

The answer to item 8 is recorded in PROFILE as auto_topics with the actual request; no repeat consent is needed before each topic. If item 8 was omitted, manual_topics is used without adding another setup question.

At completion it creates A001 with actual observations, selects a provisional route, populates TOPICS with all German codes (untested ones not_started), and verifies the save. In authorized auto mode it prepares `DE-A1-01 — Meeting people`, records the returned destination in PLAN and gives the real chat link/card if available: “Курс настроен. Откройте подготовленный чат и напишите «Начнём».” If creation is unavailable, it gives that exact title plus `Start topic DE-A1-01` for manual use. The new chat waits; setup does not count as a lesson or cause further chat creation.

If the learner stops before replying to the questionnaire, the next model reads PROFILE and shows the same unanswered form. If a reply was saved but the target language was unclear, it asks only for that item; it does not repeat the full setup or run an invented diagnostic. If this is only a walkthrough, as here, no personal files are created and no fictional results are saved.
