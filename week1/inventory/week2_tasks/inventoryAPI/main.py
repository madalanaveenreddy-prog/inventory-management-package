from fastapi import FastAPI, HTTPException, Query
from models import ProductCreateSchema, ProductUpdateSchema
from database import fake_db, PhysicalProduct, DigitalProduct

app = FastAPI(title="Advanced CRUD Inventory API")

# 1. GET ALL with Query Parameter (?max_price=50)
@app.get("/products")
def get_products(max_price: float = Query(None, description="Filter products below this total price")):
    return {"products": fake_db.get_all_products(max_price)}

# 2. GET SINGLE with Path Parameter (/products/1)
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    product = fake_db.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return {
        "id": product.id,
        "name": product.name,
        "total_price": product.calculate_total_price()
    }

# 3. POST (Create)
@app.post("/products", status_code=201) # 201 indicates "Created" successfully
def create_product(payload: ProductCreateSchema):
    if fake_db.get_product_by_id(payload.id):
        raise HTTPException(status_code=400, detail="Product ID already exists")
        
    if payload.product_type == "physical":
        new_product = PhysicalProduct(payload.id, payload.name, payload.base_price)
    else:
        new_product = DigitalProduct(payload.id, payload.name, payload.base_price)
    
    fake_db.add_product(new_product)
    return {"message": f"Successfully added {payload.name}!"}

# 4. PUT (Update using Path Parameter & Request Body)
@app.put("/products/{product_id}")
def update_product(product_id: int, payload: ProductUpdateSchema):
    product = fake_db.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Mutating the existing object properties safely
    product.name = payload.name
    product.base_price = payload.base_price
    return {"message": f"Product {product_id} updated successfully!"}

# 5. DELETE (Remove using Path Parameter)
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    success = fake_db.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": f"Product {product_id} deleted successfully!"}
