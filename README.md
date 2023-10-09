# Authentication 

This is a simple authentication application built using FastAPI, and the Singleton design pattern. It allows users to register, log in, and view their own profile information.

## Features

- User registration with email and password.
- User login with email and password.
- JWT (JSON Web Token) authentication.
- Protected route to view user profile information.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/niluws/authentication.git
   ```

2. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

The application should now be running at http://localhost:8000.

## Usage

### Register a User

To register a new user, make a POST request to `/register/` with the user's full name, email, and password in the request body:

```http
POST /register/

{
    "full_name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
}
```

### Login

To log in, make a POST request to `/login/` with the user's email and password in the request body:

```http
POST /login/

{
    "email": "john@example.com",
    "password": "securepassword"
}
```

Upon successful login, you will receive an access token and a refresh token.

### View User Profile

To view the user's profile, make a GET request to `/me/` with the access token included in the `Authorization` header:

```http
GET /me/
Authorization: Bearer <access_token>
```

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [MongoDB](https://www.mongodb.com/)
- [JSON Web Tokens (JWT)](https://jwt.io/)
