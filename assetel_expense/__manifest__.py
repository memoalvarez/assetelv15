# -*- coding: utf-8 -*-
{
    'name': "Modificaciones gastos Assetel",

    'summary': """
        Modificaciones gastos Assetel""",

    'description': """
        Modificaciones gastos Assetel
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_expense'],

    # always loaded
    'data': [
        'views/hr_expense.xml',
    ],
}
