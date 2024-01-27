import configparser
import logging
import os
from datetime import datetime

import yaml

# abstraction of information from simulations
script_path = os.path.abspath(__file__)
folder_path = os.path.join(os.path.dirname(script_path), 'SIMULATIONS')

# creation of Data variable to store all the information
data = []
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            with open(file_path, 'r') as file:
                data.extend(file.readlines())
        except FileNotFoundError:
            print(f"The file was not found: {file_path}")
        except Exception as e:
            print(f"No interactions currently found {file_path}: {e}")

# creation of diccionary_list variable with all the data to make variables
diccionary_list = []
for i in range(0, len(data), 5):
    grupo = data[i: i + 5]
    diccionary = dict(line.strip().split(': ', 1) for line in grupo)
    diccionary_list.append(diccionary)

# Creation of variables necessary to answer the workshop questions
count_mission = {}
count_device = {}
count_device_status = {}
count_simulations = {'count': 0}

for item in diccionary_list:
    mission_actual = item.get('Mission', 'This mission never happened')
    count_mission[mission_actual] = count_mission.get(mission_actual, 0) + 1

    device_actual = item.get('Device Type', 'This dispositive was not used in any mission')
    count_device[device_actual] = count_device.get(device_actual, 0) + 1

    device_status_actual = item.get('Device Status', 'This status never happened')
    count_device_status[device_status_actual] = count_device_status.get(device_status_actual, 0) + 1

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)
date_format = config_data['general']['date_format']
now = datetime.now()
current_time = now.strftime(date_format)


config = configparser.ConfigParser()
config.read('count_reports.ini')

count_of_reports = config.getint('count_of_name_reports', 'count_of_reports')
count_of_reports += 1
config.set('count_of_name_reports', 'count_of_reports', str(count_of_reports))
with open('count_reports.ini', 'w') as config_file:
    config.write(config_file)
if diccionary_list == []:
    print('We do not have pending simulations')
else:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(message)s',
        datefmt='%d%m%y%H%M%S',
        filename=f'./proyecto_final/DEVICES/REPORTS/APLSTATS-{count_of_reports}-{current_time}.log',
        filemode='a'
    )

for i in diccionary_list:
    count_simulations['count'] += 1

total_simulations = count_simulations['count']
logging.info(f"Total simulations: {total_simulations}\n")

logging.info("Events for status and devices: ")
for mission, conteo_misiones in count_mission.items():
    logging.info(f'Mission "{mission}": {conteo_misiones}')
for device, count_device in count_device.items():
    logging.info(f'Device_type "{device}": {count_device}')
for device_status, count_status_devices in count_device_status.items():
    logging.info(f'device_status "{device_status}": {count_status_devices}')

# //////////////////////////////////////////////////////////////////////////////////////////////////
logging.info("\n")
logging.info("Devices that present a greater number of disconnections (UNKNOW state for each mission): ")

count_unknown_per_mission = {}
for item in diccionary_list:
    mission = item['Mission']
    device_status = item['Device Status']
    if mission in count_unknown_per_mission:
        count_unknown_per_mission[mission] += 1 if device_status == 'unknown' else 0
    else:
        count_unknown_per_mission[mission] = 1 if device_status == 'unknown' else 0

for mission, count in count_unknown_per_mission.items():
    logging.info(f'UNKNOW in the mission: "{mission}": {count}')


# //////////////////////////////////////////////////////////////////////////////////////////////////
logging.info("\n")
logging.info("Mission consolidation with inoperable devices (status KILLED and FAULTY): ")

count_faulty_killed_per_device = {}

for item in diccionary_list:
    device = item['Device Type']
    device_status = item['Device Status']

    if device_status != 'Unknown':
        if device in count_faulty_killed_per_device:
            count_faulty_killed_per_device[device] += (
                1 if (device_status == 'killed' or device_status == 'faulty') else 0)
        else:
            count_faulty_killed_per_device[device] = (
                1 if (device_status == 'killed' or device_status == 'faulty') else 0)
for device, count_device in count_faulty_killed_per_device.items():
    logging.info(f'Number of times "faulty-killed" for the device "{device}": {count_device}')

# //////////////////////////////////////////////////////////////////////////////////////////////////

logging.info("\n")
logging.info("Percentage of data generated for each device and mission with respect to the amount of data: ")
total_simulations = count_simulations['count']
logging.info(f"Total simulations: {total_simulations}")

for mission, count_mission in count_mission.items():
    number = count_mission / total_simulations
    percentage = number * 100
    logging.info(f'%Mission sobre total iteraciones: "{mission}": {percentage:.2f}%')

for device_status, count_status_devices in count_device_status.items():
    numero = count_status_devices / total_simulations
    percentage = numero * 100
    logging.info(f'%Device Status over total iterations: "{device_status}": {percentage:.2f}%')
