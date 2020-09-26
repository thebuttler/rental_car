# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class CreateClient(models.Model):
    _name = 'rental.customerdetails'
    _description = 'Create a car'
    _rec_name = 'customer_firstname'

    customer_firstname = fields.Char(string='Name', required=True)
    customer_lastname = fields.Char(string='Last Name', required=True)
    customer_phone = fields.Integer('Phone', required=True)
    customer_email = fields.Char(string='Email')
    customer_address = fields.Char(string='Address')
    customer_status = fields.Integer('Status')
    customer_image = fields.Binary(string='Image')
    customer_seq = fields.Char(string='Client ID', required=True, copy=False, readonly=True,
                               index=True, default=lambda self: _('New'))

    # Override the create function for a sequence that is going to represent the id to use to handle the transactions
    @api.model
    def create(self, vals):
        if vals.get('customer_seq', _('New')) == _('New'):
            vals['customer_seq'] = self.env['ir.sequence'].next_by_code('client.details.sequence') or _('New')
        result = super(CreateClient, self).create(vals)
        return result
