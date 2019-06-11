from uuid import uuid1 

from odoo import models, api, fields, _


class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    name = fields.Char(default='new')
    vehicle_id = fields.Char(compute='_gen_id', store=True)

    # identifying info
    vin6                    = fields.Char(compute="_compute_vin_6")
    vin8                    = fields.Char(compute="_compute_vin_8")
    stockNo = fields.Char()

    # relational fields
    vin          = fields.Many2one('vehicle.vin')
    licensePlate = fields.Many2one('vehicle.plate')
    year         = fields.Many2one('vehicle.year')
    make         = fields.Many2one('vehicle.make')
    model        = fields.Many2one('vehicle.model')

    def _gen_id(self):
        for rec in self:
            rec.vehicle_id = uuid1()

    @api.depends('vin')
    def _compute_vin_6(self):
        for rec in self:
            rec.vin6 = rec.vin[-6:] if rec.vin else None

    @api.depends('vin')
    def _compute_vin_8(self):
        for rec in self:
            rec.vin6 = rec.vin[-8:] if rec.vin else None

    @api.multi
    def findVehicleInfo(self):
        """ RecordSet => None
        """
        for rec in self:
            print(self.env['oreilly.vehicle'].search(
                    [
                        ('licensePlate', '!=', ''),
                        '|',
                        ('vin', '!=', ''),
                        '&',
                        ('licensePlate','=',rec.licensePlate),
                        '|',
                        ('vin', '=', rec.vin),
                        ]
                    )
                    )

class VehicleVin(models.Model):
    _name = 'vehicle.vin'
    _description = 'Vehicle Identification Number'
    _rec_name = 'vin'
    _parent_store = True
    parent_path = fields.Char(index=True)
    parent_id = fields.One2many('vehicle.vehicle', 'vin',)

    vin = fields.Char(string='VIN')

    year = fields.Many2one('vehicle.year')

class VehiclePlate(models.Model):
    _name = 'vehicle.plate'
    _description = 'Vehicle License Plate'
    _rec_name = 'licensePlate'
    _parent_store = True
    _parent_name = 'vehicle_parent'
    parent_path = fields.Char(index=True)
    vehicle_parent = fields.One2many('vehicle.vehicle','licensePlate',)

    licensePlate = fields.Char(string='Plate')

    year = fields.Many2one('vehicle.year')


class VehicleYear(models.Model):
    _name = 'vehicle.year'
    _description = 'Vehicle Model Year  - not a build date'
    _rec_name = 'year'
    _parent_store = True
    _parent_name = 'vehicle_id'
    parent_path = fields.Char(index=True)
    vehicle_id = fields.One2many('vehicle.vehicle','year')

    year = fields.Char(string="Year")
    make = fields.Many2one('vehicle.make')


class VehicleMake(models.Model):
    _name = 'vehicle.make'
    _rec_name = 'make'
    _parent_store = True
    _parent_name = 'year'
    parent_path = fields.Char(index=True)
    year = fields.One2many('vehicle.year','year',)

    make = fields.Char(string="Make")
    model = fields.Many2one('vehicle.model')

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _rec_name = 'model'
    _parent_store = True
    _parent_name = 'make'
    parent_path = fields.Char(index=True)
    make = fields.One2many('vehicle.make', 'model',)

    model = fields.Char(string="Model")


    image_medium = fields.Binary(string='image', store=True, attachment=True)


