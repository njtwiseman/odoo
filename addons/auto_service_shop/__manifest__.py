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
    'category': '',
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'depends': ['base', 'stock_account', 'mail', 'product', 'account'],
    'data': ['security/security.xml',
             'security/ir.model.access.csv',
             'views/vehicle_views.xml',
             'views/vehicle_template.xml',
             'views/vehicle_action.xml',
             'views/auto_service_views.xml',
             #  'wizard/auto_create_invoice_views.xml',
             #  'reports/auto_service_ticket.xml',
             #  'reports/service_ticket_template.xml',
             'data/auto_service_data.xml',
             'data/auto_service_email_template.xml',
             'data/vehicle.ymm.csv',
             'views/view.xml'],
    'images': ['static/description/banner.jpg',
               'static/img/png/car.png'],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'AGPL-3',
}
