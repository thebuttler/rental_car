# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Rental Cars',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'sequence': 5,
    'summary': 'Track the rental of automobiles',
    'description': "",
    'website': 'www.rulesware.com',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/rsecurity.xml',
        'views/Rental.xml',
        'views/Customer.xml',
        'views/Contract.xml',
        'data/sequence.xml',

    ],
    'demo': [],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
