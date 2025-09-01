from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()

class EduCostRequest(BaseModel):
    years: int = Field(gt=0)
    tuition_per_year: float = Field(ge=0)
    living_cost_per_year: float = Field(ge=0)
    scholarships_per_year: Optional[float] = Field(default=0, ge=0)

class EduCostResponse(BaseModel):
    total_tuition: float
    total_living: float
    total_scholarships: float
    total_cost: float

@router.post("/estimate", response_model=EduCostResponse)
def estimate_cost(payload: EduCostRequest):
    total_tuition = payload.tuition_per_year * payload.years
    total_living = payload.living_cost_per_year * payload.years
    total_scholarships = (payload.scholarships_per_year or 0) * payload.years
    total_cost = total_tuition + total_living - total_scholarships

    return EduCostResponse(
        total_tuition=round(total_tuition, 2),
        total_living=round(total_living, 2),
        total_scholarships=round(total_scholarships, 2),
        total_cost=round(total_cost, 2),
    )