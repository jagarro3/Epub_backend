"""app.routers.v2"""
from fastapi import APIRouter

V2 = APIRouter()

@V2.get("/sources")
async def get_confirmed():
    return {"message": "Hello V2 Bigger Applications!"}