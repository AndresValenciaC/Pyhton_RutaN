import os
import yaml
from typing import List

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
config_path = os.path.join(project_dir, 'config.ini')


class Mission:
    """Represents the mission within the program's context.

    This class is responsible for handling information related to missions.
    It initializes an instance with specific mission details obtained from an
    generate_mission_files.

    Attributes:
        __mission (str): (PRIVATE ATRIBUTE) Stores mission information obtained from the configuration.
    Methods:
        get_Mission: Using the method getter for get the private attribute mission.

    """
    def __init__(self):
        config_data = Configuration.load_config()
        self.__mission: List[str] = config_data['general']['missions']

    def get_Mission(self):
        return self.__mission


class Devices:
    """Manages and represents devices within the program.

    This class is used for handling devices. It includes functionality
    to initialize and store details about various devices, which are
    obtained from configuration (config.yaml) list of devices.

    Attributes:
        _device (str): A semi-public attribute containing information about the device from the configuration.

    Methods:
        get_mission: A method for retrieving the private attribute 'mission'
    """
    def __init__(self):
        config_data = Configuration.load_config()
        self._device: List[str] = config_data['general']['devices']

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
        config_data = Configuration.load_config()
        self.status: List[str] = config_data['general']['status']


class Configuration:
    """
    Manages centralized loading and access to the application's configuration.

    This class implements the Singleton pattern to load and store the application's
    configuration from a YAML file, ensuring that configuration data is loaded
    only once and reused throughout the program.

    Class Attributes:
        __config_data (dict): A private class variable that stores the loaded configuration from 'config.yaml'.
            It is only accessible within the class and cannot be directly modified from outside.

    Methods:
        load_config (cls): A class method that loads the configuration from 'config.yaml' if it has not been loaded yet.
            Returns the configuration dictionary for use in other classes.
    """
    __config_data = None

    @classmethod
    def load_config(cls):
        if cls.__config_data is None:
            with open('config.yaml', 'r') as file:
                cls.__config_data = yaml.safe_load(file)
        return cls.__config_data


class HashFormat:

    @staticmethod
    def hash_format(date, mission, device_type, device_status):
        """Generates unique hash for each simulation mission.Using and concatenating all the information of mission

    :param date: we use the date function to bring the information from generate_mission_files.py.
    :type date: str
    :param mission: we use the date function to bring the information from generate_mission_files.py
    :type mission: str
    :param device_type: we use the date function to bring the information from generate_mission_files.py
    :type device_type: str
    :param device_status: we use the date function to bring the information from generate_mission_files.py
    :type device_status: str
    :return: we use the date function to bring the information from generate_mission_files.py
    :rtype: str
    """
        return date + "_" + mission + "_" + device_type + "_" + device_status
