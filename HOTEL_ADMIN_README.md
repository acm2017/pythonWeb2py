# Hotel Administration System

A comprehensive hotel management system built with the Web2py framework, providing complete administration capabilities for hotels, rooms, guests, and reservations.

## Features

### 🏨 Hotel Management
- Add, edit, and delete hotels
- Store contact information and descriptions
- Search and sort hotel listings

### 🛏️ Room Management
- Manage room inventory with types and capacity
- Set pricing and availability status
- Link rooms to specific hotels
- Track room status (Available, Occupied, Maintenance, Out of Order)

### 👥 Guest Management
- Maintain guest profiles with contact details
- Store identification information
- Search and manage guest database

### 📅 Reservation System
- Create and manage bookings
- Check-in and check-out functionality
- Calculate costs automatically based on room rates
- Track reservation status (Pending, Confirmed, Checked In, Checked Out, Cancelled)

### 📊 Dashboard & Reporting
- Real-time statistics dashboard
- Current reservations overview
- Quick action buttons for common tasks

### 🔐 Authentication System
- User registration and login
- Protected administrative areas
- Session management

## Installation

### Prerequisites
- Python 3.6 or higher
- Web2py framework dependencies (pydal, yatl, rocket3)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/acm2017/pythonWeb2py.git
cd pythonWeb2py
```

2. Install dependencies:
```bash
pip install pydal yatl rocket3
```

3. Start the Web2py server:
```bash
python web2py.py -a admin -i 0.0.0.0 -p 8000 --no_gui
```

4. Access the application:
- Open your browser and go to `http://localhost:8000/hotel_admin`

## Usage

### First Time Setup
1. Register a new user account through the registration form
2. Login with your credentials to access administrative features

### Managing Hotels
- Navigate to "Hotels" section
- Use "Add Record" to create new hotels
- Edit existing hotels with detailed information

### Managing Rooms
- Go to "Rooms" section
- Add rooms and associate them with hotels
- Set room types, capacity, and pricing

### Creating Reservations
1. Navigate to "New Reservation"
2. Select hotel and available room
3. Choose or create guest profile
4. Set check-in and check-out dates
5. System automatically calculates total amount

### Check-in/Check-out Process
- Use dashboard to view current reservations
- Click "Check In" button for confirmed reservations
- Click "Check Out" button for checked-in guests
- Room status updates automatically

## Database Schema

### Tables
- **hotels**: Hotel information and contact details
- **rooms**: Room inventory with pricing and status
- **guests**: Guest profiles and contact information
- **reservations**: Booking details and status tracking
- **auth_user**: User authentication system

### Sample Data
The system includes pre-populated sample data:
- 2 sample hotels (Grand Plaza Hotel, Seaside Resort)
- 5 sample rooms with different types and pricing
- 2 sample guests with contact information
- 2 sample reservations for testing

## Technology Stack

- **Framework**: Web2py
- **Database**: SQLite (easily configurable for other databases)
- **Frontend**: Bootstrap 5, Font Awesome icons
- **Backend**: Python with MVC architecture
- **Authentication**: Web2py built-in auth system

## File Structure

```
applications/hotel_admin/
├── models/
│   ├── db.py              # Database models and table definitions
│   ├── menu.py            # Application menu configuration
│   └── sample_data.py     # Sample data population
├── controllers/
│   └── default.py         # Main controller with all functions
├── views/
│   ├── layout.html        # Main layout template
│   └── default/           # View templates for each function
└── static/               # Static files (CSS, JS, images)
```

## Contributing

This is a learning project. Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Use as a reference for Web2py development

## License

This project is for educational purposes. Feel free to use and modify as needed.

## Demo

The system includes a comprehensive dashboard with:
- Statistics overview
- Current reservations table
- Quick management actions
- Responsive design for mobile and desktop

For questions or support, please create an issue in the repository.