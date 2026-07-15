import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.logger import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs request path, response status,
    and execution time for every request.
    """

    async def dispatch(self, request, call_next):

        start_time = time.perf_counter()

        response = await call_next(request)

        execution_time = (time.perf_counter() - start_time) * 1000

        logger.info(
            f"{request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Latency: {execution_time:.2f} ms"
        )

        return response