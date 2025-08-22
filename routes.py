# -*- coding: utf-8 -*-

# Web2py routes configuration for hotel administration system

# Default application
default_application = 'hotel_admin'
default_controller = 'default'
default_function = 'index'

# Routes for clean URLs
routes_in = (
    ('/hotel_admin', '/hotel_admin/default/index'),
    ('/hotel_admin/$anything', '/hotel_admin/$anything'),
    ('/$anything', '/hotel_admin/default/$anything'),
)

routes_out = (
    ('/hotel_admin/default/index', '/hotel_admin'),
    ('/hotel_admin/default/$anything', '/$anything'),
    ('/hotel_admin/$anything', '/hotel_admin/$anything'),
)