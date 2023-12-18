import os
import random
from datetime import datetime
from .project_dummy_data import devices_status,hash_format,date_format

class Generate_Files:

   def __init__(self):
      self.devices_status = devices_status
      self.hash_format = hash_format
      self.date_format = date_format
      self.folder_counter = 0

   def generate_mission_files(self,missions,num_files):
     self.folder_counter +=1
     current_directory = os.path.dirname(os.path.abspath(__file__))
     date_time = datetime.now().strftime('%Y%m%d%H%M%S')
     output_directory = os.path.join(current_directory, f"SIMULACIONES/folder-{date_time}-{self.folder_counter}")


     if not os.path.exists(output_directory):
        os.makedirs(output_directory)

     all_files_data = []

     for mission in missions:
         name = mission["name"]
         components = mission["components"]

         status_components = {component : random.choice(self.devices_status) for component in components}

         component_data = [{"mission": name, "component": component, "status": status} for component, status in status_components.items()]
         all_files_data.extend(component_data)

     selected_files_data = selected_files_data = random.choices(all_files_data, k=num_files)

     for file_data in selected_files_data:
         name = file_data["mission"]
         component = file_data["component"]
         status = file_data["status"]
         date_time = self.date_format()
         file_name = f"Mission_{name}_{component}_{date_time}_{random.randint(1, 100)}.txt"
         file_path = os.path.join(output_directory, file_name)

         with open(file_path, 'w') as file:
            hash_m =  self.hash_format(date_time,name,component,status)
            file.write("Date: " + date_time + "\n")
            file.write("Mission: " + name + "\n")
            file.write("Device Type: " + component + "\n")
            file.write("Device Status: " + status + "\n")
            file.write("Hash: " + hash_m + "\n")














