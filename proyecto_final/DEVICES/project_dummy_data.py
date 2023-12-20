from datetime import datetime
#tiene que haber un registro de misiones "El nombre"
#se les asigna codigo
#En caso de que la misión no esté previamente definida en el registro (UNKN), se
#deberá almacenar y asignar un identificador único a cada ejecución.

project_missions = [
        {"id": 1, "name": "ORBONE", "components": ["Satellite", "Space_Suit","Space_food"]},
        {"id": 2, "name": "CLNM", "components": ["Satellite", "Space_vehicle","Space_rockets"]},
        {"id": 3, "name": "TMRS", "components": ["Satellite", "Space_Suit", "Space_vehicle"]},
        {"id": 4, "name": "GALXONE", "components": ["Space_Suit", "Space_vehicle","Satellite","Space_food"]},
        {"id": 5, "name": "UNKN", "components": [""]},
    ]

project_devices = [
        {"id": 1, "name": "Satellite"},
        {"id": 2, "name": "Space_Suit"},
        {"id": 3, "name": "Space_vehicle"},
        {"id": 4, "name": "Space_rockets"},
        {"id": 5, "name": "Space_tools"},
        {"id": 6, "name": "Space_food"}
    ]

def hash_format(date, mission_name, device_type, device_status):
       return date+"_"+mission_name+"_"+device_type+"_"+device_status

def date_format():
     now = datetime.now()
     return now.strftime('%d%m%Y%H%M%S')