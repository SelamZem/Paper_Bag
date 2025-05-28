# Paper Bag E-commerce Application

A Flask-based RESTful API for an e-commerce platform specializing in paper bags. This application provides endpoints for managing products, categories, users, shopping carts, orders, and payments.

## Features

- **Product Management**: CRUD operations for paper bags with categories
- **User Authentication**: User registration and authentication
- **Shopping Cart**: Users can add/remove items to/from their cart
- **Order Processing**: Create and track orders
- **Admin Dashboard**: Manage products, categories, and view orders and payements

## Tech Stack

- **Backend**: Python 3.x, Flask
- **Database**: SQLAlchemy ORM with SQLite (can be configured for other databases)
- **API Documentation**: Flasgger (Swagger UI)
- **Authentication**: JWT (JSON Web Tokens)


## Project Structure

```
Paper_Bag/
├── app/                      # Main application package
│   ├── controllers/          # Request handlers
│   ├── models/               # Database models
│   ├── repositories/         # Database operations
│   ├── schemas/              # Marshmallow schemas for serialization
│   ├── services/             # Business logic
│   ├── __init__.py           # Application factory
│   └── utils.py              # Utility functions
├── migrations/               # Database migrations
├── .env                      # Environment variables
├── config.py                 # Configuration settings
├── requirements.txt          # Project dependencies
├── run.py                    # Application entry point
└── seed.py                   # Database seeding script
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Paper_Bag
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
 venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///paperbag.db
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   python seed.py  # Optional: Seed the database with sample data
   ```

### Running the Application

```bash
python run.py
```

The API will be available at `http://localhost:5000`

## API Documentation

Once the application is running, you can access the interactive API documentation at:
- `http://localhost:5000/apidocs`


