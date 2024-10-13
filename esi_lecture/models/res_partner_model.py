from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    livre_id = fields.Many2many('livre.livre', string='Auteurs')