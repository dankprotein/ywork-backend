# Ywork Backend Internship Assignment

This repository contains a Django REST Framework (DRF) based backend solution for the Ywork.ai internship assignment. It includes:

- Google OAuth 2.0 authentication flow
- Secure data entry and retrieval APIs
- Sample model implementation with user linkage

---

## Project Structure

ywork-backend/
├── accounts/ # OAuth views and URL routing
├── api/ # DRF model, views, serializers
├── ywork_backend/ # Project settings and root config
├── .env.template # Environment variable template
├── requirements.txt # Required Python packages
├── README.md # Project documentation


---

## Features

**Google OAuth 2.0 Integration**
- Obtain access and refresh tokens using Google login
- Implemented via `GET /auth/google/` and `GET /auth/callback/`

**Protected Data APIs**
- Model: `Item` with fields `title`, `description`, and linked `user`
- Create entry via `POST /api/items/`
- Search entries via `GET /api/items/?title=...`
- Endpoints require authentication

---

## Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/dankprotein/ywork-backend.git
cd ywork-backend

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate    # For Windows

3. Install dependencies

pip install -r requirements.txt


4. Configure environment variables
Create a .env file using the provided template:

cp .env.template .env


Fill in your Google OAuth Client ID, Secret, and Redirect URI.

5. Apply migrations
python manage.py makemigrations
python manage.py migrate

6. Run the development server
python manage.py runserver

API Documentation
Authentication
GET /auth/google/
Returns a Google login URL for user authorization.

GET /auth/callback/?code=...
Exchanges the authorization code for access and refresh tokens.

Item API (Authenticated)
POST /api/items/
Creates a new item linked to the logged-in user.

GET /api/items/?title=foo
Lists user’s items filtered by title if provided.

Admin Panel
To access the Django admin:

1. Create a superuser:
python manage.py createsuperuser

2. Navigate to:
http://localhost:8000/admin/

Environment Variable Template
The .env.template file contains:

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/


Notes
This application is designed for local development and internship evaluation purposes.

.env is excluded from version control to protect sensitive credentials.

Use Postman to test the OAuth 2.0 flow and API endpoints.

Author
This project was developed by Tushar as part of the AI + Backend Developer Internship application for Ywork.ai.

