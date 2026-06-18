from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="BurguerRank API",
    description="API for managing the BurguerRank application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app= "main:app", host="localhost", port=8000, reload=True)

