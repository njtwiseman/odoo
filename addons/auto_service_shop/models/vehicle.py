from uuid import uuid1
from odoo import models, api, fields


class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _rec_name = 'vehicle_id'
    vehicle_id = fields.Char()
    customer_id = fields.Many2one('res.partner')
    make = fields.Char(related='ymm.make')
    model = fields.Char(related='ymm.model')
    year = fields.Char(related='ymm.year')

    # identifying info
    stockNo = fields.Char()

    # relational fields
    vin = fields.Many2one('vehicle.vin')
    vin6 = fields.Char(related='vin.vin6')
    vin8 = fields.Char(related='vin.vin8')
    licensePlate = fields.Char()  # Many2one('vehicle.plate')
    ymm = fields.Many2one('vehicle.ymm')

    def _gen_id(self):
        for rec in self:
            rec.vehicle_id = uuid1()

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
                    ('licensePlate', '=', rec.licensePlate),
                    '|',
                    ('vin', '=', rec.vin),
                ]
            ))


class VehicleVin(models.Model):
    _name = 'vehicle.vin'
    _description = 'Vehicle Identification Number'
    id = fields.Char(string='VIN')
    vehicle_id = fields.One2many('vehicle.vehicle', 'vin')
    vin6 = fields.Char(compute="_compute_vin_6")
    vin8 = fields.Char(compute="_compute_vin_8")
    
    def _compute_vin_6(self):
        for rec in self:
            rec.vin6 = rec.vin[-6:] if rec.vin else None

    def _compute_vin_8(self):
        for rec in self:
            rec.vin6 = rec.vin[-8:] if rec.vin else None


class VehiclePlate(models.Model):
    _name = 'vehicle.plate'
    _description = 'Vehicle License Plate'
    id = fields.Char(string='Plate')


class YMM(models.Model):
    _name = 'vehicle.ymm'
    _description = "the Year Make and Model"
    id = fields.Char()
    vehicle_id = fields.One2many('vehicle.vehicle', 'ymm')
    name = fields.Char(compute="_combine_name")
    year = fields.Char()  # Many2one('vehicle.year')
    rel_year = fields.Many2many('ymm.year')
    make = fields.Char()  # Many2one('vehicle.make')
    rel_make = fields.Many2many('ymm.make')
    model = fields.Char()  # Many2one('vehicle.model')
    rel_model = fields.Many2many('ymm.model')

    def _combine_name(self):
        for rec in self:
            rec.name = f"{rec.year} {rec.make} {rec.model}"


class VehicleYear(models.Model):
    _name = 'ymm.year'
    _description = 'Vehicle Model Year  - not a build date'
    id = fields.Char(string="Year")
    rel_ymm = fields.Many2many('vehicle.ymm')


class VehicleMake(models.Model):
    _name = 'ymm.make'
    _description = 'Vehicle Manufacturer'
    id = fields.Char(string="Make")
    rel_make = fields.Many2many('vehicle.ymm')


class VehicleModel(models.Model):
    _name = 'ymm.model'
    _description = 'Manufacturer\'s Model Name'
    id = fields.Char(string="Model")
    rel_make = fields.Many2many('vehicle.ymm')
    image_medium = fields.Binary(string='image', store=True, attachment=True)
