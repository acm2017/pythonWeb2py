# -*- coding: utf-8 -*-

def index():
    """Main dashboard for hotel administration"""
    # Get summary statistics
    total_hotels = db(db.hotels).count()
    total_rooms = db(db.rooms).count()
    total_guests = db(db.guests).count()
    total_reservations = db(db.reservations).count()
    
    # Get current reservations
    current_reservations = db(db.reservations.status.belongs(['Confirmed', 'Checked In'])).select(
        db.reservations.ALL,
        db.hotels.name,
        db.rooms.room_number,
        db.guests.first_name,
        db.guests.last_name,
        left=[
            db.hotels.on(db.reservations.hotel_id == db.hotels.id),
            db.rooms.on(db.reservations.room_id == db.rooms.id),
            db.guests.on(db.reservations.guest_id == db.guests.id)
        ],
        orderby=db.reservations.check_in_date,
        limitby=(0, 10)
    )
    
    return dict(
        total_hotels=total_hotels,
        total_rooms=total_rooms,
        total_guests=total_guests,
        total_reservations=total_reservations,
        current_reservations=current_reservations
    )

@auth.requires_login()
def hotels():
    """Manage hotels"""
    grid = SQLFORM.grid(
        db.hotels,
        csv=False,
        searchable=True,
        sortable=True,
        deletable=True,
        editable=True,
        create=True,
        details=True,
        user_signature=False
    )
    return dict(grid=grid)

@auth.requires_login()
def rooms():
    """Manage rooms"""
    grid = SQLFORM.grid(
        db.rooms,
        csv=False,
        searchable=True,
        sortable=True,
        deletable=True,
        editable=True,
        create=True,
        details=True,
        user_signature=False,
        left=[db.hotels.on(db.rooms.hotel_id == db.hotels.id)]
    )
    return dict(grid=grid)

@auth.requires_login()
def guests():
    """Manage guests"""
    grid = SQLFORM.grid(
        db.guests,
        csv=False,
        searchable=True,
        sortable=True,
        deletable=True,
        editable=True,
        create=True,
        details=True,
        user_signature=False
    )
    return dict(grid=grid)

@auth.requires_login()
def reservations():
    """Manage reservations"""
    grid = SQLFORM.grid(
        db.reservations,
        csv=False,
        searchable=True,
        sortable=True,
        deletable=True,
        editable=True,
        create=True,
        details=True,
        user_signature=False,
        left=[
            db.hotels.on(db.reservations.hotel_id == db.hotels.id),
            db.rooms.on(db.reservations.room_id == db.rooms.id),
            db.guests.on(db.reservations.guest_id == db.guests.id)
        ]
    )
    return dict(grid=grid)

@auth.requires_login()
def new_reservation():
    """Create a new reservation"""
    form = SQLFORM(db.reservations)
    
    if form.process().accepted:
        # Calculate total amount based on dates and room price
        room = db.rooms[form.vars.room_id]
        check_in = form.vars.check_in_date
        check_out = form.vars.check_out_date
        
        if room and check_in and check_out:
            from datetime import datetime
            if isinstance(check_in, str):
                check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
            if isinstance(check_out, str):
                check_out = datetime.strptime(check_out, '%Y-%m-%d').date()
            
            nights = (check_out - check_in).days
            total_amount = nights * room.price_per_night
            
            db(db.reservations.id == form.vars.id).update(total_amount=total_amount)
            
        session.flash = 'Reservation created successfully'
        redirect(URL('reservations'))
    
    return dict(form=form)

@auth.requires_login()
def check_in():
    """Check in a guest"""
    reservation_id = request.args(0)
    if reservation_id:
        reservation = db.reservations[reservation_id]
        if reservation and reservation.status == 'Confirmed':
            db(db.reservations.id == reservation_id).update(status='Checked In')
            db(db.rooms.id == reservation.room_id).update(status='Occupied')
            session.flash = 'Guest checked in successfully'
        else:
            session.flash = 'Invalid reservation or already checked in'
    redirect(URL('reservations'))

@auth.requires_login()
def check_out():
    """Check out a guest"""
    reservation_id = request.args(0)
    if reservation_id:
        reservation = db.reservations[reservation_id]
        if reservation and reservation.status == 'Checked In':
            db(db.reservations.id == reservation_id).update(status='Checked Out')
            db(db.rooms.id == reservation.room_id).update(status='Available')
            session.flash = 'Guest checked out successfully'
        else:
            session.flash = 'Invalid reservation or not checked in'
    redirect(URL('reservations'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)