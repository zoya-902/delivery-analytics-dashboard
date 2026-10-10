# Delivery Analytics Dashboard

A full-stack application that manages customers, delivery agents, and orders, and provides delivery insights through REST APIs and an interactive web dashboard.

## Tech Stack

- Backend: Python, FastAPI, SQLAlchemy, Pydantic
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Data Visualization: Chart.js
- Configuration: Environment variables using `python-dotenv`

## Features

- CRUD operations for customers, delivery agents, and orders
- Pydantic schemas for request validation and response serialization
- PostgreSQL database with foreign-key relationships
- PUT endpoints for updating customer and agent details
- PATCH endpoint for partially updating order details
- HTTP error handling for missing resources, database constraint violations, and deletion conflicts
- Customer-wise and agent-wise order retrieval
- SQL-based analytics for:
  - Total orders, total revenue, and average delivery time
  - Order counts by status
  - City-wise order counts
  - City-wise revenue
  - Agent performance and average delivery time
  - Monthly revenue

- Interactive dashboard with KPI cards and charts
- Frontend error messages when API requests fail
- Environment-based database configuration to keep credentials out of source code

## Project Structure

text
delivery_analytics/
├── .gitignore
├── .env
├── requirements.txt
├── generate_data.py
├── main.py
├── models.py
├── schemas.py
├── README.md
├── data/
│ ├── customer.csv
│ ├── agent.csv
│ └── order.csv
└── frontend/
├── index.html
├── style.css
└── script.js

Ensure the filenames match your actual project. Do not upload `.env` to GitHub.

## Setup and Installation

### 1. Create the PostgreSQL database

Create a PostgreSQL database named `delivery_analytics`.

### 2. Configure environment variables

Create a `.env` file in the project root:

text
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/delivery_analytics

Replace `YOUR_PASSWORD` with your PostgreSQL password.

The application loads this value using `python-dotenv`. Keep `.env` in `.gitignore` and never commit database credentials.

### 3. Install dependencies

Activate your Python virtual environment and install the packages:

bash
pip install -r requirements.txt

Ensure `requirements.txt` includes the packages used by the project, such as FastAPI, Uvicorn, SQLAlchemy, `psycopg2-binary`, and `python-dotenv`.

### 4. Start the backend

From the project root, run:

bash
python -m uvicorn main:app --reload

API base URL: http://127.0.0.1:8000
Interactive API documentation: http://127.0.0.1:8000/docs

The application creates missing tables through SQLAlchemy metadata. Ensure the database contains the sample data required for analytics.

### 5. Start the frontend

Open `frontend/index.html` using VS Code Live Server.

If Live Server runs at `http://127.0.0.1:5500`, the backend CORS configuration must allow that origin. The frontend retrieves analytics data from the local FastAPI application.

### 6. Prepare sample data

Use the provided CSV files and `generate_data.py` according to the data-generation workflow implemented in your project. Ensure customer, agent, and order records are loaded into PostgreSQL before checking analytics.

## API Endpoints

### Customers

| Method | Endpoint                         | Description                  |
| ------ | -------------------------------- | ---------------------------- |
| GET    | `/customer`                      | List all customers           |
| GET    | `/customer/{id}`                 | Retrieve a customer          |
| POST   | `/customer`                      | Create a customer            |
| PUT    | `/customer/{customer_id}`        | Update customer details      |
| DELETE | `/customer/{customer_id}`        | Delete a customer            |
| GET    | `/customer/{customer_id}/orders` | Retrieve a customer's orders |

### Delivery Agents

| Method | Endpoint                   | Description                |
| ------ | -------------------------- | -------------------------- |
| GET    | `/agent`                   | List all agents            |
| GET    | `/agent/{agent_id}`        | Retrieve an agent          |
| POST   | `/agent`                   | Create an agent            |
| PUT    | `/agent/{agent_id}`        | Update agent details       |
| DELETE | `/agent/{agent_id}`        | Delete an agent            |
| GET    | `/agent/{agent_id}/orders` | Retrieve an agent's orders |

### Orders

| Method | Endpoint            | Description               |
| ------ | ------------------- | ------------------------- |
| GET    | `/order`            | List all orders           |
| GET    | `/order/{order_id}` | Retrieve an order         |
| POST   | `/order`            | Create an order           |
| PATCH  | `/order/{order_id}` | Partially update an order |
| DELETE | `/order/{order_id}` | Delete an order           |

### Analytics

| Method | Endpoint                     | Description                                  |
| ------ | ---------------------------- | -------------------------------------------- |
| GET    | `/analytics/summary`         | Summary KPIs                                 |
| GET    | `/analytics/status`          | Order counts by status                       |
| GET    | `/analytics/cities`          | City-wise order counts                       |
| GET    | `/analytics/city-revenue`    | Revenue by city                              |
| GET    | `/analytics/agents`          | Agent order counts and average delivery time |
| GET    | `/analytics/monthly-revenue` | Monthly revenue                              |

## Testing

The application can be tested using FastAPI's interactive documentation at `/docs`.

Recommended manual checks:

1. Test CRUD endpoints with valid input.
2. Request a nonexistent resource and verify the `404` response.
3. Submit invalid data and verify Pydantic validation responses where applicable.
4. Try creating an order with invalid foreign-key references and verify database constraint handling.
5. Attempt to delete a customer or agent linked to existing orders and verify the conflict response.
6. Test customer-wise and agent-wise order retrieval.
7. Verify that all analytics endpoints return the expected JSON.
8. Open the frontend and verify that KPI cards and charts display database data.
9. Stop the backend temporarily and check the frontend's API-failure message.

## Security Notes

- Store database credentials in `.env`, not directly in Python source code.
- Keep `.env` excluded through `.gitignore`.
- Do not commit passwords, secrets, or local virtual environment files to GitHub.

## Project Status

The project is configured for local development. Public deployment requires separate hosting and configuration.
