# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Portal Debranding",
    "summary": "Remove the Odoo references of the 'Connect with your software' "
    "dialog of the purchase portal",
    "version": "20.0.1.0.0",
    "category": "Hidden",
    "website": "https://github.com/OCA/server-brand",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "purchase",
    ],
    "data": [
        "views/purchase_portal_templates.xml",
    ],
}
