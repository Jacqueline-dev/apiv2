import uvicorn
from fastapi import fastAPI

from src.responses import TrendItem
from src.services import  get_trends_from_mongo, save_trends


app = fastAPI()


@app.get('/trends', response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


if __name__ == '__main__':
    trends = get_trends_from_mongo()

    if not trends:
        save_trends()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
