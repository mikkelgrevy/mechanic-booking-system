# AutoEl-Teknik Booking System

Flask-based booking management system for a car repair workshop with time slot scheduling and secure admin panel.

![Project Screenshots](screenshots/)

## Project Overview

Web application built for managing customer bookings at a car repair shop. Features include real-time availability checking, time slot management, and a secure admin interface with two-factor authentication.

## Features

### Customer Features
- Browse available time slots for the next 5 days
- Book appointments with contact information
- Responsive design for mobile and desktop
- Real-time slot availability
- Booking confirmation system

### Admin Features
- Secure login with password protection
- Two-factor authentication (TOTP)
- View all bookings with date/time details
- Overview of available time slots
- Session timeout for security (10 minutes)

### Technical Features
- SQLite database for persistent storage
- Session management with automatic expiration
- QR code generation for 2FA setup
- Flash messaging for user feedback
- Clean separation of routes and logic

##  Tech Stack

**Backend:**
- Python 3.x
- Flask (web framework)
- SQLAlchemy (ORM)
- PyOTP (2FA authentication)

**Frontend:**
- HTML5/CSS3
- Bootstrap 5 (responsive design)
- Jinja2 templating

**Security:**
- TOTP-based two-factor authentication
- Session management with timeouts
- QR code-based authenticator app integration

**Database:**
- SQLite

## Project Structure
```
mechanic/
├── app.py                 # Main application logic
├── secret.py              # Secret keys (not in repo)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar
│   ├── index.html        # Homepage
│   ├── booking.html      # Customer booking form
│   ├── admin_login.html  # Admin authentication
│   ├── admin_2fa.html    # 2FA verification
│   └── booking_admin.html # Admin dashboard
├── static/               # Static assets (CSS, images, videos)
└── screenshots/          # Project screenshots
```

##  Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/mikkelgrevy/mechanic-booking-system.git
cd mechanic-booking-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure secrets**

Create a `secret.py` file in the root directory:
```python
# secret.py
app_pass = "your-secret-key-here"
admin_pass = "your-admin-password"
totp_pass = "your-totp-secret"  # Generate with: pyotp.random_base32()
```

4. **Initialize the database**
```bash
python app.py
```
The database will be created automatically on first run.

5. **Setup 2FA (first time only)**

Navigate to `/admin_2fa_setup` to generate a QR code for your authenticator app.

6. **Access the application**
- Customer interface: `http://localhost:5000`
- Admin login: `http://localhost:5000/admin_login`

## 📸 Screenshots

### Customer Booking Interface
![Booking Page](screenshots/booking.png)

### Admin Dashboard
![Admin Panel](screenshots/admin.png)

##  Security Features

- **Two-Factor Authentication:** Admin access requires both password and TOTP code
- **Session Management:** Automatic logout after 10 minutes of inactivity
- **Secure Secrets:** Sensitive data stored in non-committed `secret.py` file
- **Input Validation:** Form data validated before database insertion

##  Key Learnings

This project was developed as part of my IT-Technology studies at KEA. Through building it, I gained hands-on experience with:

- **Full-stack development:** Integrating frontend, backend, and database
- **Database design:** SQLAlchemy ORM and relational data modeling
- **Authentication:** Implementing TOTP-based 2FA from scratch
- **User experience:** Creating intuitive booking flows
- **Security best practices:** Session management, secret handling, input validation

##  Features in Detail

### Time Slot Management
- Generates hourly slots from 08:00 to 16:00
- Automatically marks booked slots as unavailable
- Shows only next 5 business days
- Prevents double-booking

### Admin Authentication Flow
1. Password authentication
2. TOTP code verification (6-digit code from authenticator app)
3. Time-limited session (10 minutes)

### Database Schema
```sql
Booking
├── id (Primary Key)
├── name (String, 100)
├── email (String, 100)
├── nummerplade (String, 7)  -- License plate
├── telefon (String, 11)      -- Phone number
├── timeslot (String, 20)
└── date (Date)
```

##  Known Limitations

- Single-shop setup (not multi-location)
- No email notifications for bookings
- Manual booking deletion (no customer cancellation interface)
- Danish language only in templates

##  Future Improvements

- [ ] Email confirmation system
- [ ] Customer cancellation interface
- [ ] Multi-language support
- [ ] Calendar view for admin
- [ ] SMS notifications
- [ ] Recurring booking management

##  Project Context

**Type:** School project (IT-Technology, KEA)  
**Team Size:** Group project, solo development  
**Duration:** 2-3 weeks  
**Role:** Primary developer - responsible for all backend logic, database design, authentication system, and frontend integration

##  License

This project is for educational purposes. Feel free to use it as inspiration for learning.

##  Author

**Mikkel Grevy**  
IT-Technology Student at KEA  
- Email: mmgrevy@gmail.com
- GitHub: [@mikkelgrevy](https://github.com/mikkelgrevy)