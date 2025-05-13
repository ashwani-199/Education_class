# Education_class - Django Education Class

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A comprehensive classroom management system for educational class, built with Django.

## 🚀 Features

- **Course Management**: Create and organize courses with rich content
- **Student Enrollment**: Manage student registrations and class rosters
- **Attendance Tracking**: Real-time class attendance system
- **Gradebook**: Digital grading system with analytics
- **User Roles**: Separate interfaces for Admin, Teachers, and Students

## ⚙️ Prerequisites

- Python 3.8+
- Django 4.2+
- PostgreSQL 12+
- Virtual Environment

## 🛠️ Installation

```bash
# Clone repository
git clone https://github.com/yourusername/Education_class.git
cd Education_class

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
