# -*- coding: utf-8 -*-
from odoo import http

class Oreilly(http.Controller):
    # --- Main Module Object ---
    @http.route('/oreilly/oreilly/', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/oreilly/oreilly/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('oreilly.listing', {
            'root': '/oreilly/oreilly',
            'objects': http.request.env['oreilly.oreilly'].search([]),
        })
    
    @http.route('/oreilly/oreilly/objects/<model("oreilly.oreilly"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('oreilly.object', {
            'object': obj
        })
    
    
    # --- Order Object ---
    @http.route('/oreilly/order/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('oreilly.order_listing', {
            'root': '/oreilly/order',
            'objects': http.request.env['oreilly.order'].search([]),
        })
    
    @http.route('/oreilly/order/objects/<model("oreilly.order"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('oreilly.order', {
            'object':obj
        })
    
    # --- Vehicle Object ---
    @http.route('/oreilly/vehicle/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('oreilly.vehicle_listing', {
            'root': '/oreilly/vehicle',
            'objects': http.request.env['oreilly.vehicle'].search([]),
        })
    
    @http.route('/oreilly/vehicle/objects/<model("oreilly.vehicle"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('oreilly.vehicle', {
            'object':obj
        })

    @http.route('/oreilly/update/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('oreilly.update_listing', {
            'root':'/oreilly/update',
            'objects': http.request.env['oreilly.update'].search([])
        })

    @http.route('/oreilly/update/objects/<model("oreilly.update"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('oreilly.update', {
            'object':obj
        })
