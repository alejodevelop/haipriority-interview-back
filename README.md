# haipriority-interview-back

## Descripción del Proyecto

Este proyecto es una API backend desarrollada en Python utilizando el framework FastAPI. La API maneja operaciones CRUD
para diferentes modelos como `CreditCard`, `DebitCard` y `Loan`, y registra eventos de auditoría para cada operación
realizada en estos modelos.

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tu-usuario/haipriority-interview-back.git
    cd haipriority-interview-back
    ```

2. **Crear y activar un entorno virtual:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```sh
    pip install -r requirements.txt
    ```

## Ejecución

1. **Iniciar el servidor:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Acceder a la documentación interactiva:**

   Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para ver la documentación interactiva generada por Swagger.

## Puntos Clave del Proyecto

- **FastAPI:** Utilizado para crear la API de manera rápida y eficiente.
- **SQLAlchemy:** ORM utilizado para interactuar con la base de datos.
- **Alembic:** Herramienta de migración de base de datos para manejar cambios en el esquema.
- **Eventos de Auditoría:** Implementados para registrar todas las operaciones CRUD en los modelos `CreditCard`,
  `DebitCard` y `Loan`.
- **Autenticación:** Implementada para asegurar que solo usuarios autenticados puedan realizar operaciones en la API.
- **Validación de Datos:** Realizada utilizando Pydantic para asegurar que los datos de entrada sean correctos.

## Estructura del Proyecto

- `app/`: Contiene la lógica principal de la aplicación.
    - `models/`: Define los modelos de la base de datos.
        - `auditlog_model.py`
        - `creditcard_model.py`
        - `debitcard_model.py`
        - `loan_model.py`
    - `schemas/`: Define los esquemas de Pydantic para la validación de datos.
        - `auditlog_schema.py`
        - `creditcard_schema.py`
        - `debitcard_schema.py`
        - `loan_schema.py`
    - `services/`: Contiene la lógica de negocio.
        - `auditlog_service.py`
        - `creditcard_service.py`
        - `debitcard_service.py`
        - `loan_service.py`
    - `controllers/`: Define los endpoints de la API.
        - `auth_controller.py`
        - `auditlog_controller.py`
        - `creditcard_controller.py`
        - `debitcard_controller.py`
        - `loan_controller.py`
    - `events/`: Contiene los eventos de auditoría.
        - `audit_events.py`
    - `config.py`: Configuración de la api.
    - `database.py`: Contiene las configuraciones de la base de datos.
    - `main.py`: Punto de entrada de la aplicación.
    - `router.py`: Define los routers de la API.
- `tests/`: Contiene los futuros tests del proyecto.

