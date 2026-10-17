# Delivery Analytics Dashboard

A full-stack analytics dashboard for tracking delivery orders, revenue, and delivery performance using real database data.

## Live Demo

-Frontend:https://delivery-analytics-frontend.onrender.com/

- Backend API: https://delivery-analytics-dashboard.onrender.com/
- GitHub Repository: https://github.com/zoya-902/delivery-analytics-dashboard

## Overview

The Delivery Analytics Dashboard visualizes delivery-related business data through interactive charts and summary metrics. It uses a FastAPI backend to retrieve data from PostgreSQL and a JavaScript frontend to display analytics.

## Features

-Order Summary: Total orders, total revenue, and average delivery time.

- Order Status Analysis: Visualizes orders grouped by delivery status.
- City-wise Analysis: Compares order volumes and revenue across cities.
- Agent Performance: Displays the number of orders handled by delivery agents.
- Monthly Revenue Trends: Visualizes revenue across months.
- REST API: Supports CRUD operations for customers, agents, and orders.
- Data Validation and Error Handling: Uses Pydantic schemas and HTTP status codes to handle invalid requests and database constraint violations.

## Tech Stack

| Component          | Technologies          |
| ------------------ | --------------------- |
| Frontend           | HTML, CSS, JavaScript |
| Data Visualization | Chart.js              |
| Backend            | Python, FastAPI       |
| Database           | PostgreSQL            |
| ORM                | SQLAlchemy            |
| Validation         | Pydantic              |
| Deployment         | Render                |
| Database Hosting   | Supabase              |

## Architecture

text
User
|
v
Frontend (HTML, CSS, JavaScript)
|
| HTTP requests / Fetch API
v
FastAPI Backend (Render)
|
| SQLAlchemy / SQL queries
v
PostgreSQL Database (Supabase)
|
v
Analytics JSON Responses
|
v
Dashboard Metrics and Charts

## Analytics Endpoints

| Endpoint                     | Purpose                                          |
| ---------------------------- | ------------------------------------------------ |
| `/analytics/summary`         | Total orders, revenue, and average delivery time |
| `/analytics/status`          | Order count grouped by status                    |
| `/analytics/cities`          | Order count grouped by city                      |
| `/analytics/city-revenue`    | Revenue grouped by city                          |
| `/analytics/agents`          | Order counts and average delivery time by agent  |
| `/analytics/monthly-revenue` | Revenue grouped by month                         |

## CRUD Endpoints

The backend also provides operations for managing customers, agents, and orders, including creating, retrieving, updating, and deleting records.

Interactive API documentation is available at `/docs` on the deployed backend.

## Run Locally

### 1. Clone the repository

bash
git clone https://github.com/zoya-902/delivery-analytics-dashboard.git
cd delivery-analytics-dashboard

### 2. Create and activate a virtual environment

bash
python -m venv venv

Windows:

bash
venv\Scripts\activate

### 3. Install dependencies

bash
pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file in the project root and add your PostgreSQL connection string:
env
DATABASE_URL=your_postgresql_connection_string
Keep `.env` private and do not commit database credentials to GitHub.

### 5. Start the backend

bash
uvicorn main:app --reload

Open `http://127.0.0.1:8000/docs` to explore and test the API.

Configure the frontend to use the local backend when running locally. For the deployed version, it should use the Render backend URL.

## What I Learned

- Building REST APIs with FastAPI.
- Designing database interactions using SQLAlchemy and PostgreSQL.
- Writing SQL aggregation queries for business analytics.
- Validating API requests and handling database errors.
- Connecting a JavaScript frontend to a deployed backend.
- Configuring CORS and environment variables.
- Deploying a full-stack application and debugging production issues.

## Future Improvements

- Add date-range and city filters.
- Introduce pagination for large datasets.
- Add automated API tests.
- Improve dashboard responsiveness and loading states.
- Add authentication and role-based access control.
