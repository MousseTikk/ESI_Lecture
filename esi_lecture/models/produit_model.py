from odoo import models, fields, api


class Produit(models.Model):
    _inherit='product.template'

    livre_ids = fields.Many2many('livre.livre', string='Livres Associés')