from litestar import Controller, post # type: ignore

from application.providers import hash_provider
from application.usecases.login_user_usecase import LoginUserUsecase # type: ignore
from domain import repositories
from presentation.schemas.auth_schemas import AuthResponseSchema # type: ignore
from presentation.schemas.user_schemas import UserLoginSchema # type: ignore


class AuthController(Controller):
    dependencies = {}
    
    @post("/login")
    async def login(self, data: UserLoginSchema) -> AuthResponseSchema:
        usecase = LoginUserUsecase(repositories, hash_provider)

        return AuthResponseSchema(auth_token="", refresh_token="")

    @post("/registro")
    async def register(self, data) -> None:
        return {}
