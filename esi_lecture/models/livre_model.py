from odoo import models, fields, api
from datetime import datetime
import logging

class Livre(models.Model):
    _name='livre.livre'

    name=fields.Char(string='title', required=True, unique=True)
    description= fields.Text(string='description')
    couverture_image=fields.Binary(string='image de couverture')
    date_publication = fields.Date(
        string='Date de publication',
        default=lambda self: fields.Date.to_string(datetime.today()),
        help='La date de publication doit être antérieure à la date du jour.'
    )
    nombre_page=fields.Integer(string='nombre de page')

    likes_count = fields.Integer(string='Nombre de Likes', compute='_compute_likes_count')
    liked = fields.Boolean(string='Liked', compute='_compute_liked')
    liked_by_users = fields.Many2many('res.users', string='Utilisateurs ayant aimé')

    auteur_ids = fields.Many2many('res.partner', string='Auteurs')


    @api.constrains('nombre_page')
    def _check_nombre_page(self):
        for record in self:
            if record.nombre_page < 1:
                raise models.ValidationError("Le nombre de pages doit être égal ou supérieur à 1.")


    @api.constrains('date_publication')
    def _check_date_publication(self):
        for record in self:
            if record.date_publication >= fields.Date.today():
                raise models.ValidationError("La date de publication doit être antérieure à la date du jour.")

    @api.depends('liked_by_users')
    def _compute_likes_count(self):
        for record in self:
            record.likes_count = len(record.liked_by_users)

    @api.depends('liked_by_users')
    def _compute_liked(self):
        current_user = self.env.user
        for record in self:
            record.liked = bool(current_user in record.liked_by_users if record.liked_by_users else False)

    def toggle_like(self):
        current_user = self.env.user
        if current_user in self.liked_by_users:
            self.liked_by_users -= current_user
        else:
            self.liked_by_users += current_user
            
        return True

