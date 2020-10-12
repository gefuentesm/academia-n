# -*- coding: utf-8 -*-
# from odoo import http


# class Ambassador(http.Controller):
#     @http.route('/ambassador/ambassador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ambassador/ambassador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ambassador.listing', {
#             'root': '/ambassador/ambassador',
#             'objects': http.request.env['ambassador.ambassador'].search([]),
#         })

#     @http.route('/ambassador/ambassador/objects/<model("ambassador.ambassador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ambassador.object', {
#             'object': obj
#         })
