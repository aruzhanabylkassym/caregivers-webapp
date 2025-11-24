# CSCI 341 Assignment 3 - Part 3 Report

## Flask Setup
The project is structured as a standard Flask application:
- `app.py`: The main application file containing all routes and logic.
- `templates/`: Directory containing HTML templates for the UI.
- `requirements.txt`: List of dependencies (`Flask`, `psycopg2`).

The application uses `Flask` for the web framework and `psycopg2` for PostgreSQL database interaction. Bootstrap 5 is used for a responsive and clean UI.

## Database Connection
The database connection is managed via the `get_db_connection()` function in `app.py`. It uses `psycopg2` to connect to the PostgreSQL database using the provided credentials.
- **Host**: localhost
- **Database**: caregivers_db
- **User**: postgres
- **Password**: Aruka5645 (as per draft code)

The connection is established for each request and closed in a `finally` block to ensure resource cleanup.

## CRUD Implementation
Full CRUD (Create, Read, Update, Delete) operations are implemented for all 7 entities:
1.  **USER**: Manage app users.
2.  **CAREGIVER**: Manage caregivers (linked to users). Includes search by type and city.
3.  **MEMBER**: Manage members (linked to users).
4.  **ADDRESS**: Manage addresses for members.
5.  **JOB**: Manage jobs posted by members. Includes viewing applicants for each job.
6.  **JOB_APPLICATION**: Manage applications by caregivers for jobs.
7.  **APPOINTMENT**: Manage appointments between caregivers and members. Includes a confirmation feature.

Each entity has:
- A list view (Read)
- A creation form (Create)
- A edit form (Update)
- A delete action (Delete)

## Extra Features
- **Search Caregivers**: Filter caregivers by caregiving type and city.
- **List Applicants**: View all applicants for a specific job.
- **Appointment Confirmation**: One-click confirmation for pending appointments.
- **Better UI**: Enhanced with Bootstrap 5.

## Deployment on PythonAnywhere
To deploy this application on PythonAnywhere:

1.  **Create an Account**: Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/).
2.  **Upload Files**: Upload the contents of `part3/` to your PythonAnywhere file storage.
3.  **Install Dependencies**: Open a Bash console and run:
    ```bash
    pip3 install --user flask psycopg2-binary
    ```
4.  **Database Setup**:
    - Go to the "Databases" tab.
    - Initialize a PostgreSQL database (if available on your plan) or use the provided MySQL (requires changing `psycopg2` to `mysql-connector` and adjusting SQL syntax slightly). *Note: This project is built for PostgreSQL.*
    - If using PostgreSQL, use the "Postgres console" to run the content of `schema.sql` and `data.sql`.
5.  **Web App Setup**:
    - Go to the "Web" tab.
    - Add a new web app.
    - Select "Flask" and the correct Python version.
    - Point the "Source code" and "Working directory" to your uploaded folder.
    - Edit the WSGI configuration file to import your app:
        ```python
        import sys
        path = '/home/yourusername/mysite'
        if path not in sys.path:
            sys.path.append(path)
        from app import app as application
        ```
6.  **Reload**: Reload the web app and visit your URL.

**Deployment Link**: [Insert your PythonAnywhere URL here]
