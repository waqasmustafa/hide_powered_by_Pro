# -*- coding: utf-8 -*-
from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    show_powered_by = fields.Boolean(
        string="Show Custom Branding",
        default=False,
        help="Enable to show custom 'Powered by' branding."
    )
    powered_by_html = fields.Html(
        string="Custom Footer Text",
        translate=True,
        help="Custom HTML text to replace 'Powered by Odoo'."
    )
