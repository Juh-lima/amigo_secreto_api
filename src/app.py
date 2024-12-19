from litestar import Litestar # type: ignore
from litestar.openapi import OpenAPIConfig # type: ignore
from litestar.openapi.plugins import SwaggerRenderPlugin, YamlRenderPlugin # type: ignore

from presentation.routes.auth_route import auth_route

app = Litestar(
    route_handlers=[auth_route],
    on_startup=[],
    on_shutdown=[],
    openapi_config=OpenAPIConfig(
        title="AmigoSecretoAPI",
        version="1.0.0",
        root_schema_site="swagger",
        render_plugins=[
            SwaggerRenderPlugin(path="/docs"),
            YamlRenderPlugin(path="/spec"),
        ],
    ),
)
