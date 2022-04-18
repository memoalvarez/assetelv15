# -*- coding: utf-8 -*-
from odoo import models, api, fields

class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

res_model_id = fields.Many2one('ir.model', 'Related Document Model', index=True, ondelete='cascade', help='Model of the followed resource')