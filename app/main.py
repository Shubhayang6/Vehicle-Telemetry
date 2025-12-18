from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Telemetry(BaseModel):
    vehicle_id:str
    timestamp:int
    speed:float
    engine_temp:float
    rpm:int
    
@app.post("/Telemetry")
def ingest_telemetry(data:Telemetry):
    return {
        "message": "telemetry received",
        "vehicle id": data.vehicle_id
    }

@app.get("/")
def health_check():
    return {"status": "Server is running..."}