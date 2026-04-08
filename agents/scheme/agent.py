import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_scheme_agent(user_data: dict, triage_result: dict) -> dict:
    prompt = f"""
You are a government scheme matching agent for informal workers in India.

Worker Profile:
- Occupation: {user_data.get('occupation')}
- Monthly Income: {user_data.get('monthly_income')} INR
- Location: {user_data.get('location')}
- Has Bank Account: {user_data.get('has_bank_account')}
- Has Aadhaar: {user_data.get('has_id')}
- Dependents: {user_data.get('dependents')}
- Financial Needs: {triage_result.get('financial_needs')}
- Documents Available: {triage_result.get('documents_have')}

Respond in this exact JSON format:
{{
  "matched_schemes": [
    {{
      "scheme_name": "PM Jan Dhan Yojana",
      "benefit": "Free bank account with Rs 10,000 overdraft",
      "eligibility_match": "high",
      "documents_required": ["aadhaar", "photo"],
      "application_steps": ["Visit nearest bank", "Fill Form A1"],
      "application_link": "https://pmjdy.gov.in",
      "monthly_benefit_inr": 0,
      "one_time_benefit_inr": 10000
    }}
  ],
  "priority_scheme": "PM Jan Dhan Yojana",
  "total_monthly_benefit_possible": 3500,
  "formalization_roadmap": ["Step 1: Open bank account", "Step 2: Get PAN card"]
}}
Include at least 4 real schemes. Respond with JSON only, no extra text.
"""
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)
