import os

import yaml

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
config_path = os.path.join(project_dir, 'config.ini')

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)


class Mission:
    def __init__(self):
        self.mission = config_data['general']['missions']

class Devices:
    def __init__(self):
        self.device = config_data['general']['devices']

class Status:
    def __init__(self):
        self.status = config_data['general']['status']

