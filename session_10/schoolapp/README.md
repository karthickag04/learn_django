# TMYS School Management System# School App - Django Project



A comprehensive Django-based web application designed for modern educational institutions to manage students, teachers, lectures, and assignments efficiently.## Project Overview

This is a Django-based school management application that includes modules for managing students, teachers, admin panel, and user authentication.

## 🎯 Project Overview

## Project Structure

TMYS School Management System is a robust platform that facilitates:

- **Multi-role Authentication**: Students, Teachers, and Admin access```

- **Student Management**: Profile creation, enrollment, and academic trackingschoolapp/

- **Teacher Dashboard**: Content upload, student management, and feedback system├── .vscode/                          # VS Code configuration

- **Assignment System**: Multimedia assignment submission and tracking│   └── settings.json                 # VS Code settings

- **Media Management**: Video and audio lecture uploads with organized storage├── adminpanel/                       # Admin panel Django app

│   ├── __init__.py

## 🚀 Features│   ├── admin.py                      # Admin interface configuration

│   ├── apps.py                       # App configuration

### 👨‍🎓 Student Features│   ├── models.py                     # Database models

- **Profile Management**: Complete student registration with personal details│   ├── tests.py                      # Unit tests

- **Assignment Submission**: Upload video/audio assignments for lectures│   ├── views.py                      # View functions

- **Lecture Access**: View and access all uploaded teacher content│   ├── migrations/                   # Database migrations

- **Submission Tracking**: Monitor assignment submission status and history│   │   ├── __init__.py

│   │   └── __pycache__/             # Compiled Python files

### 👩‍🏫 Teacher Features│   └── __pycache__/                 # Compiled Python files

- **Lecture Upload**: Share educational content via video/audio files├── schoolapp/                        # Main Django project directory

- **Content Management**: Organize and manage uploaded lectures│   ├── __init__.py

- **Student Oversight**: View student assignment submissions│   ├── asgi.py                       # ASGI configuration

- **Media Library**: Access to comprehensive media management system│   ├── settings.py                   # Django settings

│   ├── urls.py                       # URL routing

### 🔐 Admin Features│   ├── wsgi.py                       # WSGI configuration

- **User Management**: Complete control over student and teacher accounts│   ├── static/                       # Static files (empty)

- **Content Moderation**: Oversight of all uploaded content│   ├── templates/                    # Templates (empty)

- **System Analytics**: Access to submission and usage statistics│   └── __pycache__/                 # Compiled Python files

- **Role Management**: Assign and modify user roles and permissions├── static/                           # Global static files

│   ├── css/                          # Stylesheets

## 🛠 Technical Stack│   │   ├── index.css

│   │   └── main.css

- **Backend**: Django 5.2.7│   ├── images/                       # Image assets

- **Database**: SQLite (Development) / MySQL (Production Ready)│   │   └── web-logo.png

- **Frontend**: HTML5, CSS3, Bootstrap-styled components│   └── js/                           # JavaScript files (empty)

- **Media Handling**: Django FileField with organized storage├── students/                         # Students Django app

- **Authentication**: Django's built-in auth with custom user model│   ├── __init__.py

- **Admin Interface**: Enhanced with django-jazzmin│   ├── admin.py                      # Admin interface configuration

│   ├── apps.py                       # App configuration

## 📋 Prerequisites│   ├── form.py                       # Student forms (StudentRegistrationForm)

│   ├── models.py                     # Student models

- Python 3.8+│   ├── tests.py                      # Unit tests

- Django 5.2+│   ├── urls.py                       # URL patterns

- pip (Python package manager)│   ├── views.py                      # View functions

│   ├── migrations/                   # Database migrations

## ⚡ Quick Setup│   │   ├── __init__.py

│   │   └── __pycache__/             # Compiled Python files

### 1. Environment Setup│   ├── templates/                    # Student templates

```bash│   │   └── students/

# Clone the repository│   │       ├── base.html             # Base template

git clone <repository-url>│   │       ├── index.html            # Student index page

cd schoolapp│   │       └── student_form.html     # Student registration form template

│   └── __pycache__/                 # Compiled Python files

# Create virtual environment (recommended)├── teachers/                         # Teachers Django app

python -m venv venv│   ├── __init__.py

source venv/bin/activate  # On Windows: venv\Scripts\activate│   ├── admin.py                      # Admin interface configuration

│   ├── apps.py                       # App configuration

# Install dependencies│   ├── models.py                     # Teacher models

pip install django django-jazzmin│   ├── tests.py                      # Unit tests

```│   ├── urls.py                       # URL patterns

│   ├── views.py                      # View functions

### 2. Database Configuration│   ├── migrations/                   # Database migrations

```bash│   │   ├── __init__.py

# Apply database migrations│   │   └── __pycache__/             # Compiled Python files

python manage.py makemigrations│   ├── templates/                    # Teacher templates

python manage.py migrate│   │   └── teachers/

│   │       ├── base.html             # Base template

# Create admin superuser│   │       └── index.html            # Teacher index page

python manage.py createsuperuser│   └── __pycache__/                 # Compiled Python files

```├── templates/                        # Global templates (currently empty)

├── users/                            # User authentication Django app

### 3. Initial Data Setup│   ├── __init__.py

```bash│   ├── admin.py                      # Admin interface configuration

# Create user groups (run in Django shell)│   ├── apps.py                       # App configuration

python manage.py shell│   ├── forms.py                      # User forms

```│   ├── models.py                     # User models

```python│   ├── tests.py                      # Unit tests

from django.contrib.auth.models import Group│   ├── urls.py                       # URL patterns

Group.objects.get_or_create(name='students')│   ├── views.py                      # View functions

Group.objects.get_or_create(name='teachers')│   ├── migrations/                   # Database migrations

```│   │   ├── __init__.py

│   │   └── __pycache__/             # Compiled Python files

### 4. Run Development Server│   ├── static/                       # User-specific static files

```bash│   │   └── users/

python manage.py runserver│   │       ├── css/

```│   │       │   └── style.css         # User styles

│   │       ├── images/

Visit `http://127.0.0.1:8000` to access the application.│   │       │   └── web-logo1.png     # User logo

│   │       └── js/                   # JavaScript files (empty)

## 📁 Project Structure│   ├── templates/                    # User templates

│   │   └── users/

```│   │       ├── index.html            # User index page

schoolapp/│   │       ├── login.html            # Login page

├── schoolapp/                 # Main project configuration│   │       ├── master.html           # User master template

│   ├── settings.py           # Django settings│   │       └── register.html         # Registration page

│   ├── urls.py               # URL routing│   └── __pycache__/                 # Compiled Python files

│   └── wsgi.py               # WSGI configuration├── media/                            # Media files directory (user uploads)

├── users/                    # Authentication & user management│   ├── videos/                       # Teacher lecture videos

│   ├── models.py             # CustomUser model│   ├── audio/                        # Teacher lecture audio files

│   ├── forms.py              # User registration/login forms│   └── assignments/                  # Student assignment submissions

│   └── templates/            # Authentication templates│       ├── video/                    # Student video submissions

├── students/                 # Student management│       └── audio/                    # Student audio submissions

│   ├── models.py             # StudentProfile, AssignmentSubmission├── manage.py                         # Django management script

│   ├── form.py               # Student forms├── db.sqlite3                        # Main database file

│   ├── views.py              # Student views├── schoolapp.sqlite3                 # Additional database file

│   └── templates/            # Student interface templates├── schoolapp01.sqlite3               # Additional database file

├── teachers/                 # Teacher management└── schoolapp2.sqlite3                # Additional database file

│   ├── models.py             # Lecture, Feedback models```

│   ├── forms.py              # Teacher forms

│   ├── views.py              # Teacher views## App Structure

│   └── templates/            # Teacher interface templates

├── static/                   # Static files (CSS, JS, Images)### 1. Main Project (`schoolapp/`)

│   ├── css/                  # Stylesheets- **settings.py**: Django configuration settings

│   ├── js/                   # JavaScript files- **urls.py**: Main URL routing configuration

│   └── images/               # Static images- **wsgi.py/asgi.py**: Web server gateway interfaces

├── media/                    # User uploaded files

│   ├── videos/               # Lecture videos### 2. Admin Panel (`adminpanel/`)

│   ├── audio/                # Audio files- Custom admin panel functionality

│   └── assignments/          # Student submissions- Database models for admin operations

└── templates/                # Global templates- Views for administrative tasks

```

### 3. Students (`students/`)

## 🎮 Usage Guide- Student management system

- Student registration forms (`form.py`)

### For Students- Assignment submission system with media upload

1. **Registration**: Use the registration form to create a student account- Student-specific templates and views

2. **Profile Setup**: Complete your student profile with academic details- URL patterns for student operations

3. **View Lectures**: Browse available lectures from teachers- Database models for student data and assignment submissions

4. **Submit Assignments**: Upload video or audio responses to lecture assignments

5. **Track Progress**: Monitor your submission history and status### 4. Teachers (`teachers/`)

- Teacher management system

### For Teachers- Lecture upload system with video/audio support

1. **Account Creation**: Admin creates teacher accounts or self-registration- Teacher-specific templates and views

2. **Upload Content**: Share educational materials via video/audio uploads- URL patterns for teacher operations

3. **Manage Lectures**: Organize and categorize your uploaded content- Database models for teacher data and lecture content

4. **Review Submissions**: Access and evaluate student assignment submissions

5. **Provide Feedback**: Use the feedback system to guide student learning### 5. Users (`users/`)

- User authentication and registration

### For Administrators- Login/registration forms

1. **Access Admin Panel**: Visit `/admin/` with superuser credentials- User-specific static files and templates

2. **User Management**: Create, modify, and manage student/teacher accounts- Custom user models and views

3. **Content Oversight**: Monitor and moderate all uploaded content

4. **System Configuration**: Adjust settings and permissions as needed## Key Features



## 🗃 Database Models- **Modular Design**: Separated into distinct Django apps for different functionalities

- **Template System**: Organized template structure with base templates for each app

### Users App- **Static Files**: Centralized and app-specific static file management

- **CustomUser**: Extended Django user with role-based access (student/teacher)- **Database**: SQLite database with multiple database files

- **User Authentication**: Complete user registration and login system

### Students App- **Admin Interface**: Custom admin panel for management operations

- **StudentProfile**: Comprehensive student information (personal, academic)- **Media Upload System**: Full audio/video upload and review system for teachers and students

- **AssignmentSubmission**: Links students to lecture assignments with media uploads  - Teachers can upload lecture videos and audio files

  - Students can submit assignment responses in video/audio format

### Teachers App  - Built-in media preview with HTML5 video/audio players

- **Lecture**: Teacher-uploaded educational content with multimedia support  - Download functionality for all uploaded media

- **Feedback**: Teacher feedback and communication system for students  - Admin panel integration with direct download links



## 🎨 Styling & UI## Database Files



The application uses a modern, responsive design with:- `db.sqlite3`: Main application database

- **Bootstrap-inspired** form styling- `schoolapp.sqlite3`: Additional database (possibly for backup or testing)

- **Mobile-friendly** responsive layout- `schoolapp01.sqlite3`: Additional database (possibly for backup or testing)

- **Consistent color scheme** across all modules- `schoolapp2.sqlite3`: Additional database (possibly for backup or testing)

- **Intuitive navigation** with role-based menus

- **Professional appearance** suitable for educational environments## Development Environment



## 🔧 Configuration- Uses VS Code as the primary development environment

- Configuration stored in `.vscode/settings.json`

### Static Files- Python bytecode cached in `__pycache__/` directories

- Development: Files served from `static/` directory- Django migrations stored in respective `migrations/` directories

- Production: Configure `STATIC_ROOT` for production deployment

## Getting Started

### Media Files

- Uploads stored in `media/` directory1. Ensure Django is installed in your environment

- Organized by content type (videos, audio, assignments)2. Run migrations: `python manage.py migrate`

- Configurable upload limits and file type restrictions3. Create a superuser: `python manage.py createsuperuser`

4. Start the development server: `python manage.py runserver`

### Database5. Access the application at `http://localhost:8000`

- Development: SQLite (included)

- Production: MySQL configuration available in settings.py## Media Upload Features



## 🚀 Deployment### For Teachers:

- Upload lecture videos and audio files

For production deployment:- Access at: `/teachers/upload/`

1. Set `DEBUG = False` in settings.py- View all lectures at: `/teachers/media/`

2. Configure production database (MySQL)- Manage uploads through Django admin

3. Set up static file serving with web server

4. Configure media file storage and permissions### For Students:

5. Set secure environment variables- Submit assignment responses in video/audio format

- Access at: `/students/assignments/`

## 🤝 Contributing- View submission history and download previous submissions

- One submission per lecture allowed

1. Fork the repository

2. Create a feature branch (`git checkout -b feature/new-feature`)### Admin Panel:

3. Commit your changes (`git commit -am 'Add new feature'`)- Direct download links for all media files

4. Push to the branch (`git push origin feature/new-feature`)- Filter and search functionality

5. Create a Pull Request- Organized by upload date and user



## 📄 License## Apps Configuration



This project is developed for educational purposes and is open for academic use and modification.The project consists of the following Django apps:

- `adminpanel`: Administrative functionality

## 🆘 Support- `students`: Student management

- `teachers`: Teacher management  

For issues and questions:- `users`: User authentication and management

- Check the Django documentation

- Review the code comments and docstringsEach app follows Django's standard structure with models, views, templates, and URL configurations.
- Create an issue in the repository

---

**TMYS School Management System** - Delivering quality education through modern technology solutions.