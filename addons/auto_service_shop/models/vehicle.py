from uuid import uuid1 

from odoo import models, api, fields, _


class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    vehicle_id = fields.Char(compute='_gen_id', store=True)
    _rec_name = 'vehicle_id'

    # identifying info
    vin6                    = fields.Char(compute="_compute_vin_6")
    vin8                    = fields.Char(compute="_compute_vin_8")
    stockNo = fields.Char()

    # relational fields
    vin          = fields.Char()#Many2one('vehicle.vin')
    licensePlate = fields.Char()#Many2one('vehicle.plate')
    ymm = fields.Many2one('vehicle.ymm')
    make = fields.Char(related='ymm.make')
    model = fields.Char(related='ymm.model')
    year = fields.Char(related='ymm.year')


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

            Split into vinSearch and plateSearch
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
    id = fields.Char(string='VIN')

class VehiclePlate(models.Model):
    _name = 'vehicle.plate'
    _description = 'Vehicle License Plate'
    id = fields.Char(string='Plate')

class YMM(models.Model):
    _name = 'vehicle.ymm'
    _description = "the Year Make and Model"
    vehicle_id = fields.One2many('vehicle.vehicle', 'ymm')
    name = fields.Char(compute="_combine_name")
    year  = fields.Char()#Many2one('vehicle.year')
    make  = fields.Char()#Many2one('vehicle.make')
    model = fields.Char()#Many2one('vehicle.model')

    def _combine_name(self):
        for rec in self:
            rec.name = f"{rec.year} {rec.make} {rec.model}"

class VehicleYear(models.Model):
    _name = 'vehicle.year'
    _description = 'Vehicle Model Year  - not a build date'
    id = fields.Char(string="Year")

class VehicleMake(models.Model):
    _name = 'vehicle.make'
    id = fields.Char(string="Make")

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    id = fields.Char(string="Model")
    image_medium = fields.Binary(string='image', store=True, attachment=True)


