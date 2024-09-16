from openai import OpenAI

from app.utils.logging_config import logger

# client = OpenAI()

import openai
import os
from dotenv import load_dotenv

# Convertir audit_data a JSON string
import json


def calculate_credit_limit(user_id: int) -> float:
    '''

    # Carga las variables de entorno desde el archivo .env
    load_dotenv()

    # Configura tu clave API de OpenAI
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Define el JSON de auditoría (ejemplo de datos)
    audit_data = {
        "debito": {
            "saldo_actual": 500,
            "transacciones_recientes": [
                {"monto": -50, "fecha": "2024-09-15"},
                {"monto": 100, "fecha": "2024-09-10"}
            ]
        },
        "credito": {
            "limite": 2000,
            "saldo_actual": 1000,
            "pagos_reales": [
                {"monto": -100, "fecha": "2024-09-14"},
                {"monto": -50, "fecha": "2024-09-10"}
            ],
            "deuda_abierta": 500
        },
        "prestamos": {
            "prestamos_abiertos": [
                {"monto": 1000, "estado": "pagado"},
                {"monto": 500, "estado": "pendiente"}
            ]
        }
    }

    audit_data_json = json.dumps(audit_data)

    # Realiza la solicitud a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data analyst and credit expert."},
            {
                "role": "user",
                "content": (
                    f"Evaluate the following audit data and provide a credit score between 0 and 1. "
                    f"0 indicates poor credit with potential risk, while 1 indicates excellent credit. "
                    f"Consider factors such as loan repayments, open loans, balance in debit cards, etc.\n\n"
                    f"Audit Data:\n{audit_data_json}"
                )
            }
        ]
    )

    # Extrae el resultado
    credit_score = response.choices[0].message['content']
    logger.info("Credit Score:", credit_score)


    '''
    # En implementacion, de momento solo permito 10 mil dolares de credit
    return 10000
