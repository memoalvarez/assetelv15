# -*- coding: utf-8 -*-
{
    'name': "Instalación de Servicio",

    'summary': """
        Instalación de Servicio""",

    'description': """
        Instalación de Servicio
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'installed_services', 'mrp', 'service_sizing'],

    # always loaded
    'data': [
        'views/project_task_templates.xml',
        'views/project_task_type.xml',
        'views/project_task.xml',
        'views/installed_services.xml',
        'views/mrp_production.xml',
        'views/sale_order.xml',
        'views/sign_template.xml',
        'views/sign_request.xml',
    ],
}
