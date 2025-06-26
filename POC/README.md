# Data Pura Vida Proof of Concept

This project is a simplified and simulated proof of concept (PoC) for Data Pura Vida, demonstrating a secure national data ecosystem. It uses React for the frontend and Flask for the backend, simulating authentication, data queries, dataset access via a tripartite key system, dashboard visualization, and cost monitoring, all in a local environment.

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Backend Setup (Flask)](#backend-setup-flask)
  - [Frontend Setup (React)](#frontend-setup-react)
- [Running the Application](#running-the-application)
- [How It Works](#how-it-works)
  - [Backend (Flask)](#backend-flask)
  - [Frontend (React)](#frontend-react)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Overview

**Data Pura Vida** simulates a data ecosystem with the following features:

1. **Flask Backend**: An API server exposing protected endpoints for:
   - Simulated authentication (`/api/login`)
   - Data queries with Row-Level Security (RLS) (`/api/query`)
   - Dataset access using tripartite keys (`/api/access-dataset`, `/api/generate-shares`)
   - Simulated dashboard URLs (`/api/dashboard-url`)
   - Simulated cost monitoring (`/api/cost`)
2. **React Frontend**: A user interface for authentication, querying data, accessing datasets, viewing simulated dashboards, and monitoring costs, styled with a minimalist design (neutral colors, clean typography, ample whitespace).

Everything runs locally, using in-memory data and simulated authentication.

## Technologies

- **Backend**:
  - Flask: Python web framework
  - Flask-CORS: Cross-Origin Resource Sharing support
  - PyJWT: JWT generation and validation
  - python-json-logger: Structured console logging
  - Custom Shamir’s Secret Sharing implementation (no external dependencies)
- **Frontend**:
  - React: UI library
  - axios: HTTP client for API calls
  - CSS: Custom minimalist styling with Inter font (via Google Fonts)
- **Simulation**:
  - Authentication: Local JWTs instead of Okta
  - Storage: In-memory data instead of Snowflake/S3
  - Dashboards: Mock URLs and images instead of QuickSight
  - Costs: Mock data instead of AWS Cost Explorer
  - Logging: Console instead of CloudWatch

## Prerequisites

- Python 3.11 (for the backend)
- Node.js 18+ and npm (for the frontend)
- Basic knowledge of Flask and React

## Setup

### Backend Setup (Flask)

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>/backend

2. Create a Virtual Environment:

    ```bash
    python -m venv venv
    source venv/Scripts/Activate.ps1

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the Backend:

    ```bash
    python main.py

5. The Flask server runs on [http://localhost:5000] (or [http://192.168.1.79:5001] if the port was changed).

### Frontend Setup (React)

1. Navigate to the Frontend Directory:

    ```bash
    cd <repository-directory>/frontend

2. Install Dependencies:

    ```bash
    npm install

3. Run the Frontend:

    ```bash
    npm start

4. The React app will run on [http://localhost:3000].

### Running the Application

1. Start the Flask backend (python app.py).

2. Start the React frontend (npm start).

3. Open your browser to [http://localhost:3000].

### Use the interface to

1. Click Login to authenticate with Okta.

2. Click Llamar API Segura to call the protected backend endpoint.

3. Click Logout to sign out.

## How It Works

### Backend (Flask)

Exposes the following endpoints:

- **POST /api/login**: Authenticates users and returns a simulated JWT.
- **GET /api/secure-data**: Returns protected data, requiring a JWT.
- **POST /api/query**: Executes simulated queries with RLS based on roles.
- **POST /api/generate-shares/<dataset_id>**: Generates tripartite key shares.
- **POST /api/access-dataset/<dataset_id>**: Accesses datasets using key shares.
- **GET /api/dashboard-url/<dataset_id>**: Returns simulated dashboard URLs.
- **GET /api/cost**: Returns simulated cost data.

Features:

- Authentication: Uses local JWTs with mock users.
- Queries: Filters in-memory data with RLS based on roles.
- Tripartite Keys: Uses a custom Shamir’s Secret Sharing implementation for secure dataset access.
- Dashboards: Simulates QuickSight URLs.
- Costs: Generates mock cost data.
- Logging: Logs activities to the console.

### Frontend (React)

Provides a minimalist interface for:

- Login: Authentication with mock users (`user1@example.com`, `admin@example.com`) using a clean login form.
- Queries: Form to submit queries and view results, styled with clear typography.
- Dataset Access: Generates and enters tripartite key shares in a streamlined form.
- Dashboards: Displays simulated URLs and a placeholder image in a simple layout.
- Logout: Clears authentication state via a subtle navigation button.

The frontend uses a neutral color palette (white, grays, soft blue), the Inter font, and ample whitespace for a minimalist aesthetic.

## Usage

- Log In:
  - Use test credentials:
    - Email: `user1@example.com`, Password: password1 (Role: User)
    - Email: `admin@example.com`, Password: adminpass (Role: Admin)
- Query Data:
  - Enter a query (e.g., "SELECT *") and view results filtered by RLS.
- Access Dataset:
  - Generate shares for a dataset (e.g., dataset1) with a secret.
  - Enter two shares to unlock the dataset.
- View Dashboard:
  - Enter a dataset ID to get a simulated URL and mock image.
- Monitor Costs:
  - Access /api/cost from the backend (you can add a button in the frontend).
- Log Out:
  - Click "Log Out" to exit.

## Troubleshooting

- CORS Errors:
  - Verify that Flask-CORS allows `http://localhost:3000` in main.py.
- Token Errors:
  - Ensure test credentials are valid.
  - Check that JWT_SECRET is consistent (default: super-secret-key).
- Query Failure:
  - Queries are simulated; any text is valid, but results depend on the role.
- Tripartite Key Errors:
  - Ensure shares are generated for the same dataset ID.
  - Copy shares exactly as generated (format: x:yyyy...).
- Dependencies:
  - Recreate the virtual environment if you encounter issues with Flask dependencies.

  ``` powershell
  Remove-Item -Recurse -Force venv
  python -m venv venv
  source venv/Scripts/Activate.ps1
  pip install -r requirements.txt
  ```
