# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class CreateCar(models.Model):
    _name = 'rental.cardetails'
    _description = 'Create a car'
    _rec_name = 'car_brand'

    car_brand = fields.Char(string='Brand', required=True)
    car_model = fields.Char(string='Model', required=True)
    car_year = fields.Integer('Year', required=True)
    car_color = fields.Char(string='Color')
    car_type = fields.Selection([
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
    ], string='Type')
    car_status = fields.Integer('Status')
    car_image = fields.Binary(string='Image')
    car_seq = fields.Char(string='Car ID', required=True, copy=False, readonly=True,
                          index=True, default=lambda self: _('New'))

    # code for overrite the create method and assign a sequence value when creating a car
    @api.model
    def create(self, vals):
        if vals.get('car_seq', _('New')) == _('New'):
            vals['car_seq'] = self.env['ir.sequence'].next_by_code('car.model.sequence') or _('New')
        result = super(CreateCar, self).create(vals)
        return result
