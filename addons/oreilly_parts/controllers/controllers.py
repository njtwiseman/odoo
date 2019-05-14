# -*- coding: utf-8 -*-
from odoo import http

# class OreillyParts(http.Controller):
#     @http.route('/oreilly_parts/oreilly_parts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oreilly_parts/oreilly_parts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oreilly_parts.listing', {
#             'root': '/oreilly_parts/oreilly_parts',
#             'objects': http.request.env['oreilly_parts.oreilly_parts'].search([]),
#         })

#     @http.route('/oreilly_parts/oreilly_parts/objects/<model("oreilly_parts.oreilly_parts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oreilly_parts.object', {
#             'object': obj
#         })