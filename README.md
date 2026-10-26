# CashFlow AI

AI-powered cash-flow and credit-risk forecasting for small businesses.
Research prototype · end-to-end (frontend + backend + ML + Docker).

## Quick start
1. Copy `.env.example` to `.env`.
2. Place `Online Retail.xlsx` at `data/raw/`.
3. `docker compose up --build` → backend at :8000, frontend at :5173.
4. Run pipeline: `python -m scripts.run_uci_pipeline --business-id UCI-DEMO --opening 10000`.

See `docs/` for design, data dictionary, and research protocol.