import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_triage_agent(user_data: dict) -> dict:
    prompt = f"""
You are a financial triage agent for informal workers in APAC.

Given this worker profile:
- Name: {user_data.get('name')}
- Occupation: {user_data.get('occupation')}
- Monthly Income: {user_data.get('monthly_income')} INR
- Location: {user_data.get('location')}
- Has Bank Account: {user_data.get('has_bank_account')}
- Has Aadhaar/ID: {user_data.get('has_id')}
- Number of Dependents: {user_data.get('dependents')}
- Transaction Description: {user_data.get('transaction_description')}

Respond in this exact JSON format:
{{
  "financial_needs": ["need1", "need2", "need3"],
  "vulnerability_level": "high",
  "documents_have": ["aadhaar"],
  "documents_needed": ["pan card", "bank account"],
  "immediate_risks": ["no insurance"],
  "summary": "one sentence summary"
}}
Respond with JSON only, no extra text.
"""
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)
