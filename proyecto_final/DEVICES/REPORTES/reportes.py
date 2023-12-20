import logging
from datetime import datetime

# ////////////////GENERACIÓN DE REPORTES///////////////////////////////
# 1. HACER LECTURA DE LAS SIMULACIONES
# 2. CREAR UNA LISTA DE DICCIONARIOS CON LA INFO DE LAS SIMULACIONES
# 3. CONVERTIRLO EN DICCIONARIO
# 4. OPERAR LOS DICCIONARIOS
# 5. GENERAR EL REPORTE CON LA DATA

# //////////////////////////////////////////////////////////////////////////////////////////////////
# 1.HACER LECTURA DE LAS SIMULACIONES
# La información proporcionada
# info = "date: 05122023205914; mission: KNOW; device_type: KNOW; device_status: KNOW; hash: 05122023205914_ORBONE_satelites_killed;date: 05122023205914; mission: KNOW; device_type: KNOW; device_status: KNOW; hash: 05122023205914_ORBONE_satelites_killed;"
# file1 = open("SIMULACIONES/1/APL-ORBONE-00001.log")
# print(file1)
# file1.close()


# 2. CREAR UNA LISTA DE DICCIONARIOS CON LA INFO DE LAS SIMULACIONES
# # Separar la información en pares clave-valor
# par_llave_valor = info.split(";")

# # # # Crear un diccionario a partir de los pares clave-valor
# resultado_dict = {}
# for par in par_llave_valor:
#     if ":" in par:
#         key, value = map(str.strip, par.split(":", 1))
#         resultado_dict[key] = value

# # Imprimir el diccionario resultante
# print("diccionario_final: ",resultado_dict)

from datetime import datetime
import logging

lista_diccionarios = [
    {'date': '05122023205914', 'mission': 'KNOW', 'device_type': 'KNOW', 'device_status': 'KNOW', 'hash': '05122023205914_ORBONE_satelites_killed'},
    {'date': '05122023205915', 'mission': 'CLNM', 'device_type': 'satelites', 'device_status': 'ACTIVE', 'hash': '05122023205915_ORBONE_moon_explore'},
    {'date': '05122023205917', 'mission': 'KNOW', 'device_type': 'KNOW', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205918', 'mission': 'KNOW', 'device_type': 'KNOW', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205919', 'mission': 'TMRS', 'device_type': 'satelites', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205912', 'mission': 'GALXONE', 'device_type': 'trajes', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205913', 'mission': 'GALXONE', 'device_type': 'trajes', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205918', 'mission': 'GALXONE', 'device_type': 'vehiculos', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205920', 'mission': 'ORBONE', 'device_type': 'vehiculos', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205921', 'mission': 'ORBONE', 'device_type': 'naves', 'device_status': 'INACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205923', 'mission': 'CLNM', 'device_type': 'trajes', 'device_status': 'ACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'},
    {'date': '05122023205923', 'mission': 'JUANITO', 'device_type': 'ANDRESYMIGUEL', 'device_status': 'ACTIVE', 'hash': '05122023205916_ORBONE_mission_failed'}
    # Agrega más diccionarios según sea necesario
]

# 3. OPERAR LOS DICCIONARIOS
# INICIALIZADORES DE LOS DICCIONARIOS O DICCIONARIOS NULOS
conteo_mission = {}
conteo_device = {}
conteo_device_status = {}
conteo_simulaciones = {'count': 0}

# CONTEO DEL NUMERO DE VECES QUE SE REPITE CADA ITEM DENTRO DEL DICCIONARIO
for item in lista_diccionarios:
    mission_actual = item.get('mission', 'Esta misión no se realizó')
    conteo_mission[mission_actual] = conteo_mission.get(mission_actual, 0) + 1

    device_actual = item.get('device_type', 'Este dispositivo no se utilizó')
    conteo_device[device_actual] = conteo_device.get(device_actual, 0) + 1

    device_status_actual = item.get('device_status', 'Este status no se generó')
    conteo_device_status[device_status_actual] = conteo_device_status.get(device_status_actual, 0) + 1

# 4. GENERAR EL REPORTE CON LA DATA
def fecha_reporte():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

current_time = fecha_reporte()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    datefmt='%d%m%y%H%M%S',
    filename=f'./proyecto_final/DEVICES/REPORTES/APLSTATS-[REPORTE]-{current_time}.log',
    filemode='a'
)

# Conteo total de simulaciones
for i in lista_diccionarios:
    conteo_simulaciones['count'] += 1

total_simulaciones = conteo_simulaciones['count']
logging.info(f"Total simulaciones: {total_simulaciones}")

# Conteo de misiones
for mission, conteo_misiones in conteo_mission.items():
    logging.info(f'Mission "{mission}": {conteo_misiones}')

# Conteo de tipos de dispositivos
for device, conteo_dispositivos in conteo_device.items():
    logging.info(f'Device_type "{device}": {conteo_dispositivos}')

# Conteo de estados de dispositivos
for device_status, conteo_status_dispositivos in conteo_device_status.items():
    logging.info(f'device_status "{device_status}": {conteo_status_dispositivos}')


# % Misiones sobre total simulaciones

for mission, conteo_misiones in conteo_mission.items():
    numero = conteo_misiones/total_simulaciones
    porcentaje = numero * 100
    logging.info(f'%Mission sobre total iteraciones: "{mission}": {porcentaje:.2f}%')
    
# % Status misiones sobre total simulaciones

for device_status, conteo_status_dispositivos in conteo_device_status.items():
    numero = conteo_status_dispositivos/total_simulaciones
    porcentaje = numero * 100
    logging.info(f'%Device Status sobre total iteraciones: "{device_status}": {porcentaje:.2f}%')