# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_powered_by = fields.Boolean(
        string="Click to show and add your custom branding",
        config_parameter='hide_powered_by_Pro.show_powered_by',
        help="Enable to show custom 'Powered by' branding. If disabled, the branding is hidden."
    )
    powered_by_html = fields.Html(
        string="Custom Footer Text (HTML)",
        config_parameter='hide_powered_by_Pro.powered_by_html',
        help="Custom HTML text to replace 'Powered by Odoo'."
    )
