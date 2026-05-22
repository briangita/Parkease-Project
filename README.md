Admin
Username-abgita
Password: Asante@26

service attendant
Username- smirembe
password- Mirembe@26found

username-akizito
password - Namiiro@26

Parking attendant 
username - bmusoki
Password -brenda


# ParkEase – Integrated Parking & Vehicle Services Management System

## Project Overview

ParkEase is a web-based management system developed using Django to help parking facilities digitize and automate their daily operations. The system supports vehicle parking management, tyre clinic services, and battery hire/sales management in one centralized platform.

The project improves record keeping, automates parking charge calculations, generates receipts, supports role-based access control, and provides reporting features for administrators.

---

# Business Modules

## 1. Parking Management System

The Parking Management module is the core module of ParkEase.

### Features

- Vehicle registration on arrival
- Automatic receipt generation
- Parking charge calculation
- Vehicle sign-out management
- Daily parking reports
- Parking receipt printing
- Vehicle tracking

### Captured Information

- Driver name
- Vehicle type
- Number plate
- Vehicle model
- Vehicle color
- Phone number
- NIN number (for boda-bodas)
- Arrival time
- Exit time
- Parking fee

### Parking Charges

| Vehicle Type | Day | Night | Less Than 3 Hours |
|---|---|---|---|
| Truck | UGX 5,000 | UGX 10,000 | UGX 2,000 |
| Personal Car | UGX 3,000 | UGX 2,000 | UGX 2,000 |
| Taxi | UGX 3,000 | UGX 2,000 | UGX 2,000 |
| Coaster | UGX 4,000 | UGX 2,000 | UGX 3,000 |
| Boda-boda | UGX 2,000 | UGX 2,000 | UGX 1,000 |

### Sign-Out Features

- Receiver name
- Receiver phone number
- Receiver gender
- Receiver NIN
- Exit date and time
- Receipt verification

---

# 2. Tyre Clinic Management

The Tyre Clinic module manages tyre-related services provided within the parking facility.

### Features

- Record tyre service transactions
- Manage tyre service pricing
- Generate service receipts
- Service reporting
- Dashboard summaries

### Supported Services

- Pressure
- Puncture fixing
- Valve replacement
- Tyre replacement
- Wheel balancing

### Captured Information

- Customer name
- Number plate
- Phone number
- Tyre size
- Tyre model
- Service type
- Service fee
- Service date and time

---

# 3. Battery Hire & Sales Management

The Battery module manages battery hiring and battery sales operations.

### Features

- Battery hire recording
- Battery sales management
- Service fee management
- Battery transaction reports
- Dashboard summaries

### Captured Information

- Customer name
- Phone number
- Number plate
- Battery type
- Service type
- Service fee
- Transaction date and time

---

# User Roles & Permissions

## 1. Parking Attendant

### Permissions

- Register vehicles
- Issue parking receipts
- Sign out vehicles
- View parking records

---

## 2. Section Manager

### Permissions

- Manage tyre services
- Manage battery services
- Record service transactions
- Set service prices
- View service records

---

## 3. System Admin

### Permissions

- Register users
- Approve user accounts
- View reports
- Delete records
- Manage all system modules
- Access Django admin panel

---

# Authentication & Security

The system uses Django Authentication and Role-Based Access Control (RBAC).

### Features

- Login system
- Logout system
- User registration
- Admin approval for accounts
- Protected pages using `@login_required`
- Role-based navigation menus
- Restricted access to admin features

---

# Validation Rules

The system validates data on both frontend and backend.

### Validation Includes

- Names must start with a capital letter
- Names cannot contain numbers
- Number plates must:
  - start with `U`
  - be alphanumeric
  - be less than 6 characters
- Ugandan phone number validation
- NIN validation
- Required field validation

---

# Technologies Used

## Backend

- Python
- Django

## Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript

## Database

- SQLite

## Version Control

- Git
- GitHub

---

# Project Structure

```text
parkease/
│
├── parking/
├── tyres/
├── battery/
├── users/
│
├── templates/
│   ├── base.html
│   ├── navs.html
│   └── registration/
│
├── manage.py
│
└── parkeaseproject/
    ├── settings.py
    ├── urls.py
    └── wsgi.py

## Installation Guide

1. Clone the project repository from GitHub.

2. Create and activate a virtual environment.

3. Install project dependencies.

4. Run database migrations.

5. Create a superuser account for system administration.

6. Start the Django development server.

---

## Future Improvements

- Dashboard analytics and charts
- SMS and email notifications
- Online payment integration
- QR code receipt generation
- PDF and Excel report exports
- Mobile responsive enhancements
- AI-powered parking analytics
- Cloud database deployment

---

# Authors

Sarah Mirembe
Angella Kizito Namiiro
Brendalyn Musoki
Brian Gita Asiimwe

---

sample logins 
Admin
Username-abgita
Password: Asante@26

service attendant
Username- smirembe
password- Mirembe@26found

username-akizito
password - Namiiro@26

Parking attendant 
username - bmusoki
Password -brenda

# License

2026 May This project is developed for educational and academic purposes.
