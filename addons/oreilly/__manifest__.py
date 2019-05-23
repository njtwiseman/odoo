# -*- coding: utf-8 -*-
{
    'name':        "oreilly",

    'summary':     
        """
            Oreilly Auto Parts Order Handling
        """,

    'description': 
        """
            Handles orders submitted on rwd.firstcallonline.com
        """,

    'author':      "Nick Wiseman",
    'website':     "nw.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'Uncategorized',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends':     ['base'],

    # always loaded
    'data':        [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/order_view.xml',
        'views/order_template.xml',
        'views/vehicle_view.xml',
        'views/vehicle_template.xml',
        'views/update_view.xml',
        'data/update_action.xml'
    ],
    # only loaded in demonstration mode
    'demo':        [
        'demo/demo.xml',
        'demo/demo2.xml',
        'demo/vehicle_demo.xml'
    ],
}
