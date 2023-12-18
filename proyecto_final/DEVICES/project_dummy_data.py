from datetime import datetime

project_missions = [
        {"id": 1, "name": "OrbitOne", "components": ["Satellite", "Space_Suit","Space_food"]},
        {"id": 2, "name": "ColonyMoon", "components": ["Satellite", "Space_vehicle","Space_rockets"]},
        {"id": 3, "name": "VacMars", "components": ["Satellite", "Space_Suit", "Space_vehicle"]},
        {"id": 4, "name": "GalaxyTwo", "components": ["Space_Suit", "Space_vehicle","Satellite","Space_food"]}
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