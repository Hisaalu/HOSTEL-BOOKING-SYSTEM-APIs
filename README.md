# HOSTEL-BOOKING-SYSTEM-APIs

Welcome to the HOSTEL-BOOKING-SYSTEM-APIs project! This project provides a RESTful API for managing hostel room bookings. Users can find available rooms in a hostel and book them using the API.

Hosted services: https://hostelapi-lucovklodq-ew.a.run.app

## Features

- **Room Find**: Users can find available rooms in a hostel using room number, category, description, price and hostel
- **Room Booking**: Users can book available rooms by providing booking details such as their names, contact, and email, the sytem will display the rooms available for them to choose.
- **User Authentication**: Secure endpoints with user authentication using JSON Web Tokens (JWT) for access control.
- **Admin Dashboard**: Admin users have access to an admin dashboard for managing rooms, bookings, and user accounts.

## Technologies Used

- **Django**: Backend web framework for building the API endpoints and handling business logic.
- **Django Rest Framework (DRF)**: Toolkit for building RESTful APIs in Django.
- **Docker**: Containerization platform used for packaging the application and dependencies.
- **Google Cloud Platform (GCP)**: Cloud platform used for hosting the API.

## Setup Instructions

To run the HOSTEL-BOOKING-SYSTEM-APIs project locally, follow these steps:

1. Clone the repository: git clone https://github.com/yourusername/HOSTEL-BOOKING-SYSTEM-APIs.git

2. Navigate to the project directory: cd HOSTEL-BOOKING-SYSTEM-APIs

3. Install the dependencies using pip: pip install -r requirements.txt

4. Run migrations to create the database schema: python manage.py makemigrations

5. Push the migrations into tables: python manage.py migrate

6. Run server: python manage.py runserver
