from pydantic import BaseModel, HttpUrl, Field


class URLCreate(BaseModel):
    original_url: HttpUrl
    short_code: str | None = Field(default=None, min_length=4, max_length=10)

    def to_dict(self):
        return {"original_url": str(self.original_url)}


class URLResponse(BaseModel):
    original_url: HttpUrl
    short_code: str
