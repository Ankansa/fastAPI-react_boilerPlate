# 🛠️ Admin Dashboard API

This is a backend system built with **FastAPI** and **MongoDB** for managing users, custom fields, and permissions in an admin-controlled environment.

## 📋 Features

- JWT-based Authentication
- Admin user registration and login
- Admin can add users and assign:
  - Role (`admin` or `user`)
  - Custom fields
- Fine-grained Permission Control:
  - View sales
  - Add users
  - Update/view permissions
- Database schema validation
- API Versioning Support
- MongoDB integration (with Motor)
- Paginated sales data API


## Permission List

`update_permissions`
`view_permissions`
`view_sales`
`view_users`
`create_user` -- A user can also create sub-user

---

## 🚀 Quick Start

### 🔧 Requirements

- Python 3.8+
- MongoDB (local or remote)
- `virtualenv` or `conda` (optional but recommended)

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Ankansa/admin_dashboard.git
cd admin_dashboard

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### ⚙️ Environment Variables

Create a `.env` file in the root directory with:

```
MONGODB_URI=mongodb://localhost:27017
JWT_SECRET_KEY=your_jwt_secret
JWT_ALGORITHM=HS256
```

### ▶️ Run the Server

```
python -m app.main
```

Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger for api testing [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Swagger Documentation [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📁 Project Structure

```
admin_dashboard/
├── app/
│   ├── routes/                # API endpoints (auth, users, permissions, sales)
│   ├── schemas/               # Pydantic models for request/response
│   ├── db/                    # MongoDB connection
│   ├── utils/                 # Auth, password hashing, permission dependencies
│   └── main.py                # FastAPI app entry
├── requirements.txt
├── .env
└── README.md
```

---

## 🔐 Authentication & Authorization

- **Register**: First user becomes admin automatically.
- **Login**: Receive a JWT token.
- **Protected Routes**: Use `Authorization: Bearer <token>` header.
- **Permissions**: Admins can assign granular permissions per user.

---

## 📦 API Endpoints

All APIs are under `/api`.

| Method | Endpoint                        | Description                     | Permission Required     |
|--------|----------------------------------|----------------------------------|--------------------------|
| POST   | /auth/register                   | Register admin                  | -                        |
| POST   | /auth/login                      | Login and get token             | -                        |
| POST   | /users                           | Create user                     | `create_user`            |
| GET    | /users                           | List all users                  | `view_users`             |
| POST   | /permissions                     | Add or update user permissions  | `update_permissions`     |
| GET    | /permissions                     | Get user permissions            | `view_permissions`       |
| GET    | /sales/{page}/{count}            | Paginated sales data            | `view_sales`             |



---
