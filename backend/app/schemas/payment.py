from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field

class PaymentBase(BaseModel):
    invoice_id: str
    payment_date: date | None = None   # null = unpaid / unresolved
    amount: Decimal = Field(..., ge=0)
    is_synthetic: bool = False

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    payment_id: str