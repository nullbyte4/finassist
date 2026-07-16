# FinAssist

> Expense tracker with receipt OCR and AI-powered automatic categorization.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)

## About the project

FinAssist is a web application that helps users track their personal expenses without the friction of typing everything manually. Users take a picture of a receipt, an OCR service extracts the items and total amount, and an LLM automatically categorizes the expense and generates simple monthly insights (e.g. "you spent 32% more on food than last month").

This is my **first full-stack project**, built to consolidate my Python skills and learn modern web development end-to-end: REST APIs, authentication, databases, frontend, and deployment.

The stack was deliberately kept small on purpose: the goal of v1 is to ship a complete, working product with a limited set of new tools, rather than to learn every tool at once. More advanced tooling (TypeScript, Docker, CI/CD, PostgreSQL) is planned as a v2 once the fundamentals are solid — see [Roadmap](#roadmap) and [Future improvements](#future-improvements-v2).

## Tech stack

| Layer       | Technology                              |
|-------------|------------------------------------------|
| Backend     | FastAPI (Python 3.12+)                  |
| Database    | SQLite + SQLModel                       |
| Frontend    | Next.js 15 + JavaScript + Tailwind CSS  |
| Auth        | JWT (basic login/register, no refresh tokens yet) |
| AI          | OpenAI API (categorization + insights)  |
| OCR         | Google Vision API (or OpenAI Vision)    |
| Testing     | pytest                                  |
| Deployment  | Vercel (frontend) + Render (backend)    |

> This stack is intentionally minimal for a first project. See [Future improvements](#future-improvements-v2) for what's planned once v1 is done.

## Roadmap

- [ ] **Phase 0** — Project setup: monorepo folder structure, Python virtual environment, base dependencies, minimal FastAPI app with a `/health` endpoint, environment variables config, Git repo initialized and pushed
- [ ] **Phase 1** — Backend: FinAssist models (expenses, categories, users) + CRUD endpoints, with basic pytest tests per endpoint
- [ ] **Phase 2** — Basic authentication (register/login with JWT), with tests for the auth flow
- [ ] **Phase 3** — OCR integration: upload a photo → extracted text (tested standalone before touching the frontend)
- [ ] **Phase 4** — AI integration: extracted text → structured categorization (JSON)
- [ ] **Phase 5** — Frontend (Next.js + JS): login, upload receipt, view list of expenses
- [ ] **Phase 6** — Simple dashboard with insights (totals per category, then month-over-month comparison)
- [ ] **Phase 7** — Testing pass: review overall coverage, fill gaps and add edge cases for critical endpoints
- [ ] **Phase 8** — Deployment (Vercel + Render)

## Future improvements (v2)

Once v1 is complete and working end-to-end, the plan is to gradually level up the stack:

- Migrate frontend from JavaScript to **TypeScript**
- Migrate database from **SQLite to PostgreSQL** (with Alembic migrations)
- Add **Docker** for local development and reproducible environments
- Add **CI/CD** with GitHub Actions
- Improve auth with refresh tokens
- Add a Tesseract fallback (or evaluate if it's actually worth the added complexity)

## Status

🚧 Currently in **Phase 0 — Project setup**. This README will grow as the project advances.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

Built by [Christian Gonzalez](https://github.com/nullbyte4) as a portfolio project.