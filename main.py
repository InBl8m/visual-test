from scripts.setup_database import setup_database
from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI()
setup_database()
app.include_router(api_router, prefix="/users", tags=["users"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
