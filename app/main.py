from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import user_controller
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.exception_handler import ExceptionHandlerMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="My FastAPI App",
    description="API para manejar usuarios y otros recursos",
    version="1.0.0",
    docs_url="/docs",  # URL para Swagger UI
    redoc_url="/redoc"  # URL para Redoc
)

# Startup event handler
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Para conexiones con frontend como React o Angular
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar el middleware de manejo de excepciones
app.add_middleware(ExceptionHandlerMiddleware)

# Registra los routers de los controladores
app.include_router(user_controller.router)

# Punto de entrada para que la aplicación corra
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)