from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, constr, condecimal
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid
import datetime, timedelta
from random, import randint



app = FastAPI()



#define user model`
class User(BaseModel):
    id: uuid.UUID = uuid.uuid4() 
    username: str
    password: str
    email: str



#define payment model
class Payment(BaseModel):
    amount: float
    currency: str
    date: datetime = Field(default_factory=datetime.now)
    account_reference: uuid.UUID = uuid.uuid4()
    payment_reference: uuid.UUID = uuid.uuid4()
    


#define payment status model
class PaymentStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    rejected = "rejected"
    


#define payment response model
class PaymentResponse(BaseModel):
    payment: Payment
    status: PaymentStatus
    message: Optional[str] = None
    




#define bank accounts request model
class BankAccountRequests(BaseModel):
    customer_name: constr(min_length=10, max_length=20)
    currency: constr(min_length=3, max_length=3)
    
    
    
    
#to generate accounts response model    
class BankAccountResponse(BaseModel):
    account_id: uuid.UUID
    account_number: str
    bank_name: str
    currency: str
    created_at: datetime
    
    
    
    
def generate_virtual_account(BankAccount: BankAccountRequest): -> BankAccountResponse:
    account_number: str(randint(1000000000, 9999999999))
    bank_name: "Mock Bank"
    
    return BankAccountResponse(
    account_id: uuid.UUID
    account_number: str
    bank_name: str
    currency: str
    created_at: datetime.utc(now)
    )
                
        
        
        
#define card accounts request model
class CardPaymentRequest(BaseModel):
    card_number: constr(min_length=13, max_length=19, regex="^/d+$")
    card_holder_name: constr(min_length=2, max_length=50, regex="^/d+$")
    expiry_date: constr(regex="^0[1-9]1[0-2]/\d{2}$")
    cvv: constr(min_length=3, max_length=5, regex="^/d+$")
    amount: condecimal(gt=0, decimal_places=2)
    currency: constr(min_length=3, max_length=3)        
 
                
                                
                                                                 
#for charging cards    
class CardPaymentResponse(BaseModel):
    card_payment_id: uuid.UUID
    status: PaymentStatus
    timestamp: datetime
    
    
def process_payment(PaymentRequest: CardPaymentRequest) -> PaymentResponse:
    if PaymentRequest.card_number starts with ("4"):
        status: PaymentStatus.confimed
    else:
        status: PaymentStatus.failed
        
    return CardPaymentResponse(
    	card_payment_id: uuid.UUID
        status: PaymentStatus
        timestamp: datetime.utc(now)
         )
        
    

@app.get("/")
def index():
    return {"Hello": "WELCOME TO THE PAYMENT PORTAL!"}
    
    
    

#create payments
@app.post("/users/")
def create_user(user: User):
    return {"user": user}



#create payments
@app.post("/payments/")
def create_payment(payment: Payment):
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment": payment}



#confirm payments
@app.post("/payments/{payment_id}/confirm")
def confirm_payment(payment_id: uuid.UUID):
    if payment_id is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment_id": payment_id, "status": PaymentStatus.confirmed}




#reject payments
@app.post("/payments/{payment_id}/reject")
def reject_payment(payment_id: uuid.UUID):
    if payment_id is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment_id": payment_id, "status": PaymentStatus.rejected}



#get payments by payment id
@app.get("/payments/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: uuid.UUID):
    return {
        "payment": {
            "amount": 100.0,
            "currency": "USD",
            "date": "2021-08-01T12:00:00",
            "account_reference": "123e4567-e89b-12d3-a456-426614174000",
            "payment_reference": "123e4567-e89b-12d3-a456-426614174000",
        },
        "status": PaymentStatus.confirmed,
    }




#get payments
@app.get("/payments/", response_model=List[PaymentResponse])
def get_payments():
    return [
        {
            "payment": {
                "amount": 100.0,
                "currency": "USD",
                "date": "2021-08-01T12:00:00",
                "account_reference": "123e4567-e89b-12d3-a456-426614174000",
                "payment_reference": "123e4567-e89b-12d3-a456-426614174000",
            },
            "status": PaymentStatus.confirmed,
        },
        {
            "payment": {
                "amount": 200.0,
                "currency": "USD",
                "date": "2021-08-01T12:00:00",
                "account_reference": "123e4567-e89b-12d3-a456-426614174000",
                "payment_reference": "123e4567-e89b-12d3-a456-426614174000",
            },
            "status": PaymentStatus.rejected,
        },
    ]




#get users by user id
@app.get("/users/{user_id}")
def get_user(user_id: uuid.UUID):
    return {"user_id": user_id}



#list users by id
@app.get("/users/")
def get_users():
    users = [
        {"user_id": "123e4567-e89b-12d3-a456-426614174000"},
        {"user_id": "123e4567-e89b-12d3-a456-426614174000"},
    ]
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return [
        {"user_id": "123e4567-e89b-12d3-a456-426614174000"},
        {"user_id": "123e4567-e89b-12d3-a456-426614174000"},
    ]



#update user by user id
@app.put("/users/{user_id}")
def update_user(user_id: uuid.UUID, user: User):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "user": user}



#delete user by user id
@app.delete("/users/{user_id}")
def delete_user(user_id: uuid.UUID):
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}



#delete payment by payment id
@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: uuid.UUID):
    if payment_id is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment_id": payment_id}



#update payment status by payment id
@app.put("/payments/{payment_id}")
def update_payment(payment_id: uuid.UUID, payment: Payment):
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment_id": payment_id, "payment": payment}



#get payment status by payment id
@app.get("/payments/{payment_id}/status")
def get_payment_status(payment_id: uuid.UUID, status: str = "pending"):
    if status == "rejected":
        return {"payment_id": payment_id, "status": PaymentStatus.rejected}
    elif status == "confirmed":
        return {"payment_id": payment_id, "status": PaymentStatus.confirmed}
    else:
        return {"payment_id": payment_id, "status": PaymentStatus.pending}



#to charge card
@app.post("/payments/charge")
def charge_card(payment_request: CardPaymentRequest):
    response= process_payment(payment_request)
    if payment.response == PaymentStatus.failed:
        raise HTTPException(status_code=400, detail="Payment processing failed")
        return response
        
        
#user transaction database
user_transactions = {}


#ussd request model
class USSDRequestModel(BaseModel):
    session_id: str
    phone_number: str
    text: str
    

class SMSRequestModel(Basemodel):
    session_id: str
    message: str
    


#process ussd payment and sms payments
@app.post("/ussd/")
async def process_ussd(payment_request: USSDRequest):
    ""
	
		session_id = request.session_id
		phone_number= request.phone_number
		text= request.text.strip()
		
		
		
		if text == "":
		
		response = "CON Welcome to PlayerOneFinance/n"
		response += "1. Check your balance/n"
		response += "2. Make Payment/n"
		response += "3. Check your transaction status/n"
		response += "4. Exit"

		

		elif text == "1":
		balance = user.transaction.get(phone_number, 1000)
		response= f" END your balance is &{balance}"
		
		elif text == "2"
		response = f"CON amount to pay":
		
		elif text.startswith("2*"):
    try:
        amount = int(text.split("*")[1])  # Extracts amount after "2*"
        
        if amount > user_transactions.get(phone_number, 1000):
            response = "END Insufficient balance."
        else:
            # Deduct the amount
            user_transactions[phone_number] = user_transactions.get(phone_number, 1000) - amount
            response = f"END Payment of ${amount} successful."
    except ValueError:
        response = "END Invalid amount. Try again."

		elif text == "3"
		response = f"END thank you for using PlayerOneFinance" 
		
		
	"" s
    
    
    
    @app.post("/sms/")
async def send_sms(payment_request: SMSRequest):
    ""
    
    phone_number = request.phone_number
    message = request.message

    
    return {"status": "success", "phone_number": phone_number, "message": message}
                
    
    "" 
            
            
    


    