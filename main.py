"""
app.main.py
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routers import EpubRouter, V2

# ############
# FastAPI App
# ############

APP = FastAPI(
    title="Epub information",
    description=(
        "Obtener datos de un libro epub"
    ),
    version="2.0.4",
    docs_url="/",
    redoc_url="/docs"
)

# Enable CORS.
APP.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
APP.add_middleware(GZipMiddleware, minimum_size=1000)

# ################
# Routing
# ################


# Include routers.
APP.include_router(EpubRouter, prefix="/epub", tags=["EpubRouter"])
APP.include_router(V2, prefix="/v2", tags=["v2"])


# Running of app.
if __name__ == "__main__":
    uvicorn.run(
        "main:APP", host="127.0.0.1", port=8000, log_level="info",
    )
