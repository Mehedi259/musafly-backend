# ⚙️ MusaFly Backend API

Welcome to the **MusaFly Backend API** repository. This is a robust and scalable REST API built with **Python** and **Django REST Framework (DRF)**. It handles all the data operations for the MusaFly platform, including the customer-facing website and the administrative dashboard.

## 🚀 Technologies Used
* **Language:** Python 3
* **Framework:** Django
* **API Framework:** Django REST Framework (DRF)
* **API Documentation:** drf-yasg (Swagger/OpenAPI)
* **Database:** SQLite (Default for development)

## 📦 Getting Started

First, clone the repository and navigate into the directory.

Create a Python virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Run database migrations:
```bash
python manage.py migrate
```

Start the development server:
```bash
python manage.py runserver
```
The API will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 📚 API Documentation
We use **Swagger** for comprehensive and interactive API documentation.
Once the server is running, visit:
- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## 📂 Project Structure
- `/config`: Core Django configuration (settings, urls, etc.).
- `/tours`, `/flights`, `/visas`, `/umrah`: Individual Django apps for different business domains containing models, views, and serializers.
