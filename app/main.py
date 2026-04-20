from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import  usuario, camion, carga

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router)
app.include_router(camion.router)

app.include_router(carga.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI JWT Auth Example"}

