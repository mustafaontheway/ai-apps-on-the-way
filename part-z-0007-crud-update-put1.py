from fastapi import FastAPI, Body

app = FastAPI()

CITIES = [
    {"name": "x city", "country": "y country", "mayor": "person z", "population": 4_000_000, "is_metropolitan": True},
    {"name": "a city", "country": "b country", "mayor": "person c", "population": 2_600_000, "is_metropolitan": True},
    {"name": "d city", "country": "e country", "mayor": " person f", "population": 2_000_000, "is_metropolitan": True},
    {"name": "k city", "country": "x country", "mayor": " person w", "population": 312_000, "is_metropolitan": False},
    {"name": "m city", "country": "x country", "mayor": " person k", "population": 214_000, "is_metropolitan": False},
]

@app.get("/all-cities")
async def get_cities():
    return CITIES

@app.get("/cities/{city_name}")
async def get_city(city_name: str):
    for city in CITIES:
        if city.get("name").casefold() == city_name.casefold():
            return city
        
@app.get("/all-cities-by-sizes")
async def get_city_by_metropolitan(big: bool):
    filtered_cities = []
    for city in CITIES:
        if city["is_metropolitan"] == big:
            filtered_cities.append(city)
    return filtered_cities

@app.post("/all-cities/add-city")
async def add_city(new_city = Body()):
    CITIES.append(new_city)
    
    
@app.put("/cities/{city_name}") 
async def update_city(city_name: str, updated_city = Body()):
    
    for i in range(len(CITIES)):
        if CITIES[i].get("name").casefold() == city_name.casefold():
            
            CITIES[i] = updated_city
            
            return {"message": f"City '{city_name}' updated successfully", "new_data": updated_city}
            
