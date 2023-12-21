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
    # Agrega más diccionarios según sea necesario
]

conteo_simulaciones = {'count': 0}

for i in lista_diccionarios:
    conteo_simulaciones['count'] += 1

total_simulaciones = conteo_simulaciones['count']
print(total_simulaciones)