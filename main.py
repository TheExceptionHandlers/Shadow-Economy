from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from agents.triage.agent import run_triage_agent
from agents.credit.agent import run_credit_agent
from agents.scheme.agent import run_scheme_agent
from agents.fraud.agent import run_fraud_agent

app = FastAPI(title="ShadowEconomy AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorkerProfile(BaseModel):
    name: str
    occupation: str
    monthly_income: int
    monthly_expenses: int
    location: str
    has_bank_account: bool
    has_id: bool
    dependents: int
    income_stability: str
    years_in_occupation: int
    has_loans: bool
    loan_details: Optional[str] = "none"
    payment_method: Optional[str] = "cash"
    transaction_description: str

@app.get("/")
def root():
    return {"status": "ShadowEconomy AI is running"}

import time

@app.post("/analyze")
def analyze_worker(profile: WorkerProfile):
    user_data = profile.dict()
    
    for attempt in range(3):
        try:
            print("Running triage agent...")
            triage_result = run_triage_agent(user_data)

            print("Running credit agent...")
            credit_result = run_credit_agent(user_data, triage_result)

            print("Running scheme agent...")
            scheme_result = run_scheme_agent(user_data, triage_result)

            print("Running fraud agent...")
            fraud_result = run_fraud_agent(user_data, credit_result)

            return {
                "worker_name": profile.name,
                "triage": triage_result,
                "credit_score": credit_result,
                "schemes": scheme_result,
                "fraud_detection": fraud_result
            }
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(5)
            else:
                raise e

@app.get("/health")
def health():
    return {"status": "healthy"}