# Django Online Learning Platform

This project is an online learning platform developed using Django, allowing users to view, create, and enroll in courses.

## Requirements

Install and Active virtual env
    '''

    python -m venv env
    env\Scripts\activate
    '''

- Python 
- Django
- Django Rest Framework
- MySQL Database Server
- mysqlclient package

## Installation

1. Install project dependencies:

    ```
    pip install -r requirements.txt
    ```

2. Configure MySQL Database:

    - Install MySQL on your system if not already installed.
    - Create a new database for the project.

3. Update Django settings:

    - Open `settings.py` in the `your_project` directory.
    - Update the `DATABASES` setting to use MySQL database:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_mysql_username',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',  # Or your MySQL host IP address
            'PORT': '3306',  # Default MySQL port
        }
    }
    ```

    Replace `'your_database_name'`, `'your_mysql_username'`, and `'your_mysql_password'` with your MySQL database name, username, and password respectively.

4. Apply migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

6. Access the project:

    Open a web browser and go to `http://localhost:8000` to access the Django admin panel or API endpoints.
    Or If you want you can use POSTMAN software for handle and test all API.

## API Endpoints

- **GET /courses**: Retrieve a list of available courses.
- **GET /courses/:id**: Retrieve a specific course by its ID.
- **POST /courses**: Create a new course.
- **POST /enrollments**: Allow students to enroll in a course.

## Usage

- Visit the `/courses` endpoint to view available courses.
- Use the `/enrollments/` endpoint to enroll students in courses.