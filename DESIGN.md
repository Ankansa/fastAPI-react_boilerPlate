Admin Dashboard Backend - Design Documentation


1. Introduction
This document outlines the design and architecture of an Admin Dashboard backend developed using FastAPI and MongoDB. The system supports user registration, permission assignment, and secure access to various parts of the application based on roles.


2. Tech Stack
- Backend Framework: FastAPI
- Database: MongoDB (using Motor async driver)
- Authentication: JWT-based
- Password Hashing: passlib (bcrypt)
- API Testing: Postman Collection



3. System Design

3.1 User Roles
- Admin: Can register, create users, and assign permissions.
- User: Can access APIs based on permissions granted by Admin.

3.2 Modules and Functionalities

- Authentication Module:
  - Register (first user becomes Admin)
  - Login (JWT Token Generation)

- User Module:
  - Admin can create normal users
  - A normal user can add a sub-user if the user has permission “create_user”
  - Tracks who added the user ('added_by')

- Permission Module:
  - Admin assigns specific API access permissions per user
  - Permissions can be updated

- Sales Module:
  - View sales data (protected by permission)
  - Supports pagination


4. API Versioning
API routes are grouped under versioned prefixes (e.g., /api/v1). This allows future versions (e.g., /api/v2) to be introduced without breaking existing clients.


5. Permission System
Each user has a 'permissions' document in the 'permissions' collection.
Permissions are stored as key-value pairs indicating access to specific API features (e.g., { 'view_sales': True, 'create_user': False }).


6. MongoDB Collections
- users
- permissions
- sales

7. Error Handling
All routes implement HTTPException handling for expected errors such as missing permissions, invalid input, or authentication failure.

8. Security
- Passwords are hashed using bcrypt.
- JWT tokens are used to authenticate and authorize requests.
- Protected endpoints require valid permissions.

9. Conclusion
The Admin Dashboard backend provides a scalable, secure foundation for managing users and access control across different parts of a product.
