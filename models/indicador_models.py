from pydantic import BaseModel

class IndicadorIn(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str

class IndicadorOut(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str

