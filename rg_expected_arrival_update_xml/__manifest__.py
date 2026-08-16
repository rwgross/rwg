{
    "name": "Purchase expected arrival update",
    "version": "19.0.3.5.0",
    "category": "Purchases",
    "summary": "Keep Late Receipts focused on the next open arrival + sync Scheduled Date from line",
    "description": """
Keep Late Receipts accurate by aligning the Purchase Order Expected Arrival
with the earliest still-open order line.

Also keeps the Scheduled Date of open stock moves in sync when a Purchase
Order Line Expected Arrival is changed (standard Odoo only updates the Deadline).

Automatic behaviours:
- After an incoming receipt is completed or cancelled → refresh PO Expected Arrival
  from open lines.
- When a PO Line Expected Arrival is created or changed → update open moves'
  Scheduled Date only.

Manual action:
Select completed or cancelled receipts → Actions → Update Expected Arrival.
This action is also recommended to correct the PO Expected Arrival after manual
changes on order lines, as Odoo always recalculates it as the minimum of every
line (including fully received ones).
→ Run the action to update the Expected Arrival to the next open expected arrival date.

Safe behaviour:
- Never changes order-line dates.
- Only writes open (not done/cancel) stock moves.
- Writes only when the value actually differs.

Installation (pure data / XML module):
Enable Developer Mode → Apps → Import Module → upload the ZIP.
Can also be installed as a regular filesystem addon.
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
