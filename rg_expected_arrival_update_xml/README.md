# Purchase expected arrival update

Improve **Late Receipts** information by keeping the Purchase Order **Expected Arrival**
aligned with the earliest order line that still has an open receipt or backorder.

Also keeps the **Scheduled Date** of open stock moves in sync when a Purchase Order Line
Expected Arrival is changed (standard Odoo only updates the Deadline).

## Behaviours

### Automatic

1. **After receipt Done / Cancel**  
   Refreshes the PO Expected Arrival from still-open lines.

2. **When a PO Line Expected Arrival is created or changed**  
   - Updates the Scheduled Date (`date`) of related open stock moves.  
   - Refreshes the PO Expected Arrival from still-open lines.  
   This covers both the forum request  
   (https://odoothinking.odoo.com/forum/keep-it-standard-1/update-scheduled-dates-based-on-purchase-expected-arrival-49)  
   and the open question about manual changes on purchase order lines.

### Manual

Select completed or cancelled receipts → **Actions > Update Expected Arrival**.

## Safe behaviour

- Never changes order-line dates.
- Only writes stock moves that are not Done or Cancelled.
- When no open line remains, leaves the current Expected Arrival unchanged.
- Writes only when the value actually differs (avoids unnecessary history).

## Installation (pure data / XML module)

1. Enable Developer Mode.
2. Go to **Apps → Import Module**.
3. Upload the ZIP.

Can also be installed/uninstalled as a regular filesystem addon.

## Dependencies

- `purchase_stock`
- `base_automation`

## Version

19.0.3.4.0

## Important limitation (standard Odoo)

`purchase.order.date_planned` is a stored computed field that always takes the
minimum of every order line that still has a date (including fully received lines).
This module corrects the header after the relevant events, but a later line write
can re-trigger the standard compute.

## Technical notes

- Pure data module – no Python files → fully compatible with Odoo Online / Import Module.
- Two independent automations so each trigger stays focused and safe.
