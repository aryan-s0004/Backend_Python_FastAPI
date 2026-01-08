from typing import List, Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="Patient API Demo")

# Patient schema
class Patient(BaseModel):
    name: str
    age: int
    weight: Optional[float] = None
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None
    contact: Optional[Dict[str, str]] = None

# Insert patient using query parameters
@app.post("/patients/insert")
def insert_patient_data(name: str, age: int):
    return {
        "name": name,
        "age": age,
        "message": "Patient inserted successfully"
    }

# Update patient using request body
@app.put("/patients/update")
def update_patient_info(patient: Patient):
    return {
        "patient": patient,
        "message": "Patient updated successfully"
    }

# Health check endpoint
@app.get("/")
def root():
    return {"status": "Patient API running"}
