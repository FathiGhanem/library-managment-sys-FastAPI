# 📚 Library Management System — FastAPI + SQLAlchemy

A backend **Library Management System** built using **FastAPI, SQLAlchemy, and PostgreSQL**.  
The system allows managing books and library members, including borrowing and returning books — using a clean layered architecture (routers → services → models/schemas → database).

---

## 🚀 Features

### 👤 Members
- Add new members
- Get all members
- Get a member by ID
- Delete a member

### 📘 Books
- Add new books
- Get all books
- Get a book by ID
- Update book details
- Delete a book
- Borrow a book
- Return a book

### 🏗 Architecture
✔ FastAPI Routers  
✔ Service Layer  
✔ SQLAlchemy ORM  
✔ Pydantic Schemas  
✔ PostgreSQL database  

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Uvicorn
- Pydantic
- Passlib & Bcrypt (hashing if needed later)

---

## 📁 Project Structure

# 📚 Library Management System — FastAPI + SQLAlchemy

A backend **Library Management System** built using **FastAPI, SQLAlchemy, and PostgreSQL**.  
The system allows managing books and library members, including borrowing and returning books — using a clean layered architecture (routers → services → models/schemas → database).

---

## 🚀 Features

### 👤 Members
- Add new members
- Get all members
- Get a member by ID
- Delete a member

### 📘 Books
- Add new books
- Get all books
- Get a book by ID
- Update book details
- Delete a book
- Borrow a book
- Return a book

### 🏗 Architecture
✔ FastAPI Routers  
✔ Service Layer  
✔ SQLAlchemy ORM  
✔ Pydantic Schemas  
✔ PostgreSQL database  

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Uvicorn
- Pydantic

---

## 📁 Project Structure

```
Library Management System/
├── main.py
├── database.py
├── requirements.txt
├── models/
│   ├── books_model.py
│   └── users_model.py
├── schemas/
│   ├── book_request.py
│   └── user_request.py
├── routers/
│   ├── books.py
│   └── users.py
└── services/
    ├── books_service.py
    └── users_service.py
```



- `models/` → SQLAlchemy database tables  
- `schemas/` → Pydantic request models  
- `routers/` → API endpoints  
- `services/` → business logic and DB operations  
- `database.py` → DB engine + session config  
- `main.py` → FastAPI app entry point  

---

## 🗄 Database Configuration

Inside `database.py`, update your database URL:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://USER:PASSWORD@localhost:5432/library_db"

Then create your database in PostgreSQL before running the app.

▶️ Run the Project
1️⃣ Create & activate a virtual environment

Linux / macOS:
python -m venv venv
source venv/bin/activate


Windows:
python -m venv venv
venv\Scripts\activate


2️⃣ Install dependencies
pip install -r requirements.txt


3️⃣ Start the server
uvicorn main:app --reload

4️⃣ Open API Docs
Swagger UI:
http://127.0.0.1:8000/docs


📌 API Endpoints
👤 Members (/members)
Method	Endpoint	Description
POST	/members/	Create a member
GET	/members/	Get all members
GET	/members/{member_id}	Get member by ID
DELETE	/members/{member_id}	Delete member
📘 Books (/books)
Method	Endpoint	Description
POST	/books/	Create a book
GET	/books/	Get all books
GET	/books/{book_id}	Get book by ID
PUT	/books/{book_id}	Update book
DELETE	/books/{book_id}	Delete book
POST	/books/borrow/{book_id}/{member_id}	Borrow book
POST	/books/return/{book_id}	Return book

🧠 Validations

Example — book fields are validated using Pydantic:

class BookRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)


