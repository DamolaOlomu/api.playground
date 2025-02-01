from fastapi import FastAPI, HttpException,
from typing import Optional, List
from enum import Enum  
from uuid import UUID
from pydantic import BaseModel


app = FastAPI()


@app.get("/index")
def index():
return {"Display: Hello World"}


payments_db = {}


class Payment(BaseModel):
	id: Optional(str) = None 
	amount: float 
	currency: str 
	desc: Optional(str) = None 
	status: Optional(str) = "Please wait while your payment is being confirmed"
	
	
class User(BaseModel):
	name = str
	username = str
	password = str


@app.post("/payments/")
def create_payment(payment : Payment):
	payment_id = str(uuid4())
	payment.id = payment_id
	payment_db[payment_id] = payment
	return payment


@app.get("/payments/{payment_id}")
def get_payment(payment_id: str):
	payment = payment_db.get(payment_id)
	if payment is None:
	raise HttpException(status_code 404, detail = "Payment Not Found")
	return payment


@app.get("/payments/{payment_id}")
def list_payment():
	return list(payment_db.values())
	
	
@app.put("/payments/{payment_id}")
def update_payment(payment_id: str, updated_payment = Payment):
	if payment_id not in payment_db:
		raise HttpException(status_code 404, detail = "Payment Not Found")
		
		updated.payment.id = updated_payment
		payments_db[payment_id] = updated_payment
		return payment
		
		
@app.delete("/payment/{payment_id}")
def delete_payment
	