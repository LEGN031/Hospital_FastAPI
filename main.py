from fastapi import FastAPI
from routers import medicoRouter, pacienteRouter, EnfermeraRouter, citaRouter

app = FastAPI(
    title="API de Gestion de Medicos y Pacientes",
    description="API para gestionar medicos y pacientes en un sistema de salud",
    version="1.0.0"
)

app.include_router(medicoRouter.router)
app.include_router(pacienteRouter.router)
app.include_router(EnfermeraRouter.router)
app.include_router(citaRouter.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Medical and Patient Management API"}
