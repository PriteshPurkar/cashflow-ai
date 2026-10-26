from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field

class BusinessBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    industry: str | None = None
    currency: str = Field(default="INR", min_length=3, max_length=3)
    minimum_cash_balance: Decimal = Field(default=Decimal("0"), ge=0)

class BusinessCreate(BusinessBase):
    pass

class BusinessRead(BusinessBase):
    business_id: str
    created_at: datetime