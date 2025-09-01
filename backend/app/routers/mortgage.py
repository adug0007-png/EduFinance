from fastapi import APIRouter
from pydantic import BaseModel, Field
import math

router = APIRouter()

class MortgageRequest(BaseModel):
    principal: float = Field(gt=0)
    annual_interest_rate_pct: float = Field(ge=0)  # e.g., 5 for 5%
    years: int = Field(gt=0)

class MortgageResponse(BaseModel):
    monthly_payment: float
    total_payment: float
    total_interest: float

@router.post("/calculate", response_model=MortgageResponse)
def calculate_mortgage(payload: MortgageRequest):
    P = payload.principal
    r = (payload.annual_interest_rate_pct / 100.0) / 12.0
    n = payload.years * 12

    if r == 0:
        monthly = P / n
    else:
        monthly = P * (r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

    total_payment = monthly * n
    total_interest = total_payment - P

    return MortgageResponse(
        monthly_payment=round(monthly, 2),
        total_payment=round(total_payment, 2),
        total_interest=round(total_interest, 2),
    )