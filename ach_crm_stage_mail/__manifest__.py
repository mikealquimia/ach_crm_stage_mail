# -*- coding: utf-8 -*-
{
    'name': "CRM Stage Mail",
    'summary': """
        Mail when changing stage""",
    'description': """
        send email templates automatically when changing stage
    """,
    'author': "Gt Alchemy Development",
    'license': 'LGPL-3',
    'support': 'developmentalchemygx@gmail.com',
    'category': 'Sales',
    'version': '1.1',
    'depends': ['base', 
                'crm'],
    'data': [
        'views/crm_stage.xml',
    ],
    'images': ['static/description/banner.png'],
}