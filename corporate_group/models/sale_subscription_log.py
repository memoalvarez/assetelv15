# -*- coding: utf-8 -*-

from odoo import models, api, fields

class SaleSubscriptionLog(models.Model):
	_inherit = 'sale.subscription.log'

	corporate_group_id = fields.Many2one('res.partner.category', string='Grupo corporativo', store=True, related='contact_id.corporate_group_id')
	contact_id = fields.Many2one('res.partner', string="Contacto")
	