# Sales auto warehouse allocation

Confirm & auto allocate sales deliveries across warehouses by stock availability.

- Uses each warehouse's available stock and standard delivery route.
- Supports partial availability; any shortage remains with the first warehouse
  for Odoo's normal backorder flow.
- Keeps warehouse deliveries clear for logistics while the customer sees one
  clean product line in the PDF and portal preview.
- Services and manually routed lines are left unchanged.

The regular **Confirm** button remains available. Website orders confirmed by
Odoo's checkout/payment flow are allocated automatically before deliveries are
created.

The module uses Odoo's standard confirmation, procurement, reservation and
backorder processes after allocation.

## Installation (pure data module/XML solution)

Enable Developer Mode → Apps → **Import Module** → upload the module ZIP.
Can also be installed and uninstalled as a regular filesystem addon.
