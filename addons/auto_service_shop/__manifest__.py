# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU AGPL (v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AGPL (AGPL v3) for more details.
#
##############################################################################
{
    'name': 'Auto Service Management',
    'version': '12.0.1.0.1',
    'summary': 'Module for managing auto service shop daily activities.',
    'category': 'Industries',
    'author': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['stock_account', 'mail', 'product', 'account'],
    'data': ['security/security.xml',
             'security/ir.model.access.csv',
             'views/auto_service_views.xml',
             'views/vehicle_views.xml',
             #'wizard/auto_create_invoice_views.xml',
             #'reports/auto_service_ticket.xml',
             #'reports/service_ticket_template.xml',
             'data/auto_service_data.xml',
             'data/auto_service_email_template.xml',
             'data/vehicle.ymm.csv'],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
