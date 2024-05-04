from fastapi import FastAPI
import uvicorn

from configs.config import settings
from api_v1.routers import all_routers

app = FastAPI()

for router in all_routers:
    app.include_router(router)
    
if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.app.host, port=settings.app.port, reload=True)
