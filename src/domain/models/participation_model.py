from uuid import UUID

from pydantic import BaseModel # type: ignore


class Participation(BaseModel):
    id: UUID
    user_id: str
    event_id: str
    hidden_friend_id: str
