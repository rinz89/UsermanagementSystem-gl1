# 🧩 Django User & Task Management API

A **User and Task Management System** built with **Django** and **Django REST Framework (DRF)**.  
This project provides user registration, authentication (token-based), and CRUD operations for managing tasks, along with API documentation via Swagger.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register, Login, and Logout using DRF Token Authentication
- ✅ **Task Management**
  - Create, Read, Update, Delete tasks per user
- 📎 **File Upload Support**
  - Upload attachments for each task
- 📘 **API Documentation**
  - Swagger and DRF Browsable API
- 🧱 **Clean and Modular Structure**
  - Django apps for users and tasks
- ☁️ **Deployment Ready**
  - Configured for deployment on Render / Heroku

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5.x |
| **API Framework** | Django REST Framework |
| **Authentication** | DRF Token Authentication |
| **Database** | SQLite (Default) |
| **Documentation** | Swagger (`drf-yasg`) |
| **Deployment** | Gunicorn + Whitenoise (Render/Heroku Ready) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/UserManagementProject.git
cd UserManagementProject
