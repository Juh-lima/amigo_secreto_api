from litestar import Router # type: ignore

from presentation.controllers.auth_controller import AuthController

auth_route = Router(path="/auth", route_handlers=[AuthController])
