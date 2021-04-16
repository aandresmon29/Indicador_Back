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
    ponderado: float
    lgreen: float
    lyellow: float
    lred: float

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
    "Indicador1": IndicadorInDB(**{"id_indicador": 1,
                            "name":"Oportunidad en la atención de oficios de Requerimientos de Entes Externos",
                            "porcentaje": 99.3,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"Oficios de Requerimientos de Entes Externos atendidos oportunamente /  oficios de Requerimientos de Entes Externos radicados",
                            "calculo":"148/149 = 99.33%",
                            "ponderado":95.0,
                            "lgreen":98.0,
                            "lyellow":95.0,
                            "lred":95.0}),
    "Indicador2": IndicadorInDB(**{"id_indicador": 2,
                            "name":"Oportunidad en la atención de Embargos-Desembargos",
                            "porcentaje": 99.4,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"Embargos-Desembargos atendidos oportunamente / Total Embargos-Desembargos radicados",
                            "calculo":"10.855/10.914 = 99.45%",
                            "ponderado":95.0,
                            "lgreen":98.0,
                            "lyellow":95.0,
                            "lred":95.0}),
    "Indicador3": IndicadorInDB(**{"id_indicador": 3,
                            "name":"Calidad Embargos y Desembargos",
                            "porcentaje": 99.9,
                            "gerencia": "Gerencia Operación Bancaria",
                            "central": "Atención a Requerimientos Externos",
                            "colorin":"green",
                            "formula":"(Total Embargos y Desembargos radicados – Reclamos favorables para el cliente) / Total Embargos-Desembargos radicados",
                            "calculo":"(10.914-0)/10.914 = 100%",
                            "ponderado":95.0,
                            "lgreen":97.5,
                            "lyellow":97.5,
                            "lred":95.0}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None