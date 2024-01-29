import os

import yaml

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
config_path = os.path.join(project_dir, 'config.ini')

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)


class Mission:
    def __init__(self):
        self.__mission = config_data['general']['missions']

    def get_Mission(self):
        return self.__mission

class Devices:
    def __init__(self):
        self._device = config_data['general']['devices']

    def get_Devices(self):
        return self._device
class Status:
    def __init__(self):
        self.status = config_data['general']['status']

