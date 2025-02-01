from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# Database simulation
payments_db = {}

# Payment schema
class Payment(BaseModel):
    id: Optional[str] = None
    amount: float
    currency: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    
    
#payment schema again
class User(BaseModel):
    id: str = uuid.UUID
    user: str
    password: str
    


# Create a new payment
@app.post("/payments/", status_code=201)
def create_payment(payment: Payment):
    payment_id = str(uuid4())
    payment.id = payment_id
    payments_db[payment_id] = payment
    return payment

# Get a payment by ID
@app.get("/payments/{payment_id}")
def get_payment(payment_id: str):
    payment = payments_db.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

# List all payments
@app.get("/payments/")
def list_payments():
    return list(payments_db.values())

# Update a payment
@app.put("/payments/{payment_id}")
def update_payment(payment_id: str, updated_payment: Payment):
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    updated_payment.id = payment_id
    payments_db[payment_id] = updated_payment
    return updated_payment

# Delete a payment
@app.delete("/payments/{payment_id}", status_code=204)
def delete_payment(payment_id: str):
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    del payments_db[payment_id]
    return {"message": "Payment deleted successfully"}
    
    
    
#CREATE USER CALL.
@app.post("")





@app.get("/users")
def get_user