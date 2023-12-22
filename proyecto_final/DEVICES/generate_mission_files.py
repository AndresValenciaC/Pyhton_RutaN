import os
import random
from .functions import date_format, hash_format
from .classes import Mission, Devices, Status

class Generate_Files:
    def __init__(self):
        self.mission_instance = Mission()
        self.devices_instance = Devices()
        self.status_instance = Status()
        self.hash_format = hash_format
        self.date_format = date_format
        self.file_number = 0

    def create_output_directory(self, num_folder):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        output_directory = os.path.join(current_directory, f"SIMULATIONS/Folder-{num_folder}")
        os.makedirs(output_directory, exist_ok=True)
        return output_directory

    def generate_file_data(self):
        return {
            "name": random.choice(self.mission_instance.mission),
            "component": random.choice(self.devices_instance.device),
            "status": random.choice(self.status_instance.status),
        }

    def generate_files(self, num_files_from, num_files_to):
        num_folder = num_files_to - num_files_from
        output_directory = self.create_output_directory(num_folder)

        all_files_data = [self.generate_file_data() for _ in range(num_files_from, num_files_to)]

        for file_data in all_files_data:
            self.file_number += 1
            name, component, status = file_data["name"], file_data["component"], file_data["status"]
            date_time = self.date_format()
            hash_m = self.hash_format(date_time, name, component, status)

            if name == "UNKN":
                name, component, status, hash_m = "Unknown", "Unknown", "Unknown", ""

            file_name = f"APL[{name}]-0000[{self.file_number}].log"
            file_path = os.path.join(output_directory, file_name)

            with open(file_path, 'w') as file:
                file.write(f"Date: {date_time}\n")
                file.write(f"Mission: {name}\n")
                file.write(f"Device Type: {component}\n")
                file.write(f"Device Status: {status}\n")
                file.write(f"Hash: {hash_m}\n")


