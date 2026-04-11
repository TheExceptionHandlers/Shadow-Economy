# ShadowEconomy AI

> 700M informal workers in APAC have no financial identity. ShadowEconomy AI fixes that using 4 Gemini-powered agents in under 60 seconds.

## Live Demo
https://shadoweconomy-ai-416047014535.asia-southeast1.run.app

## What it does

ShadowEconomy AI is a multi-agent system that builds a complete financial profile for informal workers who are invisible to banks, insurance providers, and government welfare systems.

A worker describes their situation in plain language. Four AI agents analyze their profile and return:

- An alternative credit score built from behavioral signals
- Matched government welfare schemes with exact application steps
- A step-by-step formalization roadmap
- Exploitation and predatory lending detection

## Agents

| Agent | Role |
|---|---|
| Triage Agent | Assesses vulnerability level, top financial needs, document gaps |
| Credit Agent | Generates behavioral credit score (300-900) with no bank history needed |
| Scheme Agent | Matches worker to 200+ real APAC government schemes |
| Fraud Agent | Detects wage theft, predatory lending, middleman exploitation |

## Tech Stack

- **LLM:** Gemini 2.5 Flash via Google GenAI SDK
- **Agent Orchestration:** Google ADK
- **Backend:** Python 3.11 + FastAPI
- **Frontend:** React 18
- **Deployment:** Google Cloud Run
- **Build:** Docker multi-stage (Node.js + Python)

## Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Google Cloud account with billing enabled
- Gemini API key from https://aistudio.google.com/app/apikey

### Local Development

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/shadoweconomy-ai.git
cd shadoweconomy-ai

# Backend setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Add your API key
echo GEMINI_API_KEY=your_key_here > .env

# Run backend
uvicorn main:app --port 8000

# Frontend setup (new terminal)
cd frontend# ShadowEconomy AI

> 700M informal workers in APAC have no financial identity. ShadowEconomy AI fixes that using 4 Gemini-powered agents in under 60 seconds.

## Live Demo
https://shadoweconomy-ai-416047014535.asia-southeast1.run.app

## What it does

ShadowEconomy AI is a multi-agent system that builds a complete financial profile for informal workers who are invisible to banks, insurance providers, and government welfare systems.

A worker describes their situation in plain language. Four AI agents analyze their profile and return:

- An alternative credit score built from behavioral signals
- Matched government welfare schemes with exact application steps
- A step-by-step formalization roadmap
- Exploitation and predatory lending detection

## Agents

| Agent | Role |
|---|---|
| Triage Agent | Assesses vulnerability level, top financial needs, document gaps |
| Credit Agent | Generates behavioral credit score (300-900) with no bank history needed |
| Scheme Agent | Matches worker to 200+ real APAC government schemes |
| Fraud Agent | Detects wage theft, predatory lending, middleman exploitation |

## Tech Stack

- **LLM:** Gemini 2.5 Flash via Google GenAI SDK
- **Agent Orchestration:** Google ADK
- **Backend:** Python 3.11 + FastAPI
- **Frontend:** React 18
- **Deployment:** Google Cloud Run
- **Build:** Docker multi-stage (Node.js + Python)

## Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Google Cloud account with billing enabled
- Gemini API key from https://aistudio.google.com/app/apikey

### Local Development

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/shadoweconomy-ai.git
cd shadoweconomy-ai

# Backend setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Add your API key
echo GEMINI_API_KEY=your_key_here > .env

# Run backend
uvicorn main:app --port 8000

# Frontend setup (new terminal)
cd frontend
npm install
npm start
```

### Deploy to Cloud Run

```bash
gcloud run deploy shadoweconomy-ai --source . --region asia-southeast1 --allow-unauthenticated --set-env-vars GEMINI_API_KEY=your_key_here --memory 2Gi --timeout 300
```

## Project Structure
npm install
npm start
```

### Deploy to Cloud Run

```bash
gcloud run deploy shadoweconomy-ai --source . --region asia-southeast1 --allow-unauthenticated --set-env-vars GEMINI_API_KEY=your_key_here --memory 2Gi --timeout 300
```

## Project Structure