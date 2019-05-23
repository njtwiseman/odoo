# -*- coding: utf-8 -*-
from openerp.exceptions import ValidationError
from odoo import models, fields, api

class Order(models.Model):
    _name                   = 'oreilly.order'
    _description            = 'an Order from Oreilly Auto Parts Website'
    name                    = fields.Char()
    description             = fields.Text()
#    _sql_constraints = [ 
#            ('my_ident', 'unique(my_ident)', 'Order already Exists')
#            ]


    my_ident                = fields.Char()
    modifiedDateTime        = fields.Char()
    orderConfirmationNumber = fields.Char()
    orderSubmittedDateTime  = fields.Char()
    orderName               = fields.Char()
    vehicleDesc             = fields.Char()
    firstName               = fields.Char()
    lastName                = fields.Char()
    shopCost                = fields.Char()
    descFragment            = fields.Char()
    createdDateTime         = fields.Char()
    worksheetState          = fields.Char()
    totalPrice              = fields.Char()
    empty                   = fields.Boolean('Empty')
    
##    @api.constrains('my_ident')#
#    def _check_my_ident(self):
#        orderObjects = self.env['oreilly.order']
#        for record in self:
#            records = orderObjects.search([('my_ident','=',record.my_ident)])
#            if records:
#                #raise ValidationError(_('This one (%s) exists' % record.my_ident))
#                print(records)
#                print("Found one")
#            else:
#                print("hi")
#
#            
#   
#   
#   
