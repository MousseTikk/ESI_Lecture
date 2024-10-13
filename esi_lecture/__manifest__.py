# -*- coding: utf-8 -*-
{
    'name': "esi_lecture",

    'summary': """
        Module de gestion/Vente/Stock de livres
        """,

    'description': """
        Ceci est un module permettant la gestion/vente/stock de livres
    """,

    'author': "G57618 et G56583",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'point_of_sale',
        'stock',     
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/livre_menu.xml',
        'views/livre_view.xml',
        'views/res_partner_view.xml',
        'views/product_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True, 
    'auto_install': True,  # Si True, les dépendances seront installées automatiquement lors de l'installation
}
