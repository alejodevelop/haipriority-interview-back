from fastapi import FastAPI
import uvicorn
from app.database import Base, engine
from app.config import settings, origins
from app.routers import register_routers
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.exception_handler import ExceptionHandlerMiddleware
from app.models.events import audit_events

# Inicializa la aplicación FastAPI
app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)

# Configura el CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Evento de inicio (startup) para crear las tablas de la base de datos si aun no existen
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


# Agregar el middleware de manejo de excepciones
app.add_middleware(ExceptionHandlerMiddleware)

# Registra los routers
register_routers(app)

# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
