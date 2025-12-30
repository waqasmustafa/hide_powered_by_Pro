# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_powered_by = fields.Boolean(
        string="Click to show and add your custom branding",
        related='company_id.show_powered_by',
        readonly=False,
        help="Enable to show custom 'Powered by' branding. If disabled, the branding is hidden."
    )
    powered_by_html = fields.Html(
        string="Custom Footer Text (HTML)",
        related='company_id.powered_by_html',
        readonly=False,
        help="Custom HTML text to replace 'Powered by Odoo'."
    )
