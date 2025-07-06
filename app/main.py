from fastapi     import FastAPI
from app.routers import indicators, users

app = FastAPI(title="Saturn Analytics API")

app.include_router(indicators.router, prefix="/indicators", tags=["Indicators"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Saturn Analytics API online"}
