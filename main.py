from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from starlette.responses import JSONResponse
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QueryRequest(BaseModel):
    start_place: str
    destination: str
    start_date: str
    end_date: str
    budget: float
    currency: str
    travelers: int
    preference: str
    accommodation: str
    interests: Optional[List[str]] = []


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print("Received Query:", query.dict())

        # Initialize graph
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()   # compiled StateGraph (Option 2)

        # Build natural language prompt
        user_prompt = f"""
        Plan a trip for {query.travelers} traveler(s) from {query.start_place} to {query.destination}.
        Dates: {query.start_date} → {query.end_date}.
        Budget: {query.budget} {query.currency}.
        Travel style: {query.preference}.
        Accommodation preference: {query.accommodation}.
        Special interests: {", ".join(query.interests) if query.interests else "None"}.
        """

        # Messages format for the graph
        messages = {"messages": [user_prompt]}

        # Run the graph
        output = await react_app.ainvoke(messages)  # 👈 async call since you're inside FastAPI

        # Extract final response
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
