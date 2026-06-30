from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.telemetry import router as telemetry_router
from app.api.status import router as status_router
app = FastAPI(
    title="CERT-SAT Backend",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(status_router)
app.include_router(telemetry_router)

@app.get("/")
def root():
    return {"message": "CERT-SAT Backend Running"}