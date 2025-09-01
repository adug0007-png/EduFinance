from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import math

router = APIRouter()

class SavingsRequest(BaseModel):
    goal_amount: float = Field(gt=0)
    current_savings: float = Field(default=0, ge=0)
    target_months: Optional[int] = Field(default=None, gt=0)
    target_date: Optional[str] = None  # ISO date string, e.g., 2025-12-01
    annual_interest_rate: Optional[float] = Field(default=0, ge=0)  # e.g., 0.03 for 3%

class SavingsResponse(BaseModel):
    months: int
    required_monthly_no_interest: float
    required_weekly_no_interest: float
    required_monthly_with_interest: Optional[float] = None

@router.post("/plan", response_model=SavingsResponse)
def savings_plan(payload: SavingsRequest):
    # Derive months
    months = payload.target_months
    if months is None and payload.target_date:
        try:
            target = datetime.fromisoformat(payload.target_date)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid target_date: {e}")
        days = max(0, (target - datetime.now()).days)
        months = max(1, math.ceil(days / 30.4))
    if months is None:
        raise HTTPException(status_code=400, detail="Either target_months or target_date must be provided")

    remaining = max(0.0, payload.goal_amount - payload.current_savings)
    monthly_no_interest = remaining / months
    weekly_no_interest = monthly_no_interest * 12 / 52

    monthly_with_interest = None
    if payload.annual_interest_rate and payload.annual_interest_rate > 0:
        r = payload.annual_interest_rate / 12.0
        n = months
        # Future value with monthly contributions: FV = P * [((1+r)^n - 1) / r]
        # Solve for P: P = FV * r / ((1+r)^n - 1)
        try:
            monthly_with_interest = (remaining * r) / (math.pow(1 + r, n) - 1)
        except ZeroDivisionError:
            monthly_with_interest = monthly_no_interest

    return SavingsResponse(
        months=months,
        required_monthly_no_interest=round(monthly_no_interest, 2),
        required_weekly_no_interest=round(weekly_no_interest, 2),
        required_monthly_with_interest=round(monthly_with_interest, 2) if monthly_with_interest is not None else None,
    )