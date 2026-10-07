# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo.tests import common


class TestPurchasePortalDebranding(common.TransactionCase):
    def _modal(self, xmlid):
        arch = self.env.ref(xmlid).get_combined_arch()
        modal = etree.fromstring(arch).xpath(
            "//div[@id='portal_connect_software_modal']"
        )
        self.assertEqual(len(modal), 1)
        return etree.tostring(modal[0], encoding="unicode")

    def test_modal_debranded(self):
        for xmlid in (
            "purchase.portal_my_purchase_order",
            # primary view that inherits the purchase order page
            "purchase.portal_my_purchase_order_update_date",
        ):
            modal = self._modal(xmlid)
            self.assertNotIn("Odoo", modal, xmlid)
            self.assertNotIn("odoo.com", modal, xmlid)
            # The REST URL to download the document is kept
            self.assertIn("download_edi", modal, xmlid)
            self.assertIn("Want to import this document?", modal, xmlid)
