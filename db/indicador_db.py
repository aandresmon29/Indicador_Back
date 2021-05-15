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
	comentario: str
	ponderado: float
	lgreen: float
	lyellow: str
	lred: float

database_indicadores = Dict[str, IndicadorInDB]
database_indicadores = {
	"Indicador10": IndicadorInDB(**{"id_indicador": 10,
							"name":"Cajeros: Up time cajeros NCR",
							"porcentaje":98.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros NCR",
							"calculo":"Cantidad de cajeros: 501",
							"comentario":"up time semanal del 6 al 12 de mayo",
							"ponderado":97.7,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador9": IndicadorInDB(**{"id_indicador": 9,
							"name":"Cajeros: Up time cajeros DIEBOLD",
							"porcentaje":97.5,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Up time cajeros DIEBOLD",
							"calculo":"Cantidad de cajeros: 191",
							"comentario":"up time semanal del 6 al 12 de mayo",
							"ponderado":96.8,
							"lgreen":97,
							"lyellow":"N/A",
							"lred":97}),
	"Indicador5": IndicadorInDB(**{"id_indicador": 5,
							"name":"Cajeros: Up time Multifuncionales DIEBOLD",
							"porcentaje":93.7,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Up time Multifuncionales DIEBOLD",
							"calculo":"Cantidad de MF: 56",
							"comentario":"up time semanal del 6 al 12 de mayo - Se presentó leve incremento de fallas en el depositario de las multifuncionales, ocasionadas en parte por mala operación del cliente al ingresar billetes y monedas",
							"ponderado":94.5,
							"lgreen":95,
							"lyellow":"N/A",
							"lred":95}),
	"Indicador4": IndicadorInDB(**{"id_indicador": 4,
							"name":"Efectivo: Cumplimiento Saldo de Caja",
							"porcentaje":92.4,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Total meta  / Total promedio semana (meta  para el 2021:  $570,000,000,000 promd)",
							"calculo":"Saldo promedio: $616.779.9440.838",
							"comentario":"Semana del 06 al 12 de Mayo. Debido a la situación del Paro Nacional y bloqueo de vías, las oficinas cuentan con un mayor saldo de efectivo para atender las necesidades de los clientes y se incremento la proyección de efectivo en los fondos de las transportadoras de valores, con el fin de no correr riesgos en agotamiento de efectivo para atender operación.",
							"ponderado":99,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador7": IndicadorInDB(**{"id_indicador": 7,
							"name":"Transferencias Electrónicas. Calidad lotes  aplicados",
							"porcentaje":99.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"2. Yellow",
							"formula":"Lotes aplicados / Lotes recibidos",
							"calculo":"Lotes aplicados: 27.580 Valor Total $375,307,938,899.74",
							"comentario":"Semana del 6 al 13 de mayo",
							"ponderado":99.9,
							"lgreen":100,
							"lyellow":"90",
							"lred":90}),
	"Indicador12": IndicadorInDB(**{"id_indicador": 12,
							"name":"Canje: Oportunidad compensación todas las Centrales.",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Servicios Operativos",
							"colorin":"3. Green",
							"formula":"Centrales de Canje con compensación canje / transmisión a Banco de la República oportunamente",
							"calculo":"Centrales de Canje: 38. 8 Cedec, 17 CUD o delegadas teercerizadas y 13 propias delegadas. Valor Canje Rec.: $96.040.638.694.98 Valor Canje Env.: $79.154.297.048.69",
							"comentario":"Semana del 06 al 12 mayo",
							"ponderado":100,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador1": IndicadorInDB(**{"id_indicador": 1,
							"name":"Oportunidad en la atención de Embargos-Desembargos",
							"porcentaje":80.9,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Atención Requerimientos de Entes Extern",
							"colorin":"1. Red",
							"formula":"Embargos-Desembargos atendidos oportunamente / Total Embargos-Desembargos radicados *Fuente: Sistema de embargos",
							"calculo":"Identificaciones capturadas 22.310 Identificaciones Oportunas(1-3 dias) 18.060 Identificaciones Inoportunas(mas 4 dias) 4.216 Identificaciones Pendientes 34",
							"comentario":"Respuestas del 3 al 9 de Mayo de 2021. Se presentó atraso en la captura de oficios por difucultad del personal de proveedor para llegar y permanacer en las instalaciones de la Calle 31. por temas de orden público",
							"ponderado":93.5,
							"lgreen":98,
							"lyellow":"92",
							"lred":92}),
	"Indicador2": IndicadorInDB(**{"id_indicador": 2,
							"name":"Atención casos escalados por OMAT por correo",
							"porcentaje":85.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte a Aplicaciones",
							"colorin":"2. Yellow",
							"formula":"# de casos atendidos / # casos escalados por OMAT por correo Fuente: Correos enviados por OMAT y registro de los casos atendidos en el grupo.",
							"calculo":"262",
							"comentario":"Semana del 7 al 13 de Mayo de 2021",
							"ponderado":85,
							"lgreen":100,
							"lyellow":"76",
							"lred":76}),
	"Indicador3": IndicadorInDB(**{"id_indicador": 3,
							"name":"Cumplimiento de operaciones Clientes",
							"porcentaje":91.2,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Coordinación Moneda Extranjera",
							"colorin":"2. Yellow",
							"formula":"Operaciones para tramitar en el exterior/ Operaciones enviadas por oficinas.",
							"calculo":"Op. Recibidas de clientes 365 Op. cumplidas 333 por valor de USD 3.305.456,99",
							"comentario":"Semana del 7 al 13 de Mayo de 2021",
							"ponderado":91.4,
							"lgreen":100,
							"lyellow":"90.2",
							"lred":90.2}),
	"Indicador6": IndicadorInDB(**{"id_indicador": 6,
							"name":"Oportunidad en conciliación",
							"porcentaje":96.3,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Central de Cuadre",
							"colorin":"2. Yellow",
							"formula":"Canales  a conciliar (oficinas, centros de canje, cajeros corresponsales propios, Carvajal, Efectivo clientes,centros de efectivo,AFC,impuestos, ACH, transferencias ya, mi pago amigo ) / canales  conciliados",
							"calculo":"1,739 puntos conciliados de 1,741 13 de mayo CB  sin cuadre por inconvenientes STARSET archivo de RBM 4,491 ajustes aplicados",
							"comentario":"Semana del 7 al 13 de Mayo de 2021",
							"ponderado":98.8,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador8": IndicadorInDB(**{"id_indicador": 8,
							"name":"Oportunidad en la inclusión de negociaciones vinculación Clientes Empresariales",
							"porcentaje":99.1,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Supervisión Operativa Cash",
							"colorin":"2. Yellow",
							"formula":"Solicitudes atendidas oportunamente (Fuente Herramienta de negociación Star Cash (estado de la propuesta) / Total solicitudes recibidas (Fuente excel herremienta de gestión y Control Cash relación diaria)",
							"calculo":"Clientes: 216",
							"comentario":"Semana del 07 al 13 de Mayo de 2021",
							"ponderado":99.6,
							"lgreen":100,
							"lyellow":"97.9",
							"lred":97.9}),
	"Indicador11": IndicadorInDB(**{"id_indicador": 11,
							"name":"Oportunidad transacciones atendidas en los tiempos definidos ANS",
							"porcentaje":98.8,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Centro Operación Empresarial  - Fiduciario",
							"colorin":"3. Green",
							"formula":"Transacciones cumplidas según ANS / solicitudes radicadas [Fuente: Excel - Inventario de solicitudes]",
							"calculo":"Acumulado: Q18,297 - $6.6 Bll Semanal  : Q 1,195 - $259 MMll",
							"comentario":"Semana del 07 al 13 de Mayo de 2021",
							"ponderado":98.7,
							"lgreen":95,
							"lyellow":"90",
							"lred":90}),
	"Indicador14": IndicadorInDB(**{"id_indicador": 14,
							"name":"Oportunidad en el monitoreo de alertas operativas del canal",
							"porcentaje":169,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "Soporte operativo Corresponsales Bancarios",
							"colorin":"3. Green",
							"formula":"Alertas gestionadas / Alertas generadas en el portal de monitoreo. Fuente porta monitoreo",
							"calculo":"Las alertas generadas al 29 de abril al 13 de mayo son 1371  las alertas gestionadas para esta semana deben ser 264 ( el 30% de 882 alertas), total gestionadas 446 alertas, 169% trx",
							"comentario":"Semana del 07 al 13 de Mayo de 2021",
							"ponderado":123,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
	"Indicador13": IndicadorInDB(**{"id_indicador": 13,
							"name":"Oportunidad en el cumplimiento de operaciones del PF y otras Áreas adscritas al PF",
							"porcentaje":100,
							"gerencia":"Gerencia de Operación Bancaria",
							"central": "UAC Back Office",
							"colorin":"3. Green",
							"formula":"Número total operaciones cumplidas/ operaciones a cumplir.",
							"calculo":"Se cumplieron 550 operaciones por un total de $4.585.997.122.700.55",
							"comentario":"Semana del 07 al 13 de Mayo de 2021",
							"ponderado":100,
							"lgreen":100,
							"lyellow":"N/A",
							"lred":100}),
}

def get_indicador(indicador: str):
    if indicador in database_indicadores.keys():
        return database_indicadores[indicador]
    else:
        return None