# external imports 
from fastapi import FastAPI

app = FastAPI()

# the main scraping function
from main import scrape

@app.post("/scrape/{user_id}/{platform_code}", status_code=200)
async def scrape(user_id: int, platform_code: str):
    return scrape(user_id=user_id, platform_code=platform_code)
    
