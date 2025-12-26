from fastapi import FastAPI
from app.health import health_check

app = FastAPI(title="Production DevOps API")

@app.get("/")
def root():
    return {"message": "Service is running"}

@app.get("/health")
def health():
    return health_check()

