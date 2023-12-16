import random
import time
from datetime import datetime

# ****************************ARCHIVOS***********************************************
# FECHA DEL ARCHIVOS
def fecha_solicitada():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

# STATUS DEL DISPOSITIVOS
def status():
    return random.choice(["excellent", "good", "warning", "faulty", "killed"])

status_dispositivos = status()
# print(status_dispositivo)

# HASH DEL ARCHIVOS
def hash(date,mission,device_type,device_status):
    return date+"_"+mission+"_"+device_type+"_"+device_status