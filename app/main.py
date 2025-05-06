from fastapi import FastAPI

# from app.routes import auth, users, permissions, sales
from app.routes.v1 import (
    auth as v1_auth,
    users as v1_users,
    permissions as v1_permissions,
    sales as v1_sales,
)

import uvicorn

app = FastAPI()


# app.include_router(auth.router, prefix="/api")
# app.include_router(users.router, prefix="/api")
# app.include_router(permissions.router, prefix="/api")
# app.include_router(sales.router, prefix="/api")

API_VERSION_1 = "/api/v1"

app.include_router(v1_auth.router, prefix=API_VERSION_1)
app.include_router(v1_users.router, prefix=API_VERSION_1)
app.include_router(v1_permissions.router, prefix=API_VERSION_1)
app.include_router(v1_sales.router, prefix=API_VERSION_1)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
