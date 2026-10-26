from datetime import date
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel

class AccountType(str, Enum):
    bank = "bank"
    cash = "cash"

class CashPositionBase(BaseModel):
    business_id: str
    date: date
    account_type: AccountType
    opening_balance: Decimal
    inflows: Decimal
    outflows: Decimal
    closing_balance: Decimal
    observed_closing: Decimal | None = None
    is_synthetic: bool = False

class CashPositionRead(CashPositionBase):
    balance_id: str