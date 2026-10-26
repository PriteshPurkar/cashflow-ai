"""
Run the UCI cleaning + daily aggregation pipeline.

Usage:
    python -m scripts.run_uci_pipeline --business-id UCI-DEMO --opening 10000
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from ml.data_validation.uci_loader import load_raw, schema_report
from ml.data_validation.clean_uci import clean
from ml.data_validation.aggregate_daily import aggregate_daily

PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--business-id", default="UCI-DEMO")
    ap.add_argument("--opening", type=float, default=10_000.0)
    args = ap.parse_args()

    print(">> Loading UCI raw...")
    raw = load_raw()
    print(json.dumps(schema_report(raw), indent=2, default=str))

    print(">> Cleaning...")
    cleaned, quality = clean(raw, business_id=args.business_id)
    print(json.dumps(quality, indent=2, default=str))

    print(">> Aggregating daily cash position...")
    daily = aggregate_daily(cleaned, assumed_opening_balance=args.opening)

    # Reconciliation check
    for _, r in daily.iterrows():
        expected = r["opening_balance"] + r["inflows"] - r["outflows"]
        assert abs(expected - r["closing_balance"]) < 1e-6, (
            f"Reconciliation failed on {r['date']}"
        )

    tx_path = PROCESSED / "transactions.csv"
    daily_path = PROCESSED / "daily_cash_position.csv"
    quality_path = PROCESSED / "quality_report.json"

    cleaned.to_csv(tx_path, index=False)
    daily.to_csv(daily_path, index=False)
    quality_path.write_text(json.dumps(
        {"uci_schema": schema_report(raw), "cleaning": quality},
        indent=2, default=str,
    ))

    print(f">> Wrote {tx_path} ({len(cleaned)} rows)")
    print(f">> Wrote {daily_path} ({len(daily)} rows)")
    print(f">> Wrote {quality_path}")
    print(">> Reconciliation: OK")


if __name__ == "__main__":
    main()