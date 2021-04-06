from pydantic import BaseModel

class GerIn(BaseModel):
    name: str
    indigen: float
    color: str

class GerOut(BaseModel):
    name: str
    indigen: float
    color: str