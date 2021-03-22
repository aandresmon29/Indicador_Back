from typing import Dict
from pydantic import BaseModel
from pydantic.errors import ArbitraryTypeError

class IndicadorInDB(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
    "Embargos": IndicadorInDB(**{"id_indicador": 1,
                            "name":"Embargos",
                            "porcentaje": 98.55,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos"}),
    "Requerimientos": IndicadorInDB(**{"id_indicador": 2,
                            "name":"Requerimientos",
                            "porcentaje": 100.00,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos"}),
    "Calidad": IndicadorInDB(**{"id_indicador": 3,
                            "name":"Calidad",
                            "porcentaje": 99.99,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos"})
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None