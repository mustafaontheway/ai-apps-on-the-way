from fastapi import FastAPI

app = FastAPI()

CITIES = [
    {"name": "x city", "country": "y country", "mayor": "person z", "population": 4_000_000},
    {"name": "a city", "country": "b country", "mayor": "person c", "population": 2_600_000},
    {"name": "d city", "country": "e country", "mayor": " personf", "population": 2_000_000},
]

@app.get("/all-cities")
async def get_cities():
  
    return CITIES
