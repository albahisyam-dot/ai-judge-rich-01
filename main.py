"""Write a fixed, deterministic bounty plan to the grader's output directory."""

import os
from pathlib import Path

PLAN = (
    "Reserve $75; cap tools/fees at $25 and risk at $5/day. Days 1-7: find Shopify/Etsy "
    "shops with 25-100 SKUs. On marketplaces permitting AI work, offer a $15 audit of 25 "
    "listings or $45 cleanup of 100, returning a corrected CSV and change log in 24 hours. "
    "Show 3 sample rows from public listings. Send 15 tailored proposals daily within platform "
    "limits; aim for 2 paid pilots. Verify edits and request honest reviews. Days 8-21: keep "
    "offers with paid conversions; after 3 reviews, charge $55/100 listings and target 3 "
    "weekly orders. Reinvest at most 20% of receipts. Make a $9 listing-quality checklist "
    "from general methods, never client data, and list it on a permitted digital marketplace. "
    "Days 22-30: devote 80% of time to the best net/hour offer, finish orders and withdraw "
    "available cash. Track leads, sales, hours, fees and net daily. If no sale by day 7, switch "
    "once to product-description cleanup; buy no ads. Stop channels with fees above 10%. "
    "No debt, spam, guarantees or speculation."
)

if not PLAN.strip() or len(PLAN) > 1_000:
    raise ValueError("Plan must contain 1-1,000 non-whitespace characters")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))
