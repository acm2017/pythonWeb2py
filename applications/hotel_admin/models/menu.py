# -*- coding: utf-8 -*-

# Application menu
response.menu = [
    (T('Dashboard'), False, URL('default', 'index'), []),
    (T('Hotels'), False, URL('default', 'hotels'), []),
    (T('Rooms'), False, URL('default', 'rooms'), []),
    (T('Guests'), False, URL('default', 'guests'), []),
    (T('Reservations'), False, URL('default', 'reservations'), []),
]

# Set response defaults
response.title = 'Hotel Administration System'
response.subtitle = ''
response.author = 'Hotel Admin System'
response.keywords = 'hotel, administration, web2py'
response.description = 'Hotel Administration System built with web2py'