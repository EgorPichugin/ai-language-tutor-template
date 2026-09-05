# Fictional setup walkthrough

The learner types `Set up my language course` in a fresh folder. The agent reads the adapter, INSTRUCTIONS and templates, creates missing private files and begins. Each numbered line below is a separate conversational turn, followed by a wait; it is not one seven-question message.

1. Tutor: “Какой язык вам удобнее для объяснений?” Learner: “Русский.” Save the preference and next setup question.
2. Tutor: “Какой язык хотите изучать?” Learner: “Немецкий.”
3. Tutor: “Что уже можете сказать по-немецки?” Learner: “Представиться, немного рассказать о дне.”
4. Tutor: “Для какой цели нужен немецкий?” Learner: “Для жизни в Австрии и общения на работе.”
5. Tutor: “Сколько времени готовы выделять на занятия?” Learner: “По 20 минут три раза в неделю.”
6. Tutor: “Какие интересы и рабочую область использовать в примерах?” Learner: “Программирование и прогулки.”
7. Tutor: “Что сейчас важнее: разговор, аудирование, экзамен, работа или бытовое общение?” Learner: “Разговор.”

The tutor saves setup_stage diagnostic and gives one task: “Stell dich bitte kurz vor.” It waits for an attempt. It does not display a German model introduction first. If the learner cannot answer, it teaches a short phrase after that attempt and records the support.

A successful introduction permits a routine sample. A past-event sample is offered only if appropriate; difficulty stops escalation. A short reading notice and a written reply are separate observations. In a text-only session the tutor records listening/spoken_output not_assessed and does not claim pronunciation or global A1 mastery.

If chat creation is available and no earlier preference was given, the tutor asks once whether to create separate topic chats in this same local folder. A positive answer is recorded in PROFILE as auto_topics with the actual request; no repeat consent is needed before each topic.

At completion it creates A001 with actual observations, selects a provisional route, populates TOPICS with all German codes (untested ones not_started), and verifies the save. In authorized auto mode it prepares `DE-A1-01 — Meeting people`, records the returned destination in PLAN and gives the real chat link/card if available: “Курс настроен. Откройте подготовленный чат и напишите «Начнём».” If creation is unavailable, it gives that exact title plus `Start topic DE-A1-01` for manual use. The new chat waits; setup does not count as a lesson or cause further chat creation.

If the learner stops after question four, the next model reads PROFILE and asks the time question; it does not repeat setup or run an invented diagnostic. If this is only a walkthrough, as here, no personal files are created and no fictional results are saved.
