# Purchase expected arrival update

Improve **Late Receipts** informations by updating **Expected Arrival** with the
earliest order line that still has an open receipt or backorder.

## Updates

- **Automatic:** refreshes after an incoming receipt is completed or cancelled.
- **Manual:** select completed or cancelled receipts and run **Actions > Update
  Expected Arrival**.

## Safe behavior

The module updates only the purchase order's **Expected Arrival**. Order-line
dates remain unchanged. When no open receipt or backorder remains, the current
Expected Arrival is preserved.

## Installation (pure data module/XML solution)

- Enable Developer Mode, open **Apps**, select **Import Module**, and upload the
  module ZIP.

Can also be installed and uninstalled as a regular filesystem addon.
