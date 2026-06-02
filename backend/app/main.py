# FastAPI is the framework that handles HTTP requests and routes them to the right function
from fastapi import FastAPI

# Import the settings instance to access environment variables defined in .env
from app.core.config import settings

# Create the FastAPI application — all routes and middleware attach to this object
app = FastAPI()

# @app.get("/") registers this function as the handler for GET requests to the root path
@app.get("/")
def root():
    # f-string interpolates settings.APP_NAME into the string at runtime
    # Returning a dict causes FastAPI to automatically serialize it as a JSON response
    return {"message": f"{settings.APP_NAME} API is running"}
