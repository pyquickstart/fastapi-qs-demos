from fastapi import FastAPI

app = FastAPI(
    title="Cryptocurrency Manager",
    version="1.0.0",
    description="API for managing cryptocurrency portfolios",
)


@app.get("/status")
def api_status():
    return {"status": "ok"}
