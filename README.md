# 🍅 Tomato Farm Management System

Welcome to the **Tomato Farm Management System**, a project built to manage and monitor the operations of an organic, soilless tomato farm. The system uses Django, PostgreSQL, Redis, and other essential tools to ensure seamless data flow and operational efficiency.

## 🚀 Features

- **Sensor Management**: Manage sensor data (temperature, humidity, etc.) from Raspberry Pi and other farm controllers.
- **Custom Admin Views**: Enhanced admin panel to manage sensor data with validations.
- **Automated Commands**: Custom management commands for automating sensor data cleaning and analysis.
- **Data Caching**: Redis-backed caching for real-time sensor data.
- **Database Connection Pooling**: Efficient database connections using PgBouncer.
- **Code Quality**: Enforced with Flake8 linter and standardized commit messages using Commitizen.

## 📚 Technologies Used

- **Backend Framework**: Django 5.1.1
- **Database**: PostgreSQL + PgBouncer for connection pooling
- **Caching**: Redis
- **Admin**: Django Admin with custom views and forms
- **API**: Django Rest Framework (DRF)
- **Code Quality**: Flake8, Commitizen
- **Deployment**: Gunicorn (WSGI)

## 🛠️ Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/Adebowale-Morakinyo/tomato-farm-management-system.git
   ```

2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up PostgreSQL and Redis:
   - Create a PostgreSQL database.
   - Set up Redis for caching.

4. Create `.env` file for environment variables:

   ```bash
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/db_name
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

## 📈 Admin Access

To manage sensor data and other farm-related metrics:

1. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

2. Access the admin panel at `/admin`.

## 🤖 Management Commands

Automate sensor data processing with custom commands:

```bash
python manage.py process_sensor_data
```

## 🎨 Custom Admin Views

Manage and validate sensor data through custom admin views, with detailed forms to ensure data integrity.

---

Feel free to contribute or open issues for enhancements!

**Project Maintainer**: [Adebowale Morakinyo](https://github.com/Adebowale-Morakinyo)
