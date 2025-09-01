from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Optional

router = APIRouter()

class Bracket(BaseModel):
    threshold: float = Field(ge=0)  # lower bound inclusive
    rate: float = Field(ge=0)  # e.g., 0.19 for 19%

class TaxRequest(BaseModel):
    annual_salary: float = Field(ge=0)
    brackets: Optional[List[Bracket]] = None  # if None, caller must provide later; we avoid hard-coding
    medicare_levy_rate: float = Field(default=0.02, ge=0)
    super_rate: float = Field(default=0.115, ge=0)

class TaxResponse(BaseModel):
    taxable_income: float
    income_tax: float
    medicare_levy: float
    net_income_after_tax: float
    employer_super: float


def compute_tax(income: float, brackets: List[Bracket]) -> float:
    # Sort brackets by threshold
    bs = sorted(brackets, key=lambda b: b.threshold)
    tax = 0.0
    for i, b in enumerate(bs):
        lower = b.threshold
        upper = bs[i + 1].threshold if i + 1 < len(bs) else None
        if income <= lower:
            break
        band_amount = (income if upper is None else min(income, upper)) - lower
        if band_amount > 0:
            tax += band_amount * b.rate
    return tax

@router.post("/calc", response_model=TaxResponse)
def calc_tax(payload: TaxRequest):
    if payload.brackets is None or len(payload.brackets) == 0:
        # Avoid hard-coding AU tax brackets; require client to pass them
        return TaxResponse(
            taxable_income=payload.annual_salary,
            income_tax=0.0,
            medicare_levy=round(payload.annual_salary * payload.medicare_levy_rate, 2),
            net_income_after_tax=round(payload.annual_salary * (1 - payload.medicare_levy_rate), 2),
            employer_super=round(payload.annual_salary * payload.super_rate, 2),
        )

    income = payload.annual_salary
    income_tax = compute_tax(income, payload.brackets)
    medicare = income * payload.medicare_levy_rate
    net = income - income_tax - medicare
    employer_super = income * payload.super_rate

    return TaxResponse(
        taxable_income=round(income, 2),
        income_tax=round(income_tax, 2),
        medicare_levy=round(medicare, 2),
        net_income_after_tax=round(net, 2),
        employer_super=round(employer_super, 2),
    )