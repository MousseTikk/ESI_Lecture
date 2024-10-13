# -*- coding: utf-8 -*-
# from odoo import http


# class EsiLecture(http.Controller):
#     @http.route('/esi_lecture/esi_lecture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esi_lecture/esi_lecture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esi_lecture.listing', {
#             'root': '/esi_lecture/esi_lecture',
#             'objects': http.request.env['esi_lecture.esi_lecture'].search([]),
#         })

#     @http.route('/esi_lecture/esi_lecture/objects/<model("esi_lecture.esi_lecture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esi_lecture.object', {
#             'object': obj
#         })
