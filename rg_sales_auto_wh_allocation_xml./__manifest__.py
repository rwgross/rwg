{
    "name": "Sales auto warehouse allocation",
    "version": "19.0.1.6.0",
    "category": "Sales/Inventory",
    "summary": "Automatically allocate sales quantities across warehouse stock",
    "description": """
Automatically distribute storable sales quantities across the active company
warehouses in priority order before confirmation. The remaining shortage stays
with the first warehouse so standard Odoo backorders continue to work.

Warehouse-specific deliveries remain clear for logistics, while the customer
sees one clean commercial line in the sales PDF and portal preview.

The standard Confirm button remains available. Website checkout confirmations
are allocated automatically before deliveries are created.

Installation (pure data module/XML solution):
Enable Developer Mode, open Apps, select Import Module, and upload the module ZIP.
Can also be installed and uninstalled as a regular filesystem addon.
    """,
    "author": "RGross",
    "website": "https://git.rgross.ch/RGross/Odoo19/src/branch/main/rg_sales_auto_wh_allocation_xml",
    "license": "LGPL-3",
    "depends": ["sale_stock", "base_automation", "base_import_module"],
    "data": [
        "data/allocation_fields.xml",
        "data/warehouse_allocation.xml",
        "views/sale_order_views.xml",
        "views/sale_report.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
