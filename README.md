# FinAssist

> Personal finance tracker for income and expenses with receipt OCR and AI-powered categorization.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

## About the project

FinAssist is a web application designed to track personal finances—both earnings (salary, extra income) and expenses—without the hassle of manual data entry. Users can log their income, upload pictures of purchase receipts, and let AI extract key details (store name, items, total, date) and automatically assign a category. A clean monthly dashboard provides an instant overview of total income, spending by category, and savings.

This is my **first software engineering project**, built with a primary focus: **to learn and master Python fundamentals** while building a complete, real-world application from scratch.

To keep the learning curve manageable and avoid cognitive overload, the stack avoids complex JavaScript frameworks. Everything runs on Python, using clean HTML templates and lightweight styling so effort remains 100% focused on backend architecture, database modeling, and software engineering best practices.

## Tech stack

| Layer | Technology | Rationale |
|---|---|---|
| **Language** | Python 3.12+ | Core learning objective and foundation of the project |
| **Backend & Web** | FastAPI | Modern, fast, intuitive Python web framework with automatic OpenAPI docs |
| **Templates & UI** | Jinja2 + Tailwind CSS (CDN) | Clean web interface rendered directly with Python—no Node.js/JS build toolchain |
| **Database** | SQLite + SQLModel | Zero-configuration file database combining Pydantic validation with SQLAlchemy |
| **AI & OCR** | OpenAI API (Vision & Structured Outputs) | Multimodal model to read receipt images and return structured financial data |
| **Testing** | pytest | Industry-standard Python testing tool to ensure correctness |
| **Deployment** | Render | Simple cloud hosting for Python web applications |

## Project skills

Local Copilot skills configured in `.agents/skills/`:

- `best-practices` — Clean code standards, meaningful naming, disciplined function design, robust error handling, secure secrets management, and test quality.
- `devlog-logging` — Running development log and session tracking in `DEVLOG.md`.
- `direct-mode` — Plan-first execution workflow with handoff review before Git operations.
- `git-workflow` — Feature branch workflow, local merges, and strict prohibition of AI commit co-author attribution.
- `mainframe-wiki` — Cross-project consultation of the personal knowledge base (`themainframe`).
- `mentor-mode` — Guided learning workflow where Christian writes the code and Copilot reviews.
- `new-project-kickoff` — Phase 0 context and planning framework with roadmap tracking.

## Roadmap

- [x] **Phase 0 — Project Setup & Environment**
  - Set up Python virtual environment (`venv`) and package dependencies (`fastapi`, `uvicorn`, `sqlmodel`, `jinja2`, `ruff`, `pytest`)
  - Create project folder structure (`app/`, `templates/`, `static/`, `tests/`)
  - Build minimal FastAPI app with a `GET /health` endpoint and initial home template
  - Configure `.env.example` and verify `.gitignore`

- [x] **Phase 1 — Data Models & Database**
  - Design SQLModel entities: `Income`, `Expense`, and `Category`
  - Initialize local SQLite database and connection session management
  - Write unit tests in `pytest` verifying database CRUD operations

- [ ] **Phase 2 — Manual Tracking Web UI**
  - Build web pages to record income (e.g., salary, freelance) and view income history
  - Build form to manually log an expense with category selection
  - List transactions with basic filtering by month

- [ ] **Phase 3 — Receipt OCR & AI Extraction**
  - Create a standalone Python module to process receipt images via OpenAI Vision API
  - Extract structured JSON (merchant, date, total amount, suggested category)
  - Write test cases with sample receipts to validate accuracy and error handling

- [ ] **Phase 4 — End-to-End Expense Flow**
  - Add receipt upload component in the web interface
  - Display extracted receipt data in a confirmation form before saving
  - Save confirmed expense to the database linked to its image/record

- [ ] **Phase 5 — Monthly Dashboard & Insights**
  - Calculate monthly summary: Total Income, Total Expenses, Net Savings
  - Display expense distribution by category
  - Simple comparison against previous month (e.g., spending trends)

- [ ] **Phase 6 — Testing & Refactoring**
  - Review test coverage across routes and services
  - Refactor code for clarity, error handling, and type safety

- [ ] **Phase 7 — Cloud Deployment**
  - Prepare production configuration (`render.yaml` or Procfile, requirements lock)
  - Configure persistent storage for SQLite/receipt images
  - Deploy to Render and verify live health and functionality

## Future improvements (v2)

Planned enhancements once the core application is running smoothly:

- User authentication & multi-user support (JWT / session auth)
- Budgeting goals and spending alert limits
- Data export (CSV / PDF monthly reports)
- Dedicated modern frontend (Next.js / React) after mastering Python fundamentals
- Migration from SQLite to PostgreSQL

## Status

🚧 Currently in **Phase 2 — Manual Tracking Web UI**.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

Built by [Christian Gonzalez](https://github.com/nullbyte4) as a portfolio and software engineering learning project.
