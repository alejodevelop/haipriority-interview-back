import importlib
import pkgutil
from fastapi import FastAPI

# Importo de manera automatica todos los routers que se encuentren en la carpeta controllers
def register_routers(app: FastAPI):
    package = 'app.controllers'
    for _, module_name, _ in pkgutil.iter_modules([package.replace('.', '/')]):
        module = importlib.import_module(f'{package}.{module_name}')
        if hasattr(module, 'router'):
            app.include_router(module.router)