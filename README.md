# 💼 CRM-Gestion-Web – Customer Relationship Management System

**CRM-Gestion-Web** is a comprehensive customer relationship management platform that enables businesses to manage customer interactions, sales pipelines, and business operations efficiently.

The application includes user authentication, customer database management, sales tracking, and reporting features. This project demonstrates modern full-stack development practices using Django and demonstrates professional business application development.

---

# 🚀 Features

## 👥 Customer Management
- Create, read, update, and delete customer records
- Store detailed customer information and contact history
- Organize customers by categories or segments
- Track customer interactions and communications

## 🔐 Authentication & Security
- Secure user authentication using Django's built-in system
- Password hashing and secure session management
- Protected routes and role-based access control
- User permission management

## 📊 Sales Pipeline Management
- Track sales opportunities and deals
- Monitor sales progress through multiple stages
- Record deal values and timelines
- Generate sales forecasts and reports

## 📈 Reporting & Analytics
- Generate business reports and insights
- Dashboard with key performance indicators (KPIs)
- Export data for analysis and presentations
- Track sales metrics and performance trends

## 🎯 Task & Activity Management
- Create and assign tasks to team members
- Schedule follow-ups and reminders
- Track activities and interactions with customers
- Manage project timelines and deadlines

---

# 🏗️ Architecture

The project follows a **monolithic Django architecture** with a clear separation of concerns:

```
CRM-Gestion-Web
│
├── Dominus      → Main Django app (core functionality)
├── Dom          → Additional Django app module
├── templates    → HTML templates
├── static       → CSS, JavaScript, and static assets
└── manage.py    → Django project management
```

### Data Flow

User Interface → Django Views → Business Logic → Database  
Request → Middleware → URL Router → View → Template Response

---

# 🛠️ Technologies Used

## Backend
- Django
- Python
- Django ORM (Object-Relational Mapping)
- PostgreSQL (Database)
- Django REST Framework (for API endpoints)

## Frontend
- HTML5
- CSS3
- JavaScript
- Django Templates
- Bootstrap (or custom CSS framework)

## Development Tools
- Git & GitHub
- Python Virtual Environment
- Django Management Commands
- Heroku (Deployment)

---

# 💡 Skills Demonstrated

This project demonstrates the following technical skills:

- Full-stack web application development
- Backend architecture and design patterns
- Database modeling and management
- Django framework expertise
- User authentication and authorization
- Business logic implementation
- HTML/CSS/JavaScript frontend development
- Responsive web design
- Web application deployment

---

# 📂 Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/johandev456/CRM-gestion-web.git
cd CRM-gestion-web
```

---

# Backend Setup

## Create a Virtual Environment

```bash
python -m venv .venv
```

## Activate the Virtual Environment

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Run Migrations

```bash
python manage.py migrate
```

## Create a Superuser

```bash
python manage.py createsuperuser
```

## Run the Development Server

```bash
python manage.py runserver
```

The application will run on:

```
http://localhost:8000
```

Access the admin panel at:

```
http://localhost:8000/admin
```

---

# 🌐 Deployment

The application is configured for Heroku deployment using the provided `Procfile` and `runtime.txt`.

### Deploy to Heroku

```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your_secret_key
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

For detailed production deployment instructions, see `PRODUCTION_NOTES.md`.

---

# 📝 Project Structure

```
CRM-gestion-web/
├── Dominus/              → Main Django app
├── Dom/                  → Secondary Django app
├── templates/            → HTML templates
├── static/               → CSS, JS, images
├── manage.py             → Django management
├── requirements.txt      → Python dependencies
├── Procfile              → Heroku deployment config
├── runtime.txt           → Python version
└── PRODUCTION_NOTES.md   → Production deployment guide
```

---

# 🔧 Common Commands

```bash
# Run the development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

---

# 👨‍💻 Author

**Johan Rosario**

Computer Science Engineering Student focused on full-stack development and business application development.
