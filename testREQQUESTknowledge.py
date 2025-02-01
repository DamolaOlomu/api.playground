from fastapi import FastAPI
from pydantic import BaseModel, HTTPException, Field, constr, condecimal
from typing import List, Optional
import uuid
from datetime import datetime, timedelta
import enum

app = FastAPI():


app.get("/")
return {"HOME": "WELCOME TO PLAYERONEFINANCE"}


class PAYMENT(BaseModel):
	customer_name: str
	account_ref: uuid.UUID
	payment_id: uuid.UUID
	payment_status: Payment.Status
	payment_ref: uuid.UUID
	amount: str
	currency: float
	

class PAYMENTSTATUS(str, Enum):
	pending = "pending"
	confirmed = "confirmed"
	failed = "failed"





class CARDPAYMENTSREQUEST(BaseModel):
	customer_name: str
	card_number: constr(min_length=16, max_length=18, regex= "^/d+$")
	expiry_date: constr(0[1-9],1[0-2]], regex = "^/d{2}")
	cvv: constr(min_length=3, max_length=5, regex= "^/d+$")
	amount: condecimal(gt=0, decimal_places=2)
	currency: float
	timestamp: datetime.utc(now)
	
	
class CARDPAYMENTRESPONSE(BaseModel):
	card_payment_id: uuid.UUID
	status: Payment.Status
	timestamp: datetime
	
def process_payment(PaymentRequest: CARDPAYMENTSREQUEST) -> CARDPAYMENTRESPONSE:
	if CARDPAYMENTSREQUEST.card_number starts with "4":
	return status: PaymentStatus.confirmed:
	
	else:
	return status: PaymentStatus.failed
	
	return CardPaymentResponse(
    	card_payment_id: uuid.UUID
        status: PaymentStatus
        timestamp: datetime.utc(now)
         )
	
	
	
	