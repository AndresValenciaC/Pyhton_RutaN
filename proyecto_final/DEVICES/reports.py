import logging
from datetime import datetime
import os
import configparser
# //////////////////////////////////////////////////////////////////////////////////////////////////
# 1.HACER LECTURA DE LAS SIMULACIONES
# Ruta actual del script (reportes.py)
script_path = os.path.abspath(__file__)

# RUTA DE LA CARPETA SIMULATIONS
folder_path = os.path.join(os.path.dirname(script_path), 'SIMULATIONS')

#HACER LECTURA DEL ARCHIVO SIMULACIONES Y ALMACENARLO EN VARIABLE "DATA ALMACENADA"
data = []
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            with open(file_path, 'r') as file:
                data.extend(file.readlines())
        except FileNotFoundError:
            print(f"El archivo no encontrado: {file_path}")
        except Exception as e:
            print(f"No se encuentran interaciones actualmente {file_path}: {e}")

# //////////////////////////////////////////////////////////////////////////////////////////////////
# 2. CREAR UNA LISTA DE DICCIONARIOS CON LA INFO DE LAS SIMULACIONES
# Inicializar la lista de diccionarios
lista_de_diccionarios = []

# Procesar cada grupo de 5 líneas y crear un diccionario
for i in range(0, len(data), 5):
    grupo = data[i:i+5]
    diccionario = dict(line.strip().split(': ', 1) for line in grupo)
    lista_de_diccionarios.append(diccionario)

# //////////////////////////////////////////////////////////////////////////////////////////////////
# # 3. OPERAR LOS DICCIONARIOS
# # INICIALIZADORES DE LOS DICCIONARIOS O DICCIONARIOS NULOS
conteo_mission = {}
conteo_device = {}
conteo_device_status = {}
conteo_simulaciones = {'count': 0}
file_number = 0

# # # # # CONTEO DEL NUMERO DE VECES QUE SE REPITE CADA ITEM DENTRO DEL DICCIONARIO
for item in lista_de_diccionarios:
    mission_actual = item.get('Mission', 'Esta misión no se realizó')
    conteo_mission[mission_actual] = conteo_mission.get(mission_actual, 0) + 1

    device_actual = item.get('Device Type', 'Este dispositivo no se utilizó')
    conteo_device[device_actual] = conteo_device.get(device_actual, 0) + 1

    device_status_actual = item.get('Device Status', 'Este status no se genero')
    conteo_device_status[device_status_actual] = conteo_device_status.get(device_status_actual, 0) + 1

# //////////////////////////////////////////////////////////////////////////////////////////////////
# # # 4. GENERAR EL REPORTE CON LA DATA
def fecha_reporte():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

current_time = fecha_reporte()

config = configparser.ConfigParser()
config.read('config.ini')

# Obtener el valor actual del contador desde el archivo de configuración
count_of_reports = config.getint('general', 'count_of_reports')

# Incrementar el contador para el próximo archivo
count_of_reports += 1

# Actualizar el valor del contador en el archivo de configuración
config.set('general', 'count_of_reports', str(count_of_reports))
with open('config.ini', 'w') as config_file:
    config.write(config_file)

if lista_de_diccionarios == []:
    print('No hay simulaciones pendientes por reportes')
else:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(message)s',
        datefmt='%d%m%y%H%M%S',
        filename=f'./proyecto_final/DEVICES/REPORTS/APLSTATS-{count_of_reports}-{current_time}.log',
        filemode='a'
    )
# //////////////////////////////////////////////////////////////////////////////////////////////////
# DATA A GENERAR
# # # Conteo total de simulaciones
for i in lista_de_diccionarios:
    conteo_simulaciones['count'] += 1

total_simulaciones = conteo_simulaciones['count']
logging.info(f"Total simulations: {total_simulaciones}\n")

# # # Conteo de misiones
logging.info("Cantidad de eventos por estado y dispositivo: ")
for mission, conteo_misiones in conteo_mission.items():
    logging.info(f'Mission "{mission}": {conteo_misiones}')
# # # Conteo de tipos de dispositivos
for device, conteo_dispositivos in conteo_device.items():
    logging.info(f'Device_type "{device}": {conteo_dispositivos}')
# # # Conteo de estados de dispositivos
for device_status, conteo_status_dispositivos in conteo_device_status.items():
    logging.info(f'device_status "{device_status}": {conteo_status_dispositivos}')

# //////////////////////////////////////////////////////////////////////////////////////////////////
logging.info("\n")
logging.info("Dispositivos que presentan un mayor numero de desconexiones, especificamente en el estado unknown, para cada mision: ")

# Inicializar el diccionario de conteo por mission
count_unknown_per_mission = {}

# Iterar sobre la lista de diccionarios
for item in lista_de_diccionarios:
    # Obtener la misión y el estado del dispositivo
    mission = item['Mission']
    device_status = item['Device Status']

    # Verificar si la misión ya está en el diccionario de conteo
    if mission in count_unknown_per_mission:
        # Incrementar el conteo si el estado del dispositivo es "unknown"
        count_unknown_per_mission[mission] += 1 if device_status == 'unknown' else 0
    else:
        # Inicializar el conteo si es la primera vez que se encuentra la misión
        count_unknown_per_mission[mission] = 1 if device_status == 'unknown' else 0

# Imprimir el resultado
for mission, count in count_unknown_per_mission.items():
    logging.info(f'Numero de veces que "unknown" aparece en "Device Status" para la mision "{mission}": {count}')


# //////////////////////////////////////////////////////////////////////////////////////////////////
logging.info("\n")
logging.info("Consolidacion de misiones con dispositivos inoperables :")

# Inicializar el diccionario de conteo por mission
count_faulty_killed_per_device = {}

for item in lista_de_diccionarios:
    # Obtener el tipo de dispositivo y el estado del dispositivo
    device = item['Device Type']
    device_status = item['Device Status']

    # Verificar si el tipo de dispositivo no es "unknown"
    
    if device_status != 'Unknown':
    # Verificar si el tipo de dispositivo ya está en el diccionario de conteo
        if device in count_faulty_killed_per_device:
            # Incrementar el conteo si el estado del dispositivo es "killed" o "faulty"
            count_faulty_killed_per_device[device] += 1 if (device_status == 'killed' or device_status == 'faulty') else 0
        else:
            # Inicializar el conteo si es la primera vez que se encuentra el tipo de dispositivo
            count_faulty_killed_per_device[device] = 1 if (device_status == 'killed' or device_status == 'faulty') else 0
# Imprimir el resultado
for device, count_device in count_faulty_killed_per_device.items():
    logging.info(f'Numero de veces que "faulty-killed" aparece en "Device Status" para el dispositivo "{device}": {count_device}')

# //////////////////////////////////////////////////////////////////////////////////////////////////

logging.info("\n")
logging.info("Porcentaje de datos generados para cada dispositivo y mision respecto a la cantidad de datos: ")
# # # % Misiones sobre total simulaciones
total_simulaciones = conteo_simulaciones['count']
logging.info(f"Total simulations: {total_simulaciones}")

for mission, conteo_misiones in conteo_mission.items():
    numero = conteo_misiones/total_simulaciones
    porcentaje = numero * 100
    logging.info(f'%Mission sobre total iteraciones: "{mission}": {porcentaje:.2f}%')
    
# # # % Status misiones sobre total simulaciones

for device_status, conteo_status_dispositivos in conteo_device_status.items():
    numero = conteo_status_dispositivos/total_simulaciones
    porcentaje = numero * 100
    logging.info(f'%Device Status sobre total iteraciones: "{device_status}": {porcentaje:.2f}%')
    
    
    
    
#     data = ['Date: 31122023130828\n', 'Mission: GALXONE\n', 'Device Type: Space_tools\n', 'Device Status: unknown\n', 'Hash: 31122023130828_GALXONE_Space_tools_unknown\n', 'Date: 31122023135656\n', 'Mission: CLNM\n', 'Device Type: Space_Suit\n', 'Device Status: good\n', 'Hash: 31122023135656_CLNM_Space_Suit_good\n', 'Date: 31122023135656\n', 'Mission: CLNM\n', 'Device Type: Space_rockets\n', 'Device Status: warning\n', 'Hash: 31122023135656_CLNM_Space_rockets_warning\n', 'Date: 31122023135656\n', 'Mission: GALXONE\n', 'Device Type: Space_Suit\n', 'Device Status: killed\n', 'Hash: 31122023135656_GALXONE_Space_Suit_killed\n', 'Date: 31122023135656\n', 'Mission: GALXONE\n', 'Device Type: Space_vehicle\n', 'Device Status: faulty\n', 'Hash: 31122023135656_GALXONE_Space_vehicle_faulty\n', 'Date: 31122023135656\n', 'Mission: ORBONE\n', 'Device Type: Space_rockets\n', 'Device Status: killed\n', 'Hash: 31122023135656_ORBONE_Space_rockets_killed\n', 'Date: 31122023135656\n', 'Mission: TMRS\n', 'Device Type: Space_rockets\n', 'Device Status: unknown\n', 'Hash: 31122023135656_TMRS_Space_rockets_unknown\n', 'Date: 31122023135656\n', 'Mission: Unknown\n', 'Device Type: Unknown\n', 'Device Status: Unknown\n', 'Hash: Unknown\n', 'Date: 31122023135656\n', 'Mission: Unknown\n', 'Device Type: Unknown\n', 'Device Status: Unknown\n', 'Hash: Unknown\n']

# print(type(data))

# lista_de_diccionarios = [{'Date': '31122023130828', 'Mission': 'GALXONE', 'Device Type': 'Space_tools', 'Device Status': 'unknown', 'Hash': '31122023130828_GALXONE_Space_tools_unknown'}, {'Date': '31122023135656', 'Mission': 'CLNM', 'Device Type': 'Space_Suit', 'Device Status': 'good', 'Hash': '31122023135656_CLNM_Space_Suit_good'}, {'Date': '31122023135656', 'Mission': 'CLNM', 'Device Type': 'Space_rockets', 'Device Status': 'warning', 'Hash': '31122023135656_CLNM_Space_rockets_warning'}, {'Date': '31122023135656', 'Mission': 'GALXONE', 'Device Type': 'Space_Suit', 'Device Status': 'killed', 'Hash': '31122023135656_GALXONE_Space_Suit_killed'}, {'Date': '31122023135656', 'Mission': 'GALXONE', 'Device Type': 'Space_vehicle', 'Device Status': 'faulty', 'Hash': '31122023135656_GALXONE_Space_vehicle_faulty'}, {'Date': '31122023135656', 'Mission': 'ORBONE', 'Device Type': 'Space_rockets', 'Device Status': 'killed', 'Hash': '31122023135656_ORBONE_Space_rockets_killed'}, {'Date': '31122023135656', 'Mission': 'TMRS', 'Device Type': 'Space_rockets', 'Device Status': 'unknown', 'Hash': '31122023135656_TMRS_Space_rockets_unknown'}, {'Date': '31122023135656', 'Mission': 'Unknown', 'Device Type': 'Unknown', 'Device Status': 'Unknown', 'Hash': 'Unknown'}, {'Date': '31122023135656', 'Mission': 'Unknown', 'Device Type': 'Unknown', 'Device Status': 'Unknown', 'Hash': 'Unknown'}]