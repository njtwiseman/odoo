# -*- coding: utf-8 -*-
from odoo import http

class AutoShop(http.Controller):
    @http.route('/auto_shop/auto_shop/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/auto_shop/auto_shop/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('auto_shop.listing', {
            'root': '/auto_shop/auto_shop',
            'objects': http.request.env['auto_shop.auto_shop'].search([]),
        })

    @http.route('/auto_shop/auto_shop/objects/<model("auto_shop.auto_shop"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('auto_shop.object', {
            'object': obj
        })
