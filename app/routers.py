# Archivo para registrar routers
from fastapi import FastAPI
from app.controllers import usuario_controller, auth_controller

def register_routers(app: FastAPI):
    app.include_router(usuario_controller.router)
    app.include_router(auth_controller.router)