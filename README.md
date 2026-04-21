# FinAssist

> Full-stack personal expense tracker with receipt OCR and AI-powered automatic categorization.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)

## About the project

FinAssist is a web application that helps users track their personal expenses without the friction of typing everything manually. Users take a picture of a receipt, an OCR pipeline extracts the items and total amount, and an LLM automatically categorizes the expense and generates monthly insights (e.g. "you spent 32% more on food than last month").

This is my first full-stack portfolio project, built to consolidate my Python skills and learn modern web development end-to-end: REST APIs, authentication, databases, frontend, testing, Docker and cloud deployment.

## Tech stack (planned)

| Layer       | Technology                              |
|-------------|-----------------------------------------|
| Backend     | FastAPI (Python 3.12+)                  |
| Database    | PostgreSQL + SQLModel + Alembic         |
| Frontend    | Next.js 15 + TypeScript + Tailwind CSS  |
| Auth        | JWT (python-jose + passlib/bcrypt)      |
| AI          | OpenAI API (structured outputs)         |
| OCR         | Tesseract (with Google Vision fallback) |
| Testing     | pytest, pytest-asyncio, httpx           |
| DevOps      | Docker, GitHub Actions                  |
| Deployment  | Vercel (frontend) + Railway/Render (backend) + Neon (DB) |

> This stack may evolve as the project grows.

## Roadmap

- [ ] **Phase 1** — Prerequisites and foundations
- [ ] **Phase 2** — Project setup (monorepo, Docker, tooling)
- [ ] **Phase 3** — Backend: models and CRUD endpoints
- [ ] **Phase 4** — Database and JWT authentication
- [ ] **Phase 5** — Frontend and full integration (OCR + AI)
- [ ] **Phase 6** — Testing and code quality
- [ ] **Phase 7** — Deployment (CI/CD + cloud)
- [ ] **Phase 8** — Final polish (docs, demo video, blog post)

## Status

🚧 Currently in **Phase 1 — Foundations**. This README will grow as the project advances.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

Built by [Christian Gonzalez](https://github.com/nullbyte4) as a portfolio project.
