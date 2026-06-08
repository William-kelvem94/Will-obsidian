"""
FastAPI CRUD - Complete REST API pattern with Pydantic validation

Description:
    Full CRUD (Create, Read, Update, Delete) implementation for a resource.
    Includes validation, error handling, and database integration pattern.

Usage:
    # Adapt this template for your resource (User, Post, Product, etc.)
    # 1. Replace 'Item' with your model name
    # 2. Adjust fields in ItemBase
    # 3. Add your database logic

Dependencies:
    pip install fastapi uvicorn pydantic

Example:
    # Run server
    uvicorn main:app --reload
    
    # Access
    # http://localhost:8000/docs

See also:
    - [[JARVIS/04-Engineering/Wiki/CheatSheets/FastAPI|FastAPI Cheat Sheet]]
    - [[Snippets/Database/prisma-setup.ts|Database Setup]]
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(
    title="Resource API",
    description="CRUD API for managing resources",
    version="1.0.0"
)

# ============================================================================
# MODELS (Pydantic)
# ============================================================================

class ItemBase(BaseModel):
    """Base model with common fields"""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be positive")
    is_active: bool = True


class ItemCreate(ItemBase):
    """Model for creating items (no id)"""
    pass


class ItemUpdate(BaseModel):
    """Model for updating items (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    is_active: Optional[bool] = None


class Item(ItemBase):
    """Model for response (includes id and timestamps)"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True  # For SQLAlchemy compatibility


# ============================================================================
# DATABASE (In-memory for demo - replace with real DB)
# ============================================================================

# In production, replace this with:
# - SQLAlchemy: from database import get_db
# - Prisma: from prisma import prisma
# - MongoDB: from motor import AsyncIOMotorClient

items_db: dict[int, dict] = {}
item_id_counter = 1


# ============================================================================
# ROUTES
# ============================================================================

@app.get("/", tags=["root"])
def root():
    """Health check endpoint"""
    return {"message": "API is running", "version": "1.0.0"}


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["items"]
)
def create_item(item: ItemCreate):
    """
    Create a new item
    
    Args:
        item: Item data (name, description, price)
    
    Returns:
        Created item with id and timestamps
    """
    global item_id_counter
    
    new_item = {
        "id": item_id_counter,
        **item.dict(),
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    items_db[item_id_counter] = new_item
    item_id_counter += 1
    
    return new_item


@app.get(
    "/items",
    response_model=List[Item],
    tags=["items"]
)
def list_items(
    skip: int = 0,
    limit: int = 100,
    is_active: Optional[bool] = None
):
    """
    List items with pagination and filtering
    
    Args:
        skip: Number of items to skip (for pagination)
        limit: Max number of items to return
        is_active: Filter by active status (optional)
    
    Returns:
        List of items
    """
    items = list(items_db.values())
    
    # Filter by is_active if provided
    if is_active is not None:
        items = [item for item in items if item["is_active"] == is_active]
    
    # Pagination
    return items[skip : skip + limit]


@app.get(
    "/items/{item_id}",
    response_model=Item,
    tags=["items"]
)
def get_item(item_id: int):
    """
    Get item by ID
    
    Args:
        item_id: Item ID
    
    Returns:
        Item details
    
    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    return items_db[item_id]


@app.put(
    "/items/{item_id}",
    response_model=Item,
    tags=["items"]
)
def update_item(item_id: int, item: ItemUpdate):
    """
    Update item (full replacement)
    
    Args:
        item_id: Item ID
        item: Updated item data
    
    Returns:
        Updated item
    
    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    # Get existing item
    existing_item = items_db[item_id]
    
    # Update only provided fields
    update_data = item.dict(exclude_unset=True)
    updated_item = {**existing_item, **update_data, "updated_at": datetime.now()}
    
    items_db[item_id] = updated_item
    
    return updated_item


@app.patch(
    "/items/{item_id}",
    response_model=Item,
    tags=["items"]
)
def partial_update_item(item_id: int, item: ItemUpdate):
    """
    Partially update item (same as PUT in this example)
    
    Args:
        item_id: Item ID
        item: Fields to update
    
    Returns:
        Updated item
    """
    # In this example, same as PUT
    # In practice, you might handle differently
    return update_item(item_id, item)


@app.delete(
    "/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["items"]
)
def delete_item(item_id: int):
    """
    Delete item
    
    Args:
        item_id: Item ID
    
    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    del items_db[item_id]
    
    # 204 No Content - no return value


# ============================================================================
# ERROR HANDLERS (Optional - for custom error responses)
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 handler"""
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=404,
        content={"error": "Resource not found", "path": str(request.url)}
    )


# ============================================================================
# STARTUP/SHUTDOWN (Optional - for DB connections, etc.)
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Run on app startup"""
    print("🚀 API starting up...")
    # Initialize database connection, etc.


@app.on_event("shutdown")
async def shutdown_event():
    """Run on app shutdown"""
    print("👋 API shutting down...")
    # Close database connection, etc.


# ============================================================================
# MAIN (for direct execution)
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "fastapi-crud:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on code changes
    )
