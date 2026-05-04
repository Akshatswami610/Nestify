# 🏠 Nestify – PG Finder Platform

Nestify is a full-stack web application designed to help students find and explore PG (Paying Guest) accommodations easily, while enabling property owners to manage listings and booking requests efficiently.

<img width="1456" height="836" alt="Screenshot 2026-05-04 at 7 44 04 PM" src="https://github.com/user-attachments/assets/4295bcf5-19ab-47f3-aad3-21b3bd10cb05" />

---

## 🚀 Features

### 👤 Owner Features

* Register & login using email/phone authentication
* Add, update, and delete PG listings
* Upload images for listings
* Manage booking requests
* Owner dashboard for control and monitoring

### 🧑‍🎓 User (Guest) Features

* Browse PG listings without login
* View detailed PG information
* Filter by city, rent, facilities, and gender preference
* Book visit requests (no authentication required)

---

## 🧱 Tech Stack

### 🔹 Backend

* Django
* Django REST Framework (DRF)
* Token Authentication

### 🔹 Frontend

* HTML, CSS (Airbnb-style UI)
* Django Templates

### 🔹 Database

* PostgreSQL (Azure-ready)

### 🔹 Deployment

* Azure App Service (planned)
* Gunicorn + WhiteNoise

---

## 📂 Project Structure

```
Nestify/
│
├── accounts/        # Authentication (custom user model, login, register)
├── listings/        # PG listings (core feature)
├── requests/        # Booking requests
├── support/         # Support pages (contact, etc.)
├── core/            # Project settings & main URLs
│
├── frontend/        # HTML templates (UI)
├── static/          # CSS, JS, assets
├── media/           # Uploaded images
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoints

* `/api/v1/accounts/`
* `/api/v1/listings/`
* `/api/v1/requests/`
* `/api/v1/support/`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Akshatswami610/Nestify
cd Nestify
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables (.env)

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🌐 Access the App

* Home: http://127.0.0.1:8000/
* API Root: http://127.0.0.1:8000/api/v1/

---

## ☁️ Deployment (Azure)

* Uses Azure App Service (Linux)
* PostgreSQL with SSL
* Static files via WhiteNoise
* Gunicorn as WSGI server

---

## 🔒 Security Features

* Token-based authentication
* Custom user model
* CSRF protection enabled
* Environment-based configuration

---

## 💡 Future Enhancements

* ⭐ Ratings & reviews
* 💬 Chat between owner & user
* 📍 Map-based PG search
* 💳 Online booking/payment
* 🔔 Email/SMS notifications

---

## 👨‍💻 Author

**Akshat Swami**
CSE Student | Backend Developer | Django + DRF Enthusiast

---

## 📌 License

This project is for educational and portfolio purposes.
