import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Obtén el logger
logger = logging.getLogger("APP_LOGGER")