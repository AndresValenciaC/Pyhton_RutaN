import os
import random
import time
from datetime import datetime
import yaml
from .classes import Devices, Mission, Status
from .functions import hash_format


class Generate_Files:

    def __init__(self):
        with open('config.yaml', 'r') as file:
            config_data = yaml.safe_load(file)

        date_format = config_data['general']['date_format']

        now = datetime.now()
        self.date_formatted = now.strftime(date_format)

        self.mission_instance = Mission()
        self.devices_instance = Devices()
        self.status_instance = Status()
        self.hash_format = hash_format

    def create_output_directory(self, num_folder: int, times_stamp):
        """This method will create a directory in the correct path
        :param num_folder: folder number
        :type num_folder: int
        :param times_stamp: unique id for the folder
        :return: will return the output_directory path
        :rtype: string
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        output_directory = os.path.join(current_directory, f"SIMULATIONS/Folder-{num_folder}-{times_stamp}")

        os.makedirs(output_directory, exist_ok=True)
        return output_directory

    def generate_file_data(self):
        """The method will return the data to create the files
        :return: random data
        """
        return {
            "name": random.choice(self.mission_instance.mission),
            "component": random.choice(self.devices_instance.device),
            "status": random.choice(self.status_instance.status),
        }

    def generate_files(self, num_files_from: int, num_files_to: int):
        """This function takes create_output_directory to create folders
        and put them in the wanted path and the function generate_file_data
        to get the necessary info for the creation of the files

        :param num_files_from: the start number for the range of numbers
        :type num_files_from: int
        :param num_files_to: the final number for the range of numbers
        :type num_files_to: int
        """
        timestamp = int(time.time())
        num_random = random.randrange(num_files_from, num_files_to)
        output_directory = self.create_output_directory(num_random, timestamp)

        # This data structure generates the data as many times required for each file
        all_files_data = [self.generate_file_data() for _ in range(num_random)]
        self.file_number = 0

        for file_data in all_files_data:
            self.file_number += 1
            name, component, status = file_data["name"], file_data["component"], file_data["status"]
            date_time = self.date_formatted
            hash_m = self.hash_format(date_time, name, component, status)

        if name == "UNKN":
            name, component, status, hash_m = "Unknown", "Unknown", "unknown", "unknown"

        file_name = f"APL[{name}]-0000[{self.file_number}].log"
        file_path = os.path.join(output_directory, file_name)

        with open(file_path, 'w') as file:
            file.write(f"Date: {date_time}\n")
            file.write(f"Mission: {name}\n")
            file.write(f"Device Type: {component}\n")
            file.write(f"Device Status: {status}\n")
            file.write(f"Hash: {hash_m}\n")


# instancia = Generate_Files()
# if __name__ == "__main__":
# instancia.generate_files(5, 12)
