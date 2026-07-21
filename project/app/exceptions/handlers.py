from fastapi import Request
from fastapi.responses import JSONResponse


class TelemetryException(Exception):
    def __init__(self, message: str):
        self.message = message


async def telemetry_exception_handler(
    request: Request,
    exc: TelemetryException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "status_code": 400,
            "error": exc.message,
            "path": request.url.path
        }
    )