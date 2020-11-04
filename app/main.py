import sys

sys.path.extend(["./"])

from app.application import app
from app.routes.base import router as base_router
from app.routes.users import router as user_router

ROUTERS = (base_router, user_router)

for r in ROUTERS:
    app.include_router(r)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
