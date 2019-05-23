# -*- coding:  utf-8 -*-

from odoo import models, fields, api

class vehicle(models.Model):
        _name                   = 'oreilly.vehicle'
        _description            = 'a vehicle from Oreilly Auto Parts Website'
        #_sql_constraints = [ 
                #('vin', 'unique(vin)', 'Vehicle already Exists')
                #]

        name                    = fields.Char()
        description             = fields.Text()
        my_ident                = fields.Char()
        createDateTime          = fields.Char()
        epcVehicleYear          = fields.Char()
        epcVehicleMake          = fields.Char()
        epcVehicleModel         = fields.Char()
        vin                     = fields.Char()
        licensePlate            = fields.Char()
        sourceVinScanner        = fields.Char()
        vehicleNotes            = fields.Char()
