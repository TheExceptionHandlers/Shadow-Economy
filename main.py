from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from agents.triage.agent import run_triage_agent
from agents.credit.agent import run_credit_agent
from agents.scheme.agent import run_scheme_agent
from agents.fraud.agent import run_fraud_agent
import os
import time

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

@app.get("/health")
def health():
    return {"status": "healthy"}

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

frontend_path = os.path.join(os.path.dirname(__file__), "frontend", "build")

if os.path.exists(frontend_path):
    static_path = os.path.join(frontend_path, "static")
    if os.path.exists(static_path):
        app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
def serve_root():
    index = os.path.join(frontend_path, "index.html")
    if os.path.exists(index):
        return FileResponse(index)
    return {"status": "ShadowEconomy AI is running"}

@app.get("/{full_path:path}")
def serve_frontend(full_path: str):
    file_path = os.path.join(frontend_path, full_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    index = os.path.join(frontend_path, "index.html")
    if os.path.exists(index):
        return FileResponse(index)
    return {"status": "ShadowEconomy AI is running"}