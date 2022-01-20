# -*- coding: utf-8 -*-
{
    'name': "Colegio addons",
    'version': '15.0',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'l10n_mx', 'account_check_printing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_payment_view.xml',

        'report/print_check.xml',
        'report/print_check_generic.xml',
        'report/print_check_bbva_bancomer.xml',
        'report/print_check_banamex.xml',
        'report/print_check_hsbc.xml',
        'report/print_check_santander.xml',
        'report/print_check_scotiabank.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}