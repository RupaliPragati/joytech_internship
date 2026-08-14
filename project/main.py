from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.status import router as status_router
from app.api.telemetry import router as telemetry_router

from app.core.config import settings

from app.exceptions.handlers import (
    TelemetryException,
    telemetry_exception_handler,
)

from app.logger import logger
from app.middleware.logging import RequestLoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("========== CERT-SAT Backend Starting ==========")

    yield

    logger.info("========== CERT-SAT Backend Shutdown ==========")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend service for satellite telemetry processing and anomaly detection.",
    lifespan=lifespan,
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "https://crispy-space-yodel-5gr5gx9vpgrrh66p-5500.app.github.dev",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ============================================================
# REQUEST LOGGING
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://crispy-space-yodel-5gr5gx9vpgrrh66p-5500.app.github.dev",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# EXCEPTION HANDLERS
# ============================================================

app.add_exception_handler(
    TelemetryException,
    telemetry_exception_handler,
)


# ============================================================
# API ROUTES
# ============================================================

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    health_router,
    prefix="/api/v1",
)

app.include_router(
    status_router,
    prefix="/api/v1",
)

app.include_router(
    telemetry_router,
    prefix="/api/v1",
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "CERT-SAT Backend Running",
        "api_version": "v1",
        "docs": "/docs",
        "health": "/api/v1/health",
    }