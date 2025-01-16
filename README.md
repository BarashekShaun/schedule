# Schedule API

A RESTful API for managing events and organizations. Built with Django Rest Framework and secured with JWT authentication.

## Features
- View, create, and manage events and organizations.
- JWT-based user authentication and authorization.
- API supports sorting and filtering (e.g., `?ordering=-date&date_after=2024-03-11`).
- Includes Docker support for easy deployment.

## Data Models
### Organization
Fields:
- **title**: Organization name (unique, max length: 30).
- **description**: Detailed description (max length: 250).
- **address**: Address of the organization (max length: 90).
- **postcode**: Postal code (positive integer).

### Event
Fields:
- **title**: Event name (max length: 60).
- **description**: Event details (max length: 250).
- **organizations**: Associated organizations (many-to-many relationship).
- **image**: Optional event image (stored with a timestamped path).
- **date**: Event date (required).

### User (AdvUser)
Fields:
- **organization**: Foreign key to Organization.
- **email**: User email (unique).
- **phone**: User phone number (validated format).

## Quick Start

### Prerequisites
- Docker and Docker Compose installed.
- Python 3.9+ (if running locally without Docker).

### Run with Docker
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd schedule
   ```
2. Build and run the application:
   ```bash
   docker-compose build
   docker-compose up -d
   ```
3. Access the API at:
   ```
   http://localhost:8000/api/
   ```

### Run Locally
1. Clone the repository and set up a virtual environment:
   ```bash
   git clone <repository_url>
   cd schedule
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the API at:
   ```
   http://127.0.0.1:8000/api/
   ```

## API Endpoints

### Events
- **Get all events**:
  ```
  GET /api/events/
  Authorization: Bearer <your_token>
  ```
- **Create a new event**:
  ```
  POST /api/events/add/
  Body:
  {
      "title": "New Event",
      "description": "Detailed description of the event",
      "date": "2025-01-20",
      "organizations": [1, 2]  # List of organization IDs
  }
  ```
- **Get event details**:
  ```
  GET /api/events/<int:pk>/
  ```

### Organizations
- **Create a new organization**:
  ```
  POST /api/organizations/add/
  Body:
  {
      "title": "Organization Name",
      "description": "Description of the organization",
      "address": "123 Main Street",
      "postcode": 12345
  }
  ```

### JWT Authentication
- Obtain token:
  ```
  POST /api/token/
  Body:
  {
      "email": "user@example.com",
      "password": "your_password"
  }
  ```
- Refresh token:
  ```
  POST /api/token/refresh/
  Body:
  {
      "refresh": "your_refresh_token"
  }
  ```
- Verify token:
  ```
  POST /api/token/verify/
  Body:
  {
      "token": "your_access_token"
  }
  ```

## Running Tests
Run all tests with the following command:
```bash
python manage.py test
```

## Built With
- Django 3.2
- Django Rest Framework
- SimpleJWT for authentication
- Docker & Docker Compose

## Future Improvements
- Add Swagger or ReDoc for API documentation.
- Implement more detailed logging and error handling.
- Add unit tests to cover more cases.

---
