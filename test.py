import httpx
import json

data = {
    "name": "Ramu",
    "occupation": "street vendor",
    "monthly_income": 8000,
    "monthly_expenses": 6000,
    "location": "Chennai",
    "has_bank_account": False,
    "has_id": True,
    "dependents": 3,
    "income_stability": "irregular",
    "years_in_occupation": 5,
    "has_loans": True,
    "loan_details": "informal moneylender at 5% monthly",
    "payment_method": "cash",
    "transaction_description": "sells vegetables daily at local market, earns between 200-400 per day"
}

r = httpx.post("http://127.0.0.1:8000/analyze", json=data, timeout=60)
print("STATUS:", r.status_code)
print("RESPONSE:", json.dumps(r.json(), indent=2))