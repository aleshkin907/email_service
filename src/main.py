from fastapi import FastAPI

from api_v1.routers import all_routers


app = FastAPI()

for router in all_routers:
    app.include_router(router, prefix="/api/v1")
