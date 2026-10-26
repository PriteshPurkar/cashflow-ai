# UCI Online Retail — Cleaning Pipeline

## Purpose
Train the transaction cleaning + daily aggregation pipeline on real-world
dirty data. This dataset supports pipeline correctness only — it does
NOT support claims about SME cash-flow forecasting performance, because
it has no invoices, due dates, payment dates, or expense categories.

## Dataset
- Source: UCI ML Repository, "Online Retail" (Chen, Sain, Guo).
- ~541,909 transaction rows, UK online retailer, Dec 2010–Dec 2011.
- Manually placed at `data/raw/Online Retail.xlsx`.

## Known issues handled
| Issue | Handling |
|-------|----------|
| Missing `CustomerID` (~135,080 rows) | Preserved as null; not invented |
| Duplicate rows (~5,268) | **Flagged**, not auto-deleted |
| `InvoiceNo` starting with 'C' | Tagged as cancellation → outflow/refund |
| Negative `Quantity` | Tagged as refund (outflow), retained |
| Non-positive `UnitPrice` or `Quantity` | Rejected with reason |
| Invalid `InvoiceDate` | Rejected with reason |
| No payment method column | Assumed `bank_transfer` (documented) |
| No bank account balance | Assumed opening balance, stated in run args |

## Outputs
- `data/processed/transactions.csv` — standardized records
- `data/processed/daily_cash_position.csv` — daily inflows/outflows/closing
- `data/processed/quality_report.json` — counts + reasons

## Honesty rules
- All accepted rows: `source=uci_online_retail`, `is_synthetic=false`.
- All rejected rows recorded with reasons.
- Daily reconciliation assertion runs on every row.
- **No model performance claims** may cite UCI-only results.