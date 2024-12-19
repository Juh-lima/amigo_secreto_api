from pydantic import BaseModel # type: ignore


class UserLoginSchema(BaseModel):
    password: str
    phone_number: str


class UserSignupSchema(BaseModel):
    confirm_password: str
    name: str
    password: str
    phone_number: str
