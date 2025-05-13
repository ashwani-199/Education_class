# EduClassHub - Django Education Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A comprehensive classroom management system for educational institutions, built with Django.

## 🚀 Features

- **Course Management**: Create and organize courses with rich content
- **Student Enrollment**: Manage student registrations and class rosters
- **Attendance Tracking**: Real-time class attendance system
- **Gradebook**: Digital grading system with analytics
- **Schedule Planner**: Interactive class timetable
- **User Roles**: Separate interfaces for Admin, Teachers, and Students
- **Document Sharing**: Secure file repository for course materials

## ⚙️ Prerequisites

- Python 3.8+
- Django 4.2+
- PostgreSQL 12+
- Virtual Environment

## 🛠️ Installation

```bash
# Clone repository
git clone https://github.com/yourusername/educclasshub.git
cd educclasshub

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env file with your credentials

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
