from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from uuid import UUID
from datetime import DateTime
import request
import datetime.

app = FastAPI()
r = request(https://fastapi.api/requests)


class User(BaseModel):
	id: Optional[uuid.UUID]= None
	user: Optional[str]= None
	password: Optional[str]= None
	

class Payment(BaseModel):
	amount: float
	currency: str
	recipient: str
	timestamp: datetime.now()
	timestamp: datetime = Field(default_factory=datetime.now)
	payment_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    payment_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    payment_reference: uuid.UUID = Field(default_factory=uuid.uuid4)
    account_reference: uuid.UUID = Field(default_factory=uuid.uuid4)

	
class PaymentStatus(BaseModel):
	payment_status: Optional[str]= "pending"
	
	
class
	
	

#define index 
@app.get("/")
def index():
	return{"message":"this message is to say Hi!"}
	
	

@app.post("/payments")
def create_payment(payments :str):
	if payments : payment_id
	return{payments}
		
			
					
#get payment by id	
@app.get("/payments"/{payment_id})
def get_payment(payment_id : str):
	payment.id: payment_id
	payment_id: Payment
	return{Payment}
	
	
#get payment by payment status	
app.get("payments"/{payment_status})
def get_payment_status(payment_status : str):
	payment.status : payment_status
	payment_status : PaymentStatus
	if payment not in Payment:
		raise{"Error = status code 404": "Payment not found"}
	return{payment_status}
	
	
#create user
@app.post("/users")
def create_user(users: str):
	users : User
	return{User}
	
	

#get user by id
@app.get("/users"/{user_id})
def get_user_id(user_id : str):
	user.id : user_id
	if user_id not in Users:
		raise{"Error = status code 404": "User not found"}
	return{user_id}
	
	
	


	
	

	