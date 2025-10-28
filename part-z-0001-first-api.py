from fastapi import FastAPI

app = FastAPI()

@app.get("/why")
async def why():
  
    return {"Why FastAPI?" : "For AI apps!.."}
