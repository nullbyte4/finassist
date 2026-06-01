from fastapi import FastAPI # Import FastAPI

app = FastAPI() #Creating an instance from FastAPI

@app.get("/")
def root():
    return {"message": "FinAssist API Funcionando"}
