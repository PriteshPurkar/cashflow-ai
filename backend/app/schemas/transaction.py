from datetime import date
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field

class Direction(str, Enum):
    inflow = "inflow"
    outflow = "outflow"

class Category(str, Enum):
    sales = "sales"
    customer_payment = "customer_payment"
    refund = "refund"
    raw_materials = "raw_materials"
    salary = "salary"
    rent = "rent"
    utilities = "utilities"
    equipment = "equipment"
    transfer = "transfer"
    other = "other"

class PaymentMethod(str, Enum):
    cash = "cash"
    upi = "upi"
    bank_transfer = "bank_transfer"

class Source(str, Enum):
    imported_bank_statement = "imported_bank_statement"
    manual_entry = "manual_entry"
    uci_online_retail = "uci_online_retail"

class RecordStatus(str, Enum):
    pending_review = "pending_review"
    confirmed = "confirmed"
    rejected = "rejected"

class TransactionBase(BaseModel):
    business_id: str
    date: date
    amount: Decimal = Field(..., gt=0)
    direction: Direction
    category: Category
    subcategory: str | None = None
    payment_method: PaymentMethod
    source: Source
    status: RecordStatus = RecordStatus.confirmed
    notes: str | None = None
    import_batch_id: str | None = None
    is_synthetic: bool = False

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    transaction_id: str