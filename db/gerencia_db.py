from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class GerInDB(BaseModel):
    name: str
    indigen: float
    color: str

database_gerencias = Dict[str, GerInDB]
database_gerencias = {
    "Gerencia1": GerInDB(**{"name":"Gerencia de Operación Bancaria",
                            "indigen":97.2,
                            "color":"red"}),
    "Gerencia2": GerInDB(**{"name":"Gerencia de Prueba",
                            "indigen":96.5,
                            "color":"green"})
}

def get_gerencia(gerencia: str):
    if gerencia in database_gerencias.keys():
        return database_gerencias[gerencia]
    else:
        return None