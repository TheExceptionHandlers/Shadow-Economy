import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_fraud_agent(user_data: dict, credit_result: dict) -> dict:
    prompt = f"""
You are a financial exploitation detection agent protecting informal workers in APAC.

Worker Profile:
- Occupation: {user_data.get('occupation')}
- Monthly Income: {user_data.get('monthly_income')} INR
- Monthly Expenses: {user_data.get('monthly_expenses')} INR
- Has Loans: {user_data.get('has_loans')}
- Loan Details: {user_data.get('loan_details', 'none')}
- Payment Method: {user_data.get('payment_method', 'cash')}
- Transaction Description: {user_data.get('transaction_description')}
- Credit Score: {credit_result.get('credit_score')}

Respond in this exact JSON format:
{{
  "exploitation_risk": "medium",
  "fraud_flags": [
    {{
      "type": "predatory_lending",
      "description": "Loan interest appears above legal limit",
      "severity": "high",
      "recommended_action": "Contact NBFC ombudsman at https://ombudsman.rbi.org.in"
    }}
  ],
  "wage_fairness": "underpaid",
  "market_rate_income": 18000,
  "income_gap_inr": 6000,
  "legal_protections_applicable": ["Minimum Wages Act 1948"],
  "immediate_actions": ["Document all wage payments"],
  "safe_resources": ["Labour Department: 1800-11-8001"]
}}
Respond with JSON only, no extra text.
"""
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)
