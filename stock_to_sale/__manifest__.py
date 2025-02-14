# -*- coding: utf-8 -*-
{
    'name': 'Stock para ventas',
    'summary': 'Agrega un campo donde se indica el stock ignorando las ubicaciones de transito',
    'version': '1.0.1',
    'author': 'Chroma',
    'website': 'https://www.chroma.agency',
    "category": "Stock",
    "depends": ['base','stock'],
    'data': [
        'views/product.template.xml',
    ],
    'installable': True,
    'license': 'GPL-3',
}