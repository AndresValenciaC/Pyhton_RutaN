import configparser
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
config_path = os.path.join(project_dir, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

class Mission:
    def __init__(self):
        self.mission = config.get('general', 'missions').split(',')

class Devices:
    def __init__(self):
        self.device = config.get('general', 'devices').split(',')

class Status:
    def __init__(self):
        self.status = config.get('general', 'status').split(',')

