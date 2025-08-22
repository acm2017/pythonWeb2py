# -*- coding: utf-8 -*-

# Sample data for hotel administration system
# This file will populate the database with initial data for testing

if db(db.hotels).isempty():
    # Create sample hotels
    hotel1_id = db.hotels.insert(
        name='Grand Plaza Hotel',
        address='123 Main Street, Downtown',
        phone='+1-555-0123',
        email='info@grandplaza.com',
        description='A luxury hotel in the heart of downtown with excellent amenities.'
    )
    
    hotel2_id = db.hotels.insert(
        name='Seaside Resort',
        address='456 Ocean Drive, Beachfront',
        phone='+1-555-0456',
        email='reservations@seasideresort.com',
        description='Beautiful beachfront resort with ocean views and spa services.'
    )
    
    # Create sample rooms for hotel 1
    db.rooms.insert(
        hotel_id=hotel1_id,
        room_number='101',
        room_type='Single',
        capacity=1,
        price_per_night=89.99,
        status='Available',
        description='Cozy single room with city view'
    )
    
    db.rooms.insert(
        hotel_id=hotel1_id,
        room_number='102',
        room_type='Double',
        capacity=2,
        price_per_night=129.99,
        status='Available',
        description='Comfortable double room with modern amenities'
    )
    
    db.rooms.insert(
        hotel_id=hotel1_id,
        room_number='201',
        room_type='Suite',
        capacity=4,
        price_per_night=249.99,
        status='Available',
        description='Luxurious suite with separate living area'
    )
    
    # Create sample rooms for hotel 2
    db.rooms.insert(
        hotel_id=hotel2_id,
        room_number='A1',
        room_type='Double',
        capacity=2,
        price_per_night=159.99,
        status='Available',
        description='Ocean view double room'
    )
    
    db.rooms.insert(
        hotel_id=hotel2_id,
        room_number='B1',
        room_type='Family',
        capacity=6,
        price_per_night=299.99,
        status='Available',
        description='Spacious family room with ocean view'
    )
    
    # Create sample guests
    guest1_id = db.guests.insert(
        first_name='John',
        last_name='Smith',
        email='john.smith@email.com',
        phone='+1-555-1234',
        address='789 Oak Street, Hometown',
        id_number='ID123456789'
    )
    
    guest2_id = db.guests.insert(
        first_name='Jane',
        last_name='Doe',
        email='jane.doe@email.com',
        phone='+1-555-5678',
        address='321 Pine Avenue, Cityville',
        id_number='ID987654321'
    )
    
    # Create sample reservations
    import datetime
    from datetime import timedelta
    
    today = datetime.date.today()
    
    # Current reservation
    room1 = db(db.rooms.room_number == '101').select().first()
    if room1:
        db.reservations.insert(
            hotel_id=hotel1_id,
            room_id=room1.id,
            guest_id=guest1_id,
            check_in_date=today,
            check_out_date=today + timedelta(days=3),
            adults=1,
            children=0,
            total_amount=269.97,  # 3 nights * 89.99
            status='Confirmed',
            notes='Early check-in requested'
        )
    
    # Future reservation
    room2 = db(db.rooms.room_number == 'A1').select().first()
    if room2:
        db.reservations.insert(
            hotel_id=hotel2_id,
            room_id=room2.id,
            guest_id=guest2_id,
            check_in_date=today + timedelta(days=7),
            check_out_date=today + timedelta(days=10),
            adults=2,
            children=0,
            total_amount=479.97,  # 3 nights * 159.99
            status='Confirmed',
            notes='Anniversary trip'
        )

db.commit()