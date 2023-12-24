from fastapi import FastAPI

PREFIX = "/api/v1"


async def routes(app: FastAPI):
    from .endpoints.healtz import router as healthz_router
    from .endpoints.question import router as question_router
    from .endpoints.student import router as student_router

    app.include_router(healthz_router, tags=["Heathz"])
    app.include_router(question_router, prefix=PREFIX, tags=["Questions"])
    app.include_router(student_router, prefix=PREFIX, tags=["Students"])
