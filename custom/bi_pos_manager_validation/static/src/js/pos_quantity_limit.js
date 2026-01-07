/** @odoo-module */

import { Order, Orderline } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

const MAX_QUANTITY = 9;

// Patch the Orderline model
patch(Orderline.prototype, {
    set_quantity(quantity, keep_price) {
        const parsedQty = parseFloat(quantity) || 0;
        const currentQty = this.get_quantity();
        
        // Always allow decrease in quantity (including removal/negative)
        if (parsedQty <= currentQty) {
            return super.set_quantity(...arguments);
        }
        
        // Check if new quantity exceeds limit when increasing
        if (parsedQty > MAX_QUANTITY) {
            // Show popup
            if (this.env.services.dialog) {
                this.env.services.dialog.add(AlertDialog, {
                    title: _t('Quantity Limit Exceeded'),
                    body: _t('Maximum quantity allowed per line is ' + MAX_QUANTITY + '. Please add a new line for additional quantity.'),
                });
            }
            // Keep the current quantity
            return;
        }
        
        // Quantity is within limit, allow the change
        return super.set_quantity(...arguments);
    },
    
    can_be_merged_with(orderline) {
        // Don't merge if it would exceed the limit
        if (super.can_be_merged_with(orderline)) {
            const totalQty = this.get_quantity() + orderline.get_quantity();
            if (totalQty > MAX_QUANTITY) {
                return false;
            }
            return true;
        }
        return false;
    }
});

// Patch the Order model to handle product addition
patch(Order.prototype, {
    add_product(product, options) {
        options = options || {};
        const qtyToAdd = options.quantity !== undefined ? options.quantity : 1;
        
        // If adding a small quantity, try normal flow first
        if (qtyToAdd <= MAX_QUANTITY) {
            // Check if there's an existing line with space
            const existingLines = this.get_orderlines().filter(
                line => line.product.id === product.id && 
                        line.get_quantity() < MAX_QUANTITY &&
                        JSON.stringify(line.get_discount()) === JSON.stringify(options.discount || 0)
            );
            
            if (existingLines.length > 0 && options.merge !== false) {
                const lastLine = existingLines[existingLines.length - 1];
                const currentQty = lastLine.get_quantity();
                const availableSpace = MAX_QUANTITY - currentQty;
                
                if (qtyToAdd <= availableSpace) {
                    // Fits in existing line
                    return super.add_product(product, options);
                } else {
                    // Fill the existing line first
                    if (availableSpace > 0) {
                        super.add_product(product, {...options, quantity: availableSpace});
                    }
                    // Create new line for remainder
                    const remainder = qtyToAdd - availableSpace;
                    return super.add_product(product, {...options, quantity: remainder, merge: false});
                }
            }
            
            // No existing line with space, create new line
            return super.add_product(product, {...options, merge: false});
        }
        
        // Quantity exceeds MAX_QUANTITY, need to split
        let remainingQty = qtyToAdd;
        
        // Try to fill an existing line first
        const existingLines = this.get_orderlines().filter(
            line => line.product.id === product.id && 
                    line.get_quantity() < MAX_QUANTITY &&
                    JSON.stringify(line.get_discount()) === JSON.stringify(options.discount || 0)
        );
        
        if (existingLines.length > 0) {
            const lastLine = existingLines[existingLines.length - 1];
            const currentQty = lastLine.get_quantity();
            const availableSpace = MAX_QUANTITY - currentQty;
            
            if (availableSpace > 0) {
                const fillQty = Math.min(remainingQty, availableSpace);
                super.add_product(product, {...options, quantity: fillQty});
                remainingQty -= fillQty;
            }
        }
        
        // Create new lines for remaining quantity
        while (remainingQty > 0) {
            const lineQty = Math.min(remainingQty, MAX_QUANTITY);
            super.add_product(product, {...options, quantity: lineQty, merge: false});
            remainingQty -= lineQty;
        }
    }
});
// Features:
//         - Maximum 9 units per order line
//         - Automatic line splitting for excess quantities
//         - Popup notification when limit exceeded
//         - Full line removal functionality
//         - Negative quantity support for corrections