from fastapi import FastAPI
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

app = FastAPI()

class Telemetry(BaseModel):
    vehicle_id:StrictStr
    timestamp:StrictInt
    speed:StrictFloat
    engine_temp:StrictFloat
    rpm:StrictInt
    
@app.post("/telemetry")
def ingest_telemetry(data:Telemetry):
    return {
        "message": "telemetry received",
        "vehicle id": data.vehicle_id
    }

@app.get("/")
def health_check():
    return {"status": "Server is running..."}