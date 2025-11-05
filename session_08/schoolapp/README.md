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
│   ├── form.py                       # Student forms (StudentRegistrationForm)
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
│   │       ├── index.html            # Student index page
│   │       └── student_form.html     # Student registration form template
│   └── __pycache__/                 # Compiled Python files
├── teachers/                         # Teachers Django app
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Teacher models
│   ├── tests.py                      # Unit tests
│   ├── urls.py                       # URL patterns
│   ├── views.py                      # View functions
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── __pycache__/             # Compiled Python files
│   ├── templates/                    # Teacher templates
│   │   └── teachers/
│   │       ├── base.html             # Base template
│   │       └── index.html            # Teacher index page
│   └── __pycache__/                 # Compiled Python files
├── templates/                        # Global templates (currently empty)
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
│   │       ├── index.html            # User index page
│   │       ├── login.html            # Login page
│   │       ├── master.html           # User master template
│   │       └── register.html         # Registration page
│   └── __pycache__/                 # Compiled Python files
├── media/                            # Media files directory (user uploads)
│   ├── videos/                       # Teacher lecture videos
│   ├── audio/                        # Teacher lecture audio files
│   └── assignments/                  # Student assignment submissions
│       ├── video/                    # Student video submissions
│       └── audio/                    # Student audio submissions
├── manage.py                         # Django management script
├── db.sqlite3                        # Main database file
├── schoolapp.sqlite3                 # Additional database file
├── schoolapp01.sqlite3               # Additional database file
└── schoolapp2.sqlite3                # Additional database file
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
- Student registration forms (`form.py`)
- Assignment submission system with media upload
- Student-specific templates and views
- URL patterns for student operations
- Database models for student data and assignment submissions

### 4. Teachers (`teachers/`)
- Teacher management system
- Lecture upload system with video/audio support
- Teacher-specific templates and views
- URL patterns for teacher operations
- Database models for teacher data and lecture content

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
- **Media Upload System**: Full audio/video upload and review system for teachers and students
  - Teachers can upload lecture videos and audio files
  - Students can submit assignment responses in video/audio format
  - Built-in media preview with HTML5 video/audio players
  - Download functionality for all uploaded media
  - Admin panel integration with direct download links

## Database Files

- `db.sqlite3`: Main application database
- `schoolapp.sqlite3`: Additional database (possibly for backup or testing)
- `schoolapp01.sqlite3`: Additional database (possibly for backup or testing)
- `schoolapp2.sqlite3`: Additional database (possibly for backup or testing)

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

## Media Upload Features

### For Teachers:
- Upload lecture videos and audio files
- Access at: `/teachers/upload/`
- View all lectures at: `/teachers/media/`
- Manage uploads through Django admin

### For Students:
- Submit assignment responses in video/audio format
- Access at: `/students/assignments/`
- View submission history and download previous submissions
- One submission per lecture allowed

### Admin Panel:
- Direct download links for all media files
- Filter and search functionality
- Organized by upload date and user

## Apps Configuration

The project consists of the following Django apps:
- `adminpanel`: Administrative functionality
- `students`: Student management
- `teachers`: Teacher management  
- `users`: User authentication and management

Each app follows Django's standard structure with models, views, templates, and URL configurations.