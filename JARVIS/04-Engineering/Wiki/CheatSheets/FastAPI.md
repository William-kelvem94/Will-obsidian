---
title: "FastAPI Cheat Sheet"
description: "Quick reference for FastAPI development"
tags: [cheatsheet, fastapi, python, api, backend]
updated: 2026-04-23
---

# FastAPI Cheat Sheet

Quick reference for FastAPI web framework.

---

## 🚀 Basic Setup

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="API description",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Hello World"}

# Run with:
# uvicorn main:app --reload
```

---

## 📍 Path Operations

### HTTP Methods

```python
@app.get("/items")          # Read
@app.post("/items")         # Create
@app.put("/items/{id}")     # Update (full)
@app.patch("/items/{id}")   # Update (partial)
@app.delete("/items/{id}")  # Delete
```

### Path Parameters

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Enum path params
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return {"model": model_name}
```

### Query Parameters

```python
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Optional params
from typing import Optional

@app.get("/items")
def list_items(q: Optional[str] = None):
    if q:
        return {"query": q}
    return {"query": "No query provided"}
```

---

## 📦 Request Body (Pydantic)

```python
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be positive")
    tax: Optional[float] = None

@app.post("/items")
def create_item(item: Item):
    return {"item": item.dict()}

# With validation
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)

@app.patch("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    return {"item_id": item_id, "updates": item.dict(exclude_unset=True)}
```

---

## 🔐 Authentication

### API Key

```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/secure")
def secure_endpoint(api_key: str = Security(verify_api_key)):
    return {"message": "Access granted"}
```

### Bearer Token (JWT)

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

@app.get("/protected")
def protected_route(payload: dict = Depends(verify_token)):
    return {"user": payload.get("sub")}
```

---

## 🗄️ Database (SQLAlchemy)

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends

# Database setup
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route with DB
@app.post("/users")
def create_user(email: str, name: str, db: Session = Depends(get_db)):
    user = User(email=email, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

## ⚠️ Error Handling

```python
from fastapi import HTTPException, status

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return items[item_id]

# Custom exception
class ItemNotFoundError(Exception):
    pass

@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Item not found"}
    )
```

---

## 📤 Response Models

```python
from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    email: str
    id: int

@app.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    # Password not in response due to response_model
    return {"email": user.email, "id": 123, "password": "hidden"}

# Multiple status codes
from fastapi.responses import JSONResponse

@app.post("/items", status_code=201)
def create_item(item: Item):
    return item

# Response with headers
from fastapi import Response

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="session_id", value="abc123")
    return {"message": "Cookie set"}
```

---

## 🔄 Async/Await

```python
@app.get("/async-items")
async def list_items_async():
    # Use async for I/O operations
    items = await fetch_items_from_db()
    return items

# Async database
from databases import Database

database = Database("postgresql://user:pass@localhost/db")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users")
async def list_users():
    query = "SELECT * FROM users"
    return await database.fetch_all(query)
```

---

## 📁 File Upload/Download

```python
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Save file
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename, "size": len(contents)}

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"uploads/{filename}"
    return FileResponse(file_path, filename=filename)
```

---

## 🌐 CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🧪 Testing

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post(
        "/items",
        json={"name": "Foo", "price": 10.5}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Foo"
```

---

## 🚀 Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db/dbname
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 📊 Background Tasks

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # Simulated slow task
    time.sleep(5)
    print(f"Sending email to {email}: {message}")

@app.post("/send-notification")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email, "Welcome!")
    return {"message": "Notification queued"}
```

---

## 🔗 Dependencies

```python
from fastapi import Depends

def common_params(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items")
def list_items(commons: dict = Depends(common_params)):
    return commons

# Class-based dependency
class Pagination:
    def __init__(self, skip: int = 0, limit: int = 100):
        self.skip = skip
        self.limit = limit

@app.get("/users")
def list_users(pagination: Pagination = Depends()):
    return {"skip": pagination.skip, "limit": pagination.limit}
```

---

## 📚 Key Commands

```bash
# Install
pip install fastapi uvicorn[standard]

# Run (dev)
uvicorn main:app --reload

# Run (prod)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Generate OpenAPI JSON
curl http://localhost:8000/openapi.json

# Access docs
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```

---

## 🔗 Related

- [[FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [[JARVIS/04-Engineering/Playbooks/Python-Dependency-Hell|Python Dependencies]]
- [[skills/02-software-engineering|Software Engineering Skills]]
