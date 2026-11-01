# The Grand Address

## Project Overview

The Grand Address is a Django-based property booking website that allows visitors to explore available accommodation, view property details and submit booking requests.

The platform provides an interface for managing properties and reservations through Django's administration dashboard.

## Features

- Homepage displaying featured properties.
- Property listings retrieved dynamically from the database.
- Individual property details pages.
- Property availability management.
- Customer booking forms with validation.
- Booking confirmation page with booking reference.
- Contact form for customer enquiries.
- User registration and login.
- User dashboard and saved properties.
- Django Admin for managing properties, bookings and contact messages.

## Technologies Used

- **Backend:** Python and Django
- **Frontend:** HTML, CSS and JavaScript
- **Database:** MySQL
- **Image Management:** Django Media Files
- **Development Environment:** Visual Studio Code

## Project Structure

```text
Airbnb/
│
├── accounts/
├── bookings/
├── Airbnb/
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

## Installation and Setup

### 1. Clone or download the project

Download the project source code to your computer.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

For macOS and Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the MySQL database

Create a MySQL database for the project.

Update the `DATABASES` configuration in `Airbnb/settings.py` with your local MySQL database name, username, password and connection details.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Django Administration

The administration dashboard is available at:

http://127.0.0.1:8000/admin/

Administrators can:

- Add, edit and delete properties.
- Manage property availability.
- View customer bookings.
- Update booking statuses.
- View customer contact messages.

## Booking Workflow

1. Visitors explore available properties.
2. Visitors select a property to view its details.
3. Visitors complete the booking form.
4. Django validates the submitted information.
5. Valid bookings are saved to the MySQL database.
6. Visitors receive a booking confirmation with a reference number.
7. Administrators manage bookings through Django Admin.

## Developer

The Grand Address was developed as a Django web development project.
