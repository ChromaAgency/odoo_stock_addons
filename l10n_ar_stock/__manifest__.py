{
    'name': ' stock para Argentina',
    'version': '14.0.1.15.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'Making SA',
    'website': 'www.making.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'stock_voucher',  # por la clase receiptbooks y demas
        'l10n_ar', 'delivery' 
    ],
    'data': [
        'security/l10n_ar_stock_security.xml',
        'wizards/arba_cot_wizard_views.xml',
        'wizards/res_config_settings_view.xml',
        'views/stock_picking_views.xml',
        'views/stock_book_views.xml',
        'views/product_template_views.xml',
        'views/uom_uom_views.xml',
        'views/stock_production_lot_views.xml',
        'views/report_deliveryslip.xml',
        'views/report_invoice.xml',
        'data/ir_sequence_data.xml',
        'data/product_uom_data.xml',
        'data/document_type_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
