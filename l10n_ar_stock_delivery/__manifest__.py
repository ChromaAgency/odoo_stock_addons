{
    'name': 'Integracion entre modulo delivery y localización argentina',
    'version': '17.0.1.1.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'Chroma Agency',
    'website': 'https://portal.chroma.agency/',
    'license': 'AGPL-3',
    'depends': [
        'delivery_ux',
        'l10n_ar_stock',
    ],
    'data': [
        'views/report_deliveryslip.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
