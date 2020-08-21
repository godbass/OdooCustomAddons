# -*- coding: utf-8 -*-
{
    'name': "Gérer Mon Salon de Couture",
    'version': "12.0.1",
    'category': 'Extra Tools',
    'summary': "Module for managing a sewing workshop",
    'sequence': "2",
    'author': "Willof-God Bassanti",
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/couturier.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}