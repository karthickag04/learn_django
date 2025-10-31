# School App - Django Project

## Project Overview
This is a Django-based school management application that includes modules for managing students, teachers, admin panel, and user authentication.

## Project Structure

```
schoolapp/
├── .vscode/                          # VS Code configuration
│   └── settings.json                 # VS Code settings
├── adminpanel/                       # Admin panel Django app
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Database models
│   ├── tests.py                      # Unit tests
│   ├── views.py                      # View functions
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── __pycache__/             # Compiled Python files
│   └── __pycache__/                 # Compiled Python files
├── schoolapp/                        # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py                       # ASGI configuration
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # URL routing
│   ├── wsgi.py                       # WSGI configuration
│   ├── static/                       # Static files (empty)
│   ├── templates/                    # Templates (empty)
│   └── __pycache__/                 # Compiled Python files
├── static/                           # Global static files
│   ├── css/                          # Stylesheets
│   │   ├── index.css
│   │   └── main.css
│   ├── images/                       # Image assets
│   │   └── web-logo.png
│   └── js/                           # JavaScript files (empty)
├── students/                         # Students Django app
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Student models
│   ├── tests.py                      # Unit tests
│   ├── urls.py                       # URL patterns
│   ├── views.py                      # View functions
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── __pycache__/             # Compiled Python files
│   ├── templates/                    # Student templates
│   │   └── students/
│   │       ├── base.html             # Base template
│   │       └── index.html            # Student index page
│   └── __pycache__/                 # Compiled Python files
├── teachers/                         # Teachers Django app
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Teacher models
│   ├── tests.py                      # Unit tests
│   ├── views.py                      # View functions
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── __pycache__/             # Compiled Python files
│   ├── templates/                    # Teacher templates
│   │   └── teachers/
│   │       ├── base.html             # Base template
│   │       └── index.html            # Teacher index page
│   └── __pycache__/                 # Compiled Python files
├── templates/                        # Global templates
│   ├── index.html                    # Main index page
│   └── master.html                   # Master template
├── users/                            # User authentication Django app
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── forms.py                      # User forms
│   ├── models.py                     # User models
│   ├── tests.py                      # Unit tests
│   ├── urls.py                       # URL patterns
│   ├── views.py                      # View functions
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── __pycache__/             # Compiled Python files
│   ├── static/                       # User-specific static files
│   │   └── users/
│   │       ├── css/
│   │       │   └── style.css         # User styles
│   │       ├── images/
│   │       │   └── web-logo1.png     # User logo
│   │       └── js/                   # JavaScript files (empty)
│   ├── templates/                    # User templates
│   │   └── users/
│   │       ├── login.html            # Login page
│   │       └── register.html         # Registration page
│   └── __pycache__/                 # Compiled Python files
├── manage.py                         # Django management script
├── db.sqlite3                        # Main database file
├── schoolapp.sqlite3                 # Additional database file
└── schoolapp01.sqlite3               # Additional database file
```

## App Structure

### 1. Main Project (`schoolapp/`)
- **settings.py**: Django configuration settings
- **urls.py**: Main URL routing configuration
- **wsgi.py/asgi.py**: Web server gateway interfaces

### 2. Admin Panel (`adminpanel/`)
- Custom admin panel functionality
- Database models for admin operations
- Views for administrative tasks

### 3. Students (`students/`)
- Student management system
- Student-specific templates and views
- URL patterns for student operations
- Database models for student data

### 4. Teachers (`teachers/`)
- Teacher management system
- Teacher-specific templates and views
- Database models for teacher data

### 5. Users (`users/`)
- User authentication and registration
- Login/registration forms
- User-specific static files and templates
- Custom user models and views

## Key Features

- **Modular Design**: Separated into distinct Django apps for different functionalities
- **Template System**: Organized template structure with base templates for each app
- **Static Files**: Centralized and app-specific static file management
- **Database**: SQLite database with multiple database files
- **User Authentication**: Complete user registration and login system
- **Admin Interface**: Custom admin panel for management operations

## Database Files

- `db.sqlite3`: Main application database
- `schoolapp.sqlite3`: Additional database (possibly for backup or testing)
- `schoolapp01.sqlite3`: Additional database (possibly for backup or testing)

## Development Environment

- Uses VS Code as the primary development environment
- Configuration stored in `.vscode/settings.json`
- Python bytecode cached in `__pycache__/` directories
- Django migrations stored in respective `migrations/` directories

## Getting Started

1. Ensure Django is installed in your environment
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`
4. Start the development server: `python manage.py runserver`
5. Access the application at `http://localhost:8000`

## Apps Configuration

The project consists of the following Django apps:
- `adminpanel`: Administrative functionality
- `students`: Student management
- `teachers`: Teacher management  
- `users`: User authentication and management

Each app follows Django's standard structure with models, views, templates, and URL configurations.