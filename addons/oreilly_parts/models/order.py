# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OreillyOrder(models.Model):
    _name = 'oreilly.order' 
    name = fields.Char()
    ident = fields.Char()
    modifiedDateTime = fields.Char()
    orderConfirmationNumber = fields.Char()
    orderSubmittedDateTime = fields.Char()
    orderName = fields.Char()
    vehicleDesc = fields.Char()
    firstName = fields.Char()
    lastName = fields.Char()
    shopCost = fields.Char()
    descFragment = fields.Char()
    createdDateTime = fields.Char()
    worksheetState = fields.Char()
    totalPrice = fields.Char()
    empty = fields.Char()
