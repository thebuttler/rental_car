# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class RentalCarContract(models.Model):
    _name = 'service.carcontract'
    _description = 'Car Rental Contract'
    _rec_name = 'contract_seq'
    _order = "id desc"

    # variables created for the relation fields between the car model
    car_id = fields.Many2one('rental.cardetails', string='CarID', required=True)
    cars_model = fields.Char('Model', related='car_id.car_model')
    cars_year = fields.Integer('Year', related='car_id.car_year')
    cars_color = fields.Char('Color', related='car_id.car_color')
    # variables created for the related fields between the clients
    user_id = fields.Many2one('rental.customerdetails', string='ClientID', required=True)
    client_firstname = fields.Char('First Name', related='user_id.customer_firstname')
    client_lastname = fields.Char('Last Name', related='user_id.customer_lastname')
    client_phone = fields.Integer('Phone', related='user_id.customer_phone')
    client_email = fields.Char('Client Email', related='user_id.customer_email')
    # test =fields.One2Many(string='TestUse')
    # Variables for the contract dates and cost of the service
    cost_upfront = fields.Float(string='Cost of the service', track_visibility="onchange",
                                help='the money will be refunded when the vehicle is delivered')
    cost_frequency = fields.Selection([
        ('no', 'No'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ], 'Recurring cost depending of the time', default='no', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    expiration_date = fields.Date(string='Expiration Date', required=True)
    state = fields.Selection([
        ('start', 'Start'),
        ('notrented', 'Not Rented'),
        ('rented', 'Rented'),
    ], string='Status', readonly=True, default='start')
    contract_seq = fields.Char(string='Contract ID', required=True, copy=False, readonly=True,
                               index=True, default=lambda self: _('New'))

    def begin_contract(self):
        for x in self:
            x.state = 'rented'

    def end_contract(self):
        for z in self:
            z.state = 'notrented'

    @api.model
    def create(self, vals):
        if vals.get('contract_seq', _('New')) == _('New'):
            vals['contract_seq'] = self.env['ir.sequence'].next_by_code('rent.contract.sequence') or _('New')
        result = super(RentalCarContract, self).create(vals)
        return result
