from odoo import models, api, fields, _

class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    name = fields.Char(default='new')
    # identifying info
    vin   = fields.Many2one('vehicle.vin', string='vin')
    vin6                    = fields.Char(compute="_compute_vin_6")
    vin8                    = fields.Char(compute="_compute_vin_8")
    licensePlate            = fields.Many2one('vehicle.plate', string='Plate')
    stockNo = fields.Char()

    # relational fields
    year    = fields.Many2one('vehicle.year', string="year")
    make    = fields.Many2one('vehicle.make', string="make")
    model   = fields.Many2one('vehicle.model', string="model")

    @api.depends('vin')
    def _compute_vin_6(self):
        for rec in self:
            rec.vin6 = rec.vin[-6:] if rec.vin else None

    @api.depends('vin')
    def _compute_vin_8(self):
        for rec in self:
            rec.vin6 = rec.vin[-8:] if rec.vin else None

class VehicleVin(models.Model):
    _name = 'vehicle.vin'
    _description = 'Vehicle Identification Number'
    _rec_name = 'vin'
    vin = fields.Char(string='VIN')

class VehicleYear(models.Model):
    _name = 'vehicle.year'
    _description = 'Vehicle Model Year  - not a build date'
    _rec_name = 'year'
    year = fields.Char(string="Year")

class VehicleMake(models.Model):
    _name = 'vehicle.make'
    _rec_name = 'make'
    make = fields.Char(string="Make")

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _rec_name = 'model'
    model = fields.Char(string="Model")
    image_medium = fields.Binary(string='image', store=True, attachment=True)

class VehiclePlate(models.Model):
    _name = 'vehicle.plate'
    _description = 'Vehicle License Plate'
    _rec_name = 'licensePlate'
    licensePlate = fields.Char(string='Plate')#, required=True)
    vin = fields.Many2one('vehicle.vin', string='vin')

