from pydantic import BaseModel

class IndicadorIn(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str
    colorin: str
    formula: str
    calculo: str
    ponderado: float
    lgreen: float
    lyellow: float
    lred: float

class IndicadorOut(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str
    colorin: str
    formula: str
    calculo: str
    ponderado: float
    lgreen: float
    lyellow: float
    lred: float
