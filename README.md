# 🤖 AI Trip Planner: An Agentic Approach  

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![CI](https://github.com/encoder43/AI_Trip_Planner/actions/workflows/ci.yml/badge.svg)](https://github.com/encoder43/AI_Trip_Planner/actions)  

An advanced, AI-powered travel planning agent that goes beyond simple scripts.  
This project leverages an **autonomous agent built with LangGraph** to reason, use real-time tools, and construct comprehensive, dynamic travel itineraries from a single user prompt.  

---

## ✨ Project Overview  

The **AI Trip Planner** is an end-to-end application demonstrating the power of **agentic workflows** in large language models.  
Instead of following a fixed, pre-defined logic, the system uses a **ReAct (Reasoning + Acting)** framework.  

🔹 The agent analyzes a travel request, breaks it down into steps, and autonomously decides which tools to use — checking weather, estimating hotel costs, converting currencies, etc.  
🔹 It then compiles all this into a **personalized travel plan** that feels professional and context-aware.  

This project highlights a modern AI application stack: agentic reasoning at the core, APIs for communication, and an interactive frontend for end users.  

---

## 🚀 Features  

- 🌦️ **Real-time Weather Forecasts** for destinations.  
- 🏛️ **Tourist Attractions & Local Activities** suggestions.  
- 🏨 **Hotel Cost Estimation** tailored to user preferences.  
- 💱 **Currency Conversion** for budgets across countries.  
- 🗺️ **Dynamic Itinerary Generation** (day-by-day plan).  
- 💰 **Expense Calculation** with summarized cost breakdowns.  
- 📝 **Trip Summary Report** (concise overview).  

---

## 🛠️ Tech Stack & Architecture  

| Component         | Technology                                       | Description                                                                 |
| ----------------- | ------------------------------------------------ | --------------------------------------------------------------------------- |
| **Agent Backend** | `LangGraph`, `LangChain`, `Python`               | Core reasoning engine: state graph that orchestrates tool-use and logic.    |
| **API Layer**     | `FastAPI`                                        | High-performance REST API exposing planning services.                       |
| **Frontend**      | `Streamlit` / `HTML + CSS + JS`                  | UI for user inputs and displaying itineraries.                              |
| **Deployment**    | `Docker`, `Uvicorn`, `Render` / `Vercel`         | Containerized deployment for cloud readiness.                               |

### 🔄 Workflow  

The agent runs on a **ReAct Loop**:  
1. **Reason** → Decide the next step.  
2. **Act** → Call the right tool (e.g., Weather API).  
3. **Observe** → Learn from output & continue until plan is ready.  

---

## ⚙️ Setup & Installation  

### 1. Prerequisites  
- Python **3.11+**  
- [uv](https://github.com/astral-sh/uv) (or `pip`)  
- Git  

### 2. Clone Repository  
```bash
git clone https://github.com/encoder43/AI_Trip_Planner.git
cd AI_Trip_Planner
```

### 3. Create Virtual Environment & Install Dependencies  

```bash
# Create environment
uv venv

# Activate environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 4. Configure API Keys  

Copy `.env.example` → `.env` and add your keys:  

```ini
# .env
GROQ_API_KEY="your_groq_or_openai_api_key"
HUGGINGFACE_API_KEY="your_huggingface_api_key"
OPENWEATHERMAP_API_KEY="your_weather_api_key"
EXCHANGE_RATE_API_KEY="your_exchange_rate_api_key"
```

---

## ▶️ Usage  

### 1. Run Backend (FastAPI)  

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API available at 👉 [http://localhost:8000](http://localhost:8000)  

### 2. Run Frontend  

```bash
# If using Streamlit
streamlit run app.py
```

Or simply open `index.html` in a browser for the static UI.  

---

## ☁️ Deployment  

- **Dockerized Setup** → included `Dockerfile` for container builds.  
- **CI/CD** → ready for GitHub Actions or similar pipelines.  
- **Cloud Hosting** → deploy on Render, Vercel, AWS Elastic Beanstalk, etc.  

---

## 🔮 Future Enhancements  

- [ ] Integration with **real-time flight booking APIs**  
- [ ] **User authentication** to save/manage travel plans  
- [ ] Feedback & rating loop for continuous improvement  
- [ ] Restaurant + event recommendations  

---

## 📜 License  

Licensed under the **MIT License**. See `LICENSE` for details.  

---

## 🙏 Acknowledgements  

- To all the beutifull hearts who contributed to open source 
- Built with the amazing **LangChain + FastAPI** open-source ecosystem.  

---
