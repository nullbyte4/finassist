# Session log

Short plans for each work session and what actually happened. Newest entry on top.
A session plan is sized to the time available — the goal is to *advance* the current phase, not necessarily finish it. Phases live in `README.md` (Roadmap); don't duplicate them here.

<!-- Template:

## YYYY-MM-DD — Phase X (time available)

**Goal:** one sentence, always verifiable.

**Prep (10-15 min before the session):**
- 2-3 things to skim (official docs, one concept) so the session's new terms sound familiar.

**Plan:**
- [ ] task
- [ ] task
- [ ] (stretch) optional task if time allows

**Done / Notes:** _(fill at end of session)_

**Next:** _(fill at end of session)_

-->

## 2026-07-16 — Phase 0 (1h)

**Goal:** Get a minimal FastAPI app running locally with a working `/health` endpoint.

**Prep (10-15 min before the session):**
- Skim FastAPI's "First Steps" tutorial: https://fastapi.tiangolo.com/tutorial/first-steps/ — just read it, don't code along.
- Read what uvicorn is and why FastAPI needs a separate server (search: "what is an ASGI server").
- If virtual environments are fuzzy: skim https://docs.python.org/3/library/venv.html (just the intro).

**Plan:**
- [ ] Create the monorepo folder structure (`backend/`, `frontend/` placeholder)
- [ ] Create the Python virtual environment and install base dependencies (`fastapi`, `uvicorn`, `ruff`)
- [ ] Write the minimal FastAPI app with a `GET /health` endpoint
- [ ] Run it with uvicorn and verify `/health` responds via the interactive `/docs`
- [ ] (stretch) Add `.env.example` and check `.gitignore` covers `.env` and the venv

**Done / Notes:** _(fill at end of session)_

**Next:** _(fill at end of session)_
