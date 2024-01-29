import os
from typing import List

import yaml

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
config_path = os.path.join(project_dir, 'config.ini')

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)


class Mission:
    """Represents the mission within the program's context.

    This class is responsible for handling information related to missions.
    It initializes an instance with specific mission details obtained from an
    generate_mission_files.

    Attributes:
        __mission (str): (PRIVATE ATRIBUTE) Stores mission information obtained from the configuration (confing.yaml) list of missions.
    Methods:
        get_Mission: Using the method getter for get the private attribute mission.

    """
    def __init__(self):
        self.mission = config_data['general']['missions']


class Devices:
    """Manages and represents devices within the program.

    This class is used for handling devices. It includes functionality
    to initialize and store details about various devices, which are
    obtained from configuration (config.yaml) list of devices.

    Attributes:
        _device (str): A semi-public attribute containing information about the device from the configuration (config.yaml) list of devices.

    Methods:
        get_mission: A method for retrieving the private attribute 'mission'
    """
    def __init__(self):
        self.device = config_data['general']['devices']

    def get_Devices(self):
        return self._device
class Status:
    """Represents and manages the status of an object or entity in the program.

    This class is responsible for handling the status of various entities.
    It initializes the status based on the supplied configuration and provides
    methods for its subsequent management or query.

    Attributes:
        status (str): (PUBLIC ATRIBUTE) Manages entity status from config.yaml list.
    """
    def __init__(self):
        self.status = config_data['general']['status']
