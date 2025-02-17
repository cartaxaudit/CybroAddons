# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Hafeesul Ali(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    "name": "POS Invoice Register Payment",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Create payment and register payment for invoice in pos",
    "description": "This module will help you create payments in customer list"
    "and register payment for invoices in pos",
    "author": "Cybrosys Techno Solutions",
    "company": "Cybrosys Techno Solutions",
    "maintainer": "Cybrosys Techno Solutions",
    "website": "https://www.cybrosys.com",
    "depends": ["base", "point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "pos_invoice_payment/static/src/js/pos_partnerline.js",
            "pos_invoice_payment/static/src/js/invoicing_button.js",
            "pos_invoice_payment/static/src/js/payment_popup.js",
            "pos_invoice_payment/static/src/js/invoicing_screen.js",
            "pos_invoice_payment/static/src/xml/partnerline_button_templates.xml",
            "pos_invoice_payment/static/src/xml/payment_pop_templates.xml",
            "pos_invoice_payment/static/src/xml/numpad_invoicing_button_templates.xml",
            "pos_invoice_payment/static/src/xml/invoice_screen_templates.xml",
            "pos_invoice_payment/static/src/css/invoice_list.scss",
        ]
    },
    "images": ["static/description/banner.jpg"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
