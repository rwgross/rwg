{
    "name": "Purchase expected arrival update",
    "version": "19.0.3.3.3",
    "category": "Purchases",
    "summary": "Keep Late Receipts focused on the next open arrival",
    "description": """
Improve Late Receipts informations by updating Expected Arrival with the
earliest order line that still has an open receipt or backorder.

Updates run automatically when an incoming receipt is completed or cancelled.
Users can also run Update Expected Arrival manually from selected receipts.

Safe behavior: order-line dates remain unchanged. When no open receipt or
backorder remains, the current Expected Arrival is preserved.

Installation (pure data module/XML solution):
Enable Developer Mode, open Apps, select Import Module, and upload the module ZIP.
Can also be installed and uninstalled as a regular filesystem addon.
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
