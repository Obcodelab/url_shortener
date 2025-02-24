# 🚀 FastAPI URL Shortener

A simple and efficient **URL shortener API** built with **FastAPI**, **SQLAlchemy**, and **Alembic**.  
It supports **custom short codes, automatic redirection, and click analytics**.

---

## 📌 Features

- 🔗 Shorten long URLs with a random or custom short code.
- 🔄 Automatic **redirects** from short URLs.
- 📊 **Analytics**: Track the number of clicks per URL.
- 🛠 **Database migrations** with Alembic.
- 🏗 Fully backend-based

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Obcodelab/url_shortener
cd url_shortener
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
# On Linux or Macos
python3 -m venv venv
source venv/bin/activate
```

```bash
# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup the Database

Run Alembic migrations to create the required database tables:

```bash
alembic upgrade head
```

### 5️⃣ Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

API details will be available at: http://127.0.0.1:8000/redoc
You can try it out at : http://127.0.0.1:8000/docs

## 🏗 Tech Stack

- FastAPI (Backend)
- SQLite (Database)
- SQLAlchemy & Alembic (ORM & Migrations)
- Uvicorn (ASGI Server)

## 📜 License

This project is open-source under the MIT License.
