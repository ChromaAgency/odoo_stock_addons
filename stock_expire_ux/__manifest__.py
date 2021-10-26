
{
    'name': 'Stock Expiry',
    'version': "13.0.1.2.0",
    'category': 'Warehouse Management',
    'sequence': 14,
    'summary': '',
    'author': 'Making Argentina',
    'website': 'www.making.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'stock',
        'product_expiry'
    ],
    'data': [
        "views/stock_move_line.xml",
        "views/stock_production_lot.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
