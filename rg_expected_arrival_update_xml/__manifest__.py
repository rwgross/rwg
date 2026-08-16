{
    "name": "Purchase expected arrival update",
    "version": "19.0.3.4.0",
    "category": "Purchases",
    "summary": "Keep Late Receipts focused on the next open arrival + sync Scheduled Date from line",
    "description": """
Improve Late Receipts information by keeping Purchase Order Expected Arrival
aligned with the earliest still-open order line (open receipt or backorder).

Also keeps the Scheduled Date of open stock moves in sync when a Purchase
Order Line Expected Arrival is changed (standard only updates the Deadline).

Automatic behaviours:
- After an incoming receipt is completed or cancelled → refresh PO Expected Arrival
  from open lines.
- When a PO Line Expected Arrival is created or changed → update open moves'
  Scheduled Date and refresh the PO header from open lines.

Manual action:
- Select completed/cancelled receipts → Actions > Update Expected Arrival

Safe behaviour:
- Never changes order-line dates.
- Only writes open (not done/cancel) stock moves.
- When no open line remains, leaves the current Expected Arrival unchanged.

Installation (pure data / XML module):
Enable Developer Mode → Apps → Import Module → upload the ZIP.
Can also be installed as a regular filesystem addon.

Limitation (standard Odoo behaviour):
purchase.order.date_planned is a stored computed field that always takes the
minimum of every line that still has a date (including fully received lines).
This module corrects the header after the relevant events, but a later line
write can re-trigger the standard compute.
    """,
    "author": "RGross",
    "website": "https://git.rgross.ch/RGross/Odoo19/src/branch/main/rg_expected_arrival_update_xml",
    "license": "LGPL-3",
    "depends": ["purchase_stock", "base_automation"],
    "data": [
        "data/purchase_expected_arrival_actions.xml",
    ],
    "installable": True,
    "application": False,
}
