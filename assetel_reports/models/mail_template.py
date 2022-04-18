# -*- coding: utf-8 -*-
from odoo import models, api, fields

class MailTemplate(models.Model):
    _inherit = 'mail.template'
    
    user_signature = fields.Boolean('Añadir firma', default=False)
