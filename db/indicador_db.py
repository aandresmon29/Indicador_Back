from typing import Dict
from pydantic import BaseModel
from pydantic.errors import ArbitraryTypeError

class IndicadorInDB(BaseModel):
    id_indicador: int = 0
    name: str
    porcentaje: float
    gerencia: str
    central: str
    colorin: str
    formula: str
    calculo: str

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
    "Indicador1": IndicadorInDB(**{"id_indicador": 1,
                            "name":"Embargos",
                            "porcentaje": 98.5,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"Respuestas generadas / Embargos y Desembargos Capturados",
                            "calculo":"98.5/100"}),
    "Indicador2": IndicadorInDB(**{"id_indicador": 2,
                            "name":"Requerimientos",
                            "porcentaje": 99.6,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"Respuestas generadas / Requerimientos Capturados",
                            "calculo":"99.6/100"}),
    "Indicador3": IndicadorInDB(**{"id_indicador": 3,
                            "name":"Calidad",
                            "porcentaje": 99.9,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"Embargos y Desembargos Capturados - Reclamos Favorables a clientes / Embargos y Desembargos Capturados",
                            "calculo":"99.9-1/100"}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None