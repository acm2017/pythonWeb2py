# -*- coding: utf-8 -*-

# Database configuration
db = DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])

# Define auth tables
from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False, signature=False)

# Hotels table
db.define_table('hotels',
    Field('name', 'string', length=100, required=True, label='Hotel Name'),
    Field('address', 'text', label='Address'),
    Field('phone', 'string', length=20, label='Phone'),
    Field('email', 'string', length=100, label='Email'),
    Field('description', 'text', label='Description'),
    Field('created_on', 'datetime', default=request.now, readable=False, writable=False),
    Field('created_by', 'reference auth_user', default=auth.user_id, readable=False, writable=False),
    format='%(name)s'
)

# Room types
ROOM_TYPES = ['Single', 'Double', 'Suite', 'Deluxe', 'Family']
ROOM_STATUS = ['Available', 'Occupied', 'Maintenance', 'Out of Order']

# Rooms table
db.define_table('rooms',
    Field('hotel_id', 'reference hotels', required=True, label='Hotel'),
    Field('room_number', 'string', length=10, required=True, label='Room Number'),
    Field('room_type', 'string', requires=IS_IN_SET(ROOM_TYPES), label='Room Type'),
    Field('capacity', 'integer', default=1, label='Capacity'),
    Field('price_per_night', 'decimal(10,2)', required=True, label='Price per Night'),
    Field('status', 'string', requires=IS_IN_SET(ROOM_STATUS), default='Available', label='Status'),
    Field('description', 'text', label='Description'),
    Field('created_on', 'datetime', default=request.now, readable=False, writable=False),
    Field('created_by', 'reference auth_user', default=auth.user_id, readable=False, writable=False),
    format='%(room_number)s'
)

# Guests table
db.define_table('guests',
    Field('first_name', 'string', length=50, required=True, label='First Name'),
    Field('last_name', 'string', length=50, required=True, label='Last Name'),
    Field('email', 'string', length=100, label='Email'),
    Field('phone', 'string', length=20, label='Phone'),
    Field('address', 'text', label='Address'),
    Field('id_number', 'string', length=20, label='ID Number'),
    Field('created_on', 'datetime', default=request.now, readable=False, writable=False),
    Field('created_by', 'reference auth_user', default=auth.user_id, readable=False, writable=False),
    format='%(first_name)s %(last_name)s'
)

# Reservation status
RESERVATION_STATUS = ['Pending', 'Confirmed', 'Checked In', 'Checked Out', 'Cancelled']

# Reservations table
db.define_table('reservations',
    Field('hotel_id', 'reference hotels', required=True, label='Hotel'),
    Field('room_id', 'reference rooms', required=True, label='Room'),
    Field('guest_id', 'reference guests', required=True, label='Guest'),
    Field('check_in_date', 'date', required=True, label='Check-in Date'),
    Field('check_out_date', 'date', required=True, label='Check-out Date'),
    Field('adults', 'integer', default=1, label='Adults'),
    Field('children', 'integer', default=0, label='Children'),
    Field('total_amount', 'decimal(10,2)', label='Total Amount'),
    Field('status', 'string', requires=IS_IN_SET(RESERVATION_STATUS), default='Pending', label='Status'),
    Field('notes', 'text', label='Notes'),
    Field('created_on', 'datetime', default=request.now, readable=False, writable=False),
    Field('created_by', 'reference auth_user', default=auth.user_id, readable=False, writable=False),
    format='Reservation #%(id)s'
)

# Add constraints
db.rooms.room_number.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'rooms.room_number')]
db.guests.email.requires = IS_EMAIL()
db.reservations.check_in_date.requires = IS_DATE()
db.reservations.check_out_date.requires = IS_DATE()

# Common fields
for table in db.tables:
    if hasattr(db[table], 'created_on'):
        db[table].id.readable = False
        db[table].created_on.represent = lambda value, row: value.strftime("%Y-%m-%d %H:%M")