import configparser
import os
import random
from datetime import datetime
from .functions import date_format,hash_format

config = configparser.ConfigParser()
config.read('config.ini')

class Generate_Files:

   def __init__(self):
      self.devices_status = config.get('general', 'devices_status').split(',')
      self.hash_format = hash_format
      self.date_format = date_format
      self.counter_folder = 0
      self.counter_file = 0

   def generate_mission_files(self,missions,num_files):
     self.counter_folder +=1
     current_directory = os.path.dirname(os.path.abspath(__file__))

     output_directory = os.path.join(current_directory, f"SIMULACIONES/Folder-{self.counter_folder}")


     if not os.path.exists(output_directory):
        os.makedirs(output_directory)

     all_files_data = []

     for mission in missions:
         name = mission["name"]
         components = mission["components"]

         status_components = {component : random.choice(self.devices_status) for component in components}


         component_data = [{"mission": name, "component": component, "status": status} for component, status in status_components.items()]
         all_files_data.extend(component_data)

     selected_files_data = random.choices(all_files_data, k=num_files)

     for file_data in selected_files_data:
         self.counter_file +=1
         name = file_data["mission"]
         component = file_data["component"]
         status = file_data["status"]
         date_time = self.date_format()
         hash_m =  self.hash_format(date_time,name,component,status)

         file_name = f"APL[{name}]-0000[{self.counter_file}].log"
         file_path = os.path.join(output_directory, file_name)

         if name == "UNKN":
            name = "Unknown"
            component = "Unknown"
            status = "Unknown"
            hash_m = f"{""}{""}{""}{""}"

         with open(file_path, 'w') as file:

            file.write("Date: " + date_time + "\n")
            file.write("Mission: " + name + "\n")
            file.write("Device Type: " + component + "\n")
            file.write("Device Status: " + status + "\n")
            file.write("Hash: " + hash_m + "\n")














