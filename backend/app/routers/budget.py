from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

router = APIRouter()

Frequency = Literal["weekly", "fortnightly", "monthly", "annual"]
Category = Literal["needs", "wants", "savings"]

class LineItem(BaseModel):
    name: Optional[str] = None
    amount: float = Field(ge=0)
    frequency: Frequency = "monthly"
    category: Optional[Category] = None

class BudgetRequest(BaseModel):
    incomes: List[LineItem] = []
    expenses: List[LineItem] = []

class BudgetResponse(BaseModel):
    monthly_income: float
    monthly_expenses: float
    net_savings: float
    recommended_50_30_20: dict
    actual_by_category: dict
    flags: dict

FREQ_TO_MONTH = {
    "weekly": 52 / 12,
    "fortnightly": 26 / 12,
    "monthly": 1.0,
    "annual": 1 / 12,
}

def to_monthly(amount: float, freq: Frequency) -> float:
    return amount * FREQ_TO_MONTH[freq]

@router.post("/analyze", response_model=BudgetResponse)
def analyze_budget(payload: BudgetRequest):
    monthly_income = sum(to_monthly(i.amount, i.frequency) for i in payload.incomes)
    monthly_expenses = sum(to_monthly(e.amount, e.frequency) for e in payload.expenses)
    net_savings = monthly_income - monthly_expenses

    # 50/30/20 recommendation based on income
    needs_budget = monthly_income * 0.5
    wants_budget = monthly_income * 0.3
    savings_budget = monthly_income * 0.2

    # Actuals by category
    actual = {"needs": 0.0, "wants": 0.0, "savings": 0.0}
    for e in payload.expenses:
        cat = e.category if e.category in actual else "needs"  # default to needs if unspecified
        actual[cat] += to_monthly(e.amount, e.frequency)

    flags = {
        "overspend_needs": actual["needs"] > needs_budget,
        "overspend_wants": actual["wants"] > wants_budget,
        "savings_gap": actual["savings"] < savings_budget,
        "is_deficit": net_savings < 0,
    }

    return BudgetResponse(
        monthly_income=round(monthly_income, 2),
        monthly_expenses=round(monthly_expenses, 2),
        net_savings=round(net_savings, 2),
        recommended_50_30_20={
            "needs": round(needs_budget, 2),
            "wants": round(wants_budget, 2),
            "savings": round(savings_budget, 2),
        },
        actual_by_category={k: round(v, 2) for k, v in actual.items()},
        flags=flags,
    )