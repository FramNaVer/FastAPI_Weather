from pydantic import BaseModel

class CityOut(BaseModel):
    id: int
    name: str
    country: str | None = None

    class Config:
        orm_mode = True
