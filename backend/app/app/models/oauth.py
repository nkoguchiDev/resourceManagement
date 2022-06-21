from pydantic import BaseModel


class ClientCredential(BaseModel):
    id: str
    key: str
    secret: str


class OauthToken(BaseModel):
    developerId: str
    # refresh_token: str = None
    # expires_in: int = None
    # scope: str = None
    # client_id: str = None
