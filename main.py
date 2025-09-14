from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, JSONResponse
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# --- CORS middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Serve index.html at root ---
@app.get("/")
def serve_index():
    index_path = os.path.join(os.getcwd(), "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse(status_code=404, content={"error": "index.html not found"})

# --- Request model ---
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

# --- AI Query Endpoint ---
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print("Received Query:", query.dict())

        # Initialize GraphBuilder
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()  # compiled StateGraph

        # Build prompt
        user_prompt = f"""
        Plan a trip for {query.travelers} traveler(s) from {query.start_place} to {query.destination}.
        Dates: {query.start_date} → {query.end_date}.
        Budget: {query.budget} {query.currency}.
        Travel style: {query.preference}.
        Accommodation preference: {query.accommodation}.
        Special interests: {", ".join(query.interests) if query.interests else "None"}.
        """

        messages = {"messages": [user_prompt]}

        # Run the graph asynchronously
        output = await react_app.ainvoke(messages)

        # Extract final response
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
