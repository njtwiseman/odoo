# -*- coding:  utf-8 -*-
from .. import tools
from odoo import models, fields, api

class Update(models.Model):
    _name = 'oreilly.update'
    _description = 'oreilly data fetcher / updater' 

    name = fields.Char()
    numberOfUpdates = fields.Integer('Number of Updates', help='The number of times the updater has run')
    lastUpdated = fields.Date('Last Updated')
    def oreilly_update(self):
        """ performs an update fetch """
               
                      
        self.numberOfUpdates += 1

        print("------------- Hello  World")
       

        oReillySession = tools.rwdfco.FirstCallOnline()
        oData = oReillySession.getData()
        
        self.env['oreilly.vehicle'].create(oData['vehicles'])
        self.env['oreilly.order'].create(oData['orders'])
        

        print("------------- Hello  World")
