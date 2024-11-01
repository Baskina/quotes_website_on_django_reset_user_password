# Quotes Management Application

## Project Overview
This Django application is designed to manage authors and quotes, allowing registered users to add new authors and quotes. Public users can browse all authors and quotes without authentication, while certain features require users to register and log in. The project is set up with PostgreSQL for user data and MongoDB for managing quotes and authors, offering flexibility in database configuration.

## Key Features
- **User Registration and Authentication**:
    - Users can register and log in to the site.
    - Only registered users can add new authors and quotes.
- **Author Management**:
    - Registered users can add new authors to the site.
    - Any user can view author details without logging in.
- **Quote Management**:
    - Registered users can add new quotes associated with an author.
    - All quotes are accessible for viewing without user authentication.
- **Database Migration**:
    - The application allows for migration from an existing MongoDB database to PostgreSQL, especially for user data.
    - Quotes and authors can remain in MongoDB, while user data can be managed in PostgreSQL.
    - A custom script is provided for database migration, ensuring smooth transition and data integrity.

## Technologies Used
- **Django**: The main web framework used for developing the application.
- **MongoDB**: Database for storing quotes and author data.
- **PostgreSQL**: Database for managing user data.
- **Django ORM**: Object Relational Mapper for PostgreSQL.
- **Custom Migration Script**: Used for migrating data from MongoDB to PostgreSQL as needed.

## Installation

### Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

### Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### Set up the PostgreSQL database:
1. Ensure PostgreSQL is installed and running.
2. Create a new PostgreSQL database and user if necessary.

### Apply Django migrations:
```bash
python manage.py migrate
```

### Run the custom migration script (optional):
To migrate data from MongoDB to PostgreSQL, execute the custom migration script:
```bash
python manage.py runscript migrate_mongo_to_postgres
```

### Start the Django development server:
```bash
python manage.py runserver
```

## Usage

### User Registration and Login
- Access the registration and login forms to create an account and log in.

### Adding Authors and Quotes
- Only registered users can access forms to add authors and quotes.
- Both authors and quotes are publicly accessible, so any user can browse them without logging in.

### API Endpoints (if applicable)
- **Authors**: `/authors/`
    - View all authors.
    - Registered users can add new authors.
- **Quotes**: `/quotes/`
    - View all quotes.
    - Registered users can add new quotes associated with an author.

## General Requirements
- All database credentials and sensitive information should be stored in the `.env` file.
- The application supports two databases (PostgreSQL and MongoDB), and a custom migration script is available for transitioning data from MongoDB to PostgreSQL.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
