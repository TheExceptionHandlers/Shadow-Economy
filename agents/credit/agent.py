import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_credit_agent(user_data: dict, triage_result: dict) -> dict:
    prompt = f"""
You are an alternative credit scoring agent for informal workers with no credit history.

Worker Profile:
- Occupation: {user_data.get('occupation')}
- Monthly Income: {user_data.get('monthly_income')} INR
- Income Stability: {user_data.get('income_stability')}
- Years in Occupation: {user_data.get('years_in_occupation')}
- Has Bank Account: {user_data.get('has_bank_account')}
- Monthly Expenses: {user_data.get('monthly_expenses')} INR
- Has Loans: {user_data.get('has_loans')}
- Dependents: {user_data.get('dependents')}
- Vulnerability: {triage_result.get('vulnerability_level')}

Respond in this exact JSON format:
{{
  "credit_score": 620,
  "score_band": "medium",
  "max_loan_eligible": 25000,
  "recommended_loan_type": "microfinance group loan",
  "score_factors_positive": ["stable occupation"],
  "score_factors_negative": ["no bank account"],
  "improvement_steps": ["open Jan Dhan account"],
  "lender_recommendations": ["Bandhan Bank", "MUDRA Loan"]
}}
Respond with JSON only, no extra text.
"""
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)
