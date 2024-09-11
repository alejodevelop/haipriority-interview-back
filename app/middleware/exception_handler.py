from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as exc:
            logging.error(f"HTTPException: {exc.detail}")
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        except ValueError as exc:
            logging.error(f"ValueError: {exc}")
            return JSONResponse(status_code=400, content={"detail": str(exc)})
        except Exception as exc:
            logging.error(f"Unhandled Exception: {exc}")
            return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})