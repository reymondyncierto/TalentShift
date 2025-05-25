from fastapi import FastAPI
from routers.conversion_routes import router as conversion_router

app = FastAPI()

app.include_router(conversion_router, prefix="/convert", tags=["convert"])

@app.get("/")
def index():
  return {"message": "Hello, World!"}

