# -*- coding: utf-8 -*-
# from odoo import http


# class Lekurde(http.Controller):
#     @http.route('/lekurde/lekurde', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lekurde/lekurde/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lekurde.listing', {
#             'root': '/lekurde/lekurde',
#             'objects': http.request.env['lekurde.lekurde'].search([]),
#         })

#     @http.route('/lekurde/lekurde/objects/<model("lekurde.lekurde"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lekurde.object', {
#             'object': obj
#         })

