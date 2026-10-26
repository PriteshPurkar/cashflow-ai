from datetime import date
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field

class InvoiceStatus(str, Enum):
    unpaid = "unpaid"
    partially_paid = "partially_paid"
    paid = "paid"
    unresolved = "unresolved"

class InvoiceBase(BaseModel):
    business_id: str
    customer_id: str
    issue_date: date
    due_date: date
    amount: Decimal = Field(..., gt=0)
    status: InvoiceStatus = InvoiceStatus.unpaid
    is_synthetic: bool = False

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceRead(InvoiceBase):
    invoice_id: str