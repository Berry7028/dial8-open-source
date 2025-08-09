from __future__ import annotations
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute
from starlette.middleware.cors import CORSMiddleware
from .api import routes as api_routes
from .ws import ws_routes


async def health(request):
    return JSONResponse({"ok": True})

routes = [Route("/healthz", health, methods=["GET"])] + api_routes
ws = ws_routes

app = Starlette(debug=True, routes=routes + ws)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)