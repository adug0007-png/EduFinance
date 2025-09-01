from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import budget, savings, mortgage, tax, edu_cost

app = FastAPI(title="WealthWave API", version="0.1.0")

# CORS for local frontend dev
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(budget.router, prefix="/api/budget", tags=["Budget"])
app.include_router(savings.router, prefix="/api/savings", tags=["Savings"])
app.include_router(mortgage.router, prefix="/api/mortgage", tags=["Mortgage"])
app.include_router(tax.router, prefix="/api/tax", tags=["Tax"])
app.include_router(edu_cost.router, prefix="/api/edu-cost", tags=["Education Cost"]) 

@app.get("/")
def root():
    return {"service": "WealthWave API", "status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)