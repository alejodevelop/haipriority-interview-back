# Centraliza la configuración de la aplicación
class Settings:
    TITLE = "My FastAPI App"
    DESCRIPTION = "API para manejar usuarios y otros recursos"
    VERSION = "1.0.0"
    DOCS_URL = "/docs"
    REDOC_URL = "/redoc"

settings = Settings()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:4200",
]
