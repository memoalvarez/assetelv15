# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Assetel",

    'summary': """
        Modificación del Formulario Helpdesk""",

    'description': """
       Modificación del Formulario Helpdesk
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'installed_services'],

    # always loaded
    'data': [
        'views/rating_rating.xml',
        'views/templates.xml',
    ],
    
}