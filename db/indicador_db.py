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

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Atención casos escalados por OMAT por correo",
							"porcentaje":83.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos escalados por OMAT por correo Fuente: Correos enviados por OMAT y registro de los casos atendidos en el grupo.",
							"calculo":"213 (# Casos escalados por correo)",
							"ponderado":83.1,
							"lgreen":100,
							"lyellow":76}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"Cumplimiento de operaciones Clientes",
							"porcentaje":90.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 317 Op. Cumplidas 286 por valor de USD 3.146.378,25",
							"ponderado":90.2,
							"lgreen":100,
							"lyellow":90.2}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":95.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 56",
							"ponderado":95.9,
							"lgreen":95,
							"lyellow":95}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":96.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 191",
							"ponderado":96.3,
							"lgreen":97,
							"lyellow":97}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Cajeros: Up time cajeros NCR",
							"porcentaje":98.0,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 501",
							"ponderado":98.0,
							"lgreen":97,
							"lyellow":97}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":99.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Acumulado: Q 16,146 - $ 6.0 Billones Semanal: Q 1,453  - $ 450 Mil Mll",
							"ponderado":99.3,
							"lgreen":95,
							"lyellow":90}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":99.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"1. Red",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $570,000,000,000 promd)",
							"calculo":"Saldo promedio: $572.609.361.241",
							"ponderado":99.5,
							"lgreen":100,
							"lyellow":100}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":99.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"3. Green",
							"formula":"Embargos-Desembargos atendidos oportunamente / Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones capturadas 34.699 Identificaciones Oportunas (1 a 3 dias) 34.639 Identificaciones i",
							"ponderado":99.8,
							"lgreen":98,
							"lyellow":92}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Transferencias Electrónicas - Calidad lotes  aplicados",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Lotes aplicados / Lotes recibidos",
							"calculo":"Lotes aplicados: 29.159 Valor Total $467,628,069,201.22",
							"ponderado":100,
							"lgreen":100,
							"lyellow":90}),
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"Canje: Oportunidad compensación todas las Centrales.",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Centrales de Canje con compensación canje / transmisión a Banco de la República oportunamente",
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canj",
							"ponderado":100,
							"lgreen":100,
							"lyellow":100}),
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"Oportunidad en conciliación",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"3. Green",
							"formula":"Canales  a conciliar (oficinas, centros de canje, cajeros corresponsales propios, Carvajal, Efectivo clientes,centros de efectivo,AFC,impuestos, ACH, transferencias ya, mi pago amigo ) / canales  conciliados",
							"calculo":"",
							"ponderado":100,
							"lgreen":100,
							"lyellow":100}),
	"Indicador12": IndicadorInDB(**{"id_indicador": 12,
							"name":"Oportunidad en la inclusión de negociaciones vinculación",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Supervisión Operativa Cash",
							"colorin":"3. Green",
							"formula":"Solicitudes atendidas oportunamente (Fuente Herramienta de negociación Star Cash (estado de la propuesta) / Total solicitudes recibidas (Fuente excel herremienta de gestión y Control Cash relación diaria)",
							"calculo":"Clientes 398",
							"ponderado":100,
							"lgreen":100,
							"lyellow":97.9}),
	"Indicador13": IndicadorInDB(**{"id_indicador": 13,
							"name":"Oportunidad en el monitoreo de alertas operativas del canal",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"Alertas gestionadas / Alertas generadas en el portal de monitoreo. Fuente porta monitoreo",
							"calculo":"56 alertas asignadas para esta semana. Todas gestionadas. Alertamiento en modelo propio por fraccion",
							"ponderado":100,
							"lgreen":100,
							"lyellow":100}),
	"Indicador14": IndicadorInDB(**{"id_indicador": 14,
							"name":"Oportunidad en el cumplimiento de operaciones del Piso Financiero y adsc",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"# Operaciones 571 por valor de $4.714.281.003.037.14",
							"ponderado":100,
							"lgreen":100,
							"lyellow":100}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None