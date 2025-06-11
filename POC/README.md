# React + Flask + Okta Authentication Example

This project demonstrates how to implement a secure web application using **React** for the frontend, **Flask** for the backend, and **Okta** for authentication. The backend exposes a protected API endpoint, and the frontend authenticates users via Okta, retrieves an access token, and uses it to call the secure API.

## Table of Contents
- [Overview](#overview)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Okta Configuration](#okta-configuration)
  - [Backend Setup (Flask)](#backend-setup-flask)
  - [Frontend Setup (React)](#frontend-setup-react)
- [Running the Application](#running-the-application)
- [How It Works](#how-it-works)
  - [Backend (Flask)](#backend-flask)
  - [Frontend (React)](#frontend-react)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This application consists of two main components:

1. **Flask Backend**: A Python-based API server that exposes a single protected endpoint (`/api/secure-data`). The endpoint requires a valid JWT (JSON Web Token) issued by Okta for access.
2. **React Frontend**: A simple React application that allows users to log in via Okta, obtain an access token, call the protected backend API, and log out.

Okta handles user authentication and issues JWTs, which are validated by the Flask backend to secure the API.

## Technologies

- **Backend**:
  - Flask: Web framework for Python
  - Flask-CORS: Handles Cross-Origin Resource Sharing
  - PyJWT: Validates JWTs
  - PyJWKClient: Fetches public keys from Okta for JWT verification
- **Frontend**:
  - React: JavaScript library for building user interfaces
  - @okta/okta-auth-js: Okta SDK for JavaScript
- **Authentication**:
  - Okta: Identity provider for user authentication and authorization

## Prerequisites

- Python 3.8+ (for the Flask backend)
- Node.js 16+ and npm (for the React frontend)
- An Okta developer account (free tier available at [developer.okta.com](https://developer.okta.com/))
- Basic knowledge of Flask, React, and OAuth 2.0

## Setup

### Okta Configuration

1. **Create an Okta Account**:
   - Sign up for a free Okta developer account at [developer.okta.com](https://developer.okta.com/).
2. **Create an Application**:
   - In the Okta Admin Console, go to **Applications > Create App Integration**.
   - Choose **OIDC - OpenID Connect** as the sign-in method and **Single-Page Application** as the application type.
   - Set the **Sign-in redirect URI** to `http://localhost:3000/login/callback` (or your frontend's URL).
   - Note the **Client ID** and **Okta Domain** (e.g., `dev-xxxxxxxx.us.okta.com`).
3. **Configure API Authorization**:
   - Go to **Security > API > Authorization Servers** and select the `default` server.
   - Under **Settings > Access Policies**, ensure the default policy allows access to your application.
   - Note the **Issuer URI** (e.g., `https://dev-xxxxxxxx.us.okta.com/oauth2/default`).
4. **Update Configuration**:
   - In the Flask backend (`app.py`), update the following:
     - `OKTA_DOMAIN`: Your Okta domain (e.g., `dev-w425j2q1a431gpdw.us.okta.com`).
     - `API_AUDIENCE`: Your Okta application's Client ID.
     - `OKTA_ISSUER`: Your authorization server's issuer URI.
   - In the React frontend (`App.js`), update the `oktaAuth` configuration:
     - `issuer`: Your Okta issuer URI.
     - `clientId`: Your Okta application's Client ID.
     - `redirectUri`: Your frontend's callback URL (e.g., `http://localhost:3000/login/callback`).

### Backend Setup (Flask)

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>/backend

2. Create a Virtual Environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

    ```bash
    pip install flask flask-cors pyjwt requests python-jose

4. Run the Backend:

    ```bash
    python app.py

5. The Flask server will run on http://localhost:5000.

### Frontend Setup (React)

1. Navigate to the Frontend Directory:

    ```bash
    cd <repository-directory>/frontend

2. Install Dependencies:

    ```bash
    npm install
    npm install @okta/okta-auth-js

3. Run the Frontend:

    ```bash
    npm start

4. The React app will run on http://localhost:3000.

### Running the Application

1. Start the Flask backend (python app.py).

2. Start the React frontend (npm start).

3. Open your browser to http://localhost:3000.

### Use the interface to

1. Click Login to authenticate with Okta.

2. Click Llamar API Segura to call the protected backend endpoint.

3. Click Logout to sign out.

## How It Works

### Backend (Flask)

The Flask app exposes a single endpoint: GET /api/secure-data.

The @token_required decorator validates incoming JWTs:
It extracts the Authorization: Bearer <token> header.

Fetches Okta's public keys from the JWKS endpoint (/v1/keys).

Verifies the token's signature, audience, issuer, and expiration.

Returns a 401 error for invalid or missing tokens.

If the token is valid, the endpoint returns a JSON response with protected data.

### Frontend (React)

The React app uses the @okta/okta-auth-js library to handle Okta authentication.

Login:
Opens a popup for Okta authentication.

Retrieves an access token and ID token, storing them in the Okta token manager.

Fetches user profile information (e.g., name, email).

Call Backend:
Sends a GET request to http://localhost:5000/api/secure-data with the access token in the Authorization header.

Displays the API response.

Logout:
Clears tokens and resets the app state.

## Usage

- Login: Click the "Login" button to authenticate via Okta. You'll see a popup for entering credentials.

- View Profile: After logging in, your name (from Okta's user profile) is displayed.

- Call API: Click "Llamar API Segura" to fetch data from the protected endpoint. The response is shown in JSON format.

- Logout: Click "Logout" to sign out and clear the session.

## Troubleshooting

- CORS Errors: Ensure the Flask backend allows CORS for http://localhost:3000. The CORS(app) line in app.py should handle this.

- Invalid Token Errors:
Verify that the API_AUDIENCE in app.py matches the Client ID.

Ensure the issuer in both frontend and backend matches Okta's issuer URI.

Check that the token hasn't expired (Okta tokens typically last 1 hour).

- Okta Login Fails:
Confirm the clientId and redirectUri in App.js match your Okta application settings.

Ensure your Okta application is configured for SPA and allows the required scopes (openid, profile, email).

- Backend Not Running: Ensure the Flask server is running on http://localhost:5000 before making API calls.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

### Instructions

1. Create a file named `README.md` in your project's root directory.
2. Copy and paste the content above into the file.
3. Replace `<repository-url>` and `<repository-directory>` with your actual repository URL and directory name.
4. If your project structure differs (e.g., backend and frontend are not in separate `backend/` and `frontend/` folders), update the paths in the setup instructions accordingly.
5. For security, ensure sensitive values like `OKTA_DOMAIN` and `API_AUDIENCE` are not hardcoded in production. Consider using environment variables and mention this in the README if applicable.

Let me know if you need help with additional sections, such as deployment instructions, or if
