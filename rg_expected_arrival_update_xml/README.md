# Purchase expected arrival update

Keep **Late Receipts** accurate by aligning the Purchase Order **Expected Arrival** with the earliest still-open order line, and automatically sync the **Scheduled Date** of open receipts when a line date changes.

## Automatic

- After an incoming receipt is completed or cancelled → Expected Arrival is refreshed from open lines.
- When a Purchase Order Line Expected Arrival is created or changed → open stock moves receive the new Scheduled Date and the PO header is corrected.

## Manual

Select completed or cancelled receipts → **Actions → Update Expected Arrival**.

This action is also recommended to correct the PO Expected Arrival after manual changes on order lines, as Odoo always recalculates it as the minimum of every line (including fully received ones).  
→ Run the action to update the Expected Arrival to the next open expected arrival date.

## Safe by design

- Never modifies order-line dates  
- Only updates open (not done/cancelled) moves  
- Writes only when the value actually changes  

## Installation

Pure data module – fully compatible with **Odoo Online**.  
Apps → Import Module → upload the ZIP.

**Dependencies:** `purchase_stock`, `base_automation`  
**Version:** 19.0.3.4.0
