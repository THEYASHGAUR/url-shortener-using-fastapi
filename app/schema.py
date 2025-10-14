from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLInfo(BaseModel):
    original_url: str
    short_url: str

    class Config:
        orm_mode = True
