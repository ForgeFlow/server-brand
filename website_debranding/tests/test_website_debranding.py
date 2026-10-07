# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestWebsiteDebranding(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # The post_init_hook deactivates the view when tests are enabled
        cls.view = cls.env.ref("website_debranding.layout_footer_copyright")
        cls.view.active = True

    def _render_promotion(self):
        return self.env["ir.ui.view"]._render_template(
            "web.brand_promotion_message",
            values={"_message": "Create a free website", "_utm_medium": "website"},
        )

    def test_promotion_removed(self):
        html = self._render_promotion()
        self.assertNotIn("Powered by", html)
        self.assertNotIn("odoo.com", html)
        self.assertNotIn("Create a free website", html)

    def test_promotion_customizable(self):
        """The website editor can bring the promotion back"""
        self.view.active = False
        html = self._render_promotion()
        self.assertIn("Powered by", html)
        self.assertIn("odoo.com", html)
