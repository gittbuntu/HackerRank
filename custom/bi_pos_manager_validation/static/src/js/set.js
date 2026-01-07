/** @odoo-module */

import { Orderline } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

const maximum = 9;

patch(Orderline.prototype, {
  set_quantity(quantity) {
    const qty = parseFloat(quantity) || 1;
    const presentqty = this.get_quantity();

    if (qty <= presentqty) {
      return super.set_quantity(...arguments);
    }

    if (qty > maximum) {
      // Alert
      if (this.env.services.dialog) {
        this.env.services.dialog.add(AlertDialog, {
          title: _t("Quantity Exceeded"),
          body: _t(
            "Double digit not allowed" + presentqty + ". Please select product again."
          ),
        });
      }
      return;
    }

    return super.set_quantity(...arguments);
  },
});
