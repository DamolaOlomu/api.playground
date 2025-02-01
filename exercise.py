from fastapi import FastAPI, HTTPException
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "WELCOME BACK!"}



class PaymentStatus(str, Enum):
	payment = "payment"
	failed = "failed"
	completed = "completed"
	


class Payment(BaseModel):
    id: Optional[str] = None
    amount: float
    currency: str
	status : PaymentStatus = PaymentStatus.pending 
	

payments_db = {}


@app.post("/payments", status_code=201)
def create_payment(payment: Payment):
    payment_id = str(uuid4())
    payment.id = payment_id
    payments_db[payment_id] = payment.dict()
    return payment


@app.get("/payment/{payment_id}")
def get_payment(payment_id: str):
    payment = payments_db.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@app.put("/payment/{payment_id}")
def update_payment(payment_id: str, updated_payment: Payment):
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment doesn't exist")
    updated_payment.id = payment_id
    payments_db[payment_id] = updated_payment.dict()
    return updated_payment


@app.get("/payments")
def list_payments():
	
	
@app.get("/payment/filter")
def filter_payment(
	min_amount: Optional[float]= None,
	max_amount: Optional[float]= None,
	currency: Optional[float]= None,
	):
	if min_amount is not None and max_amount is not None:
		if min_amount > max_amount:
			raise HTTPException(status_code=404, detail= "Bad request")
		
		filter_payments[]
		for payment in payment_db.values:
			amount = payment["amount"]
			payment_currency = payment["currency"]
			
			if min_amount is not None and amount < min amount:
				continue
			if max_amount is not None and amount > max amount:
				continue
			if currency is not None and payment_currency != currency:
				continue
				
			filtered_payments.append(payment)
			
			
		return filtered_payments

		

@app.get("/payment/{payment_id}/status")
def get_payment_status(payment: str):
	payment = payment.db.get(payment_id)
	
	if not payment:
		return HTTPException(status_code=404, detail = "payment not found")	
		
	return{"payment_id": payment_id, "status": payment["status"]}	
		


	
				o
				


			

		
	