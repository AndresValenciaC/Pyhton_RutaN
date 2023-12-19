import os
import random
import schedule

from project_dummy_data import project_missions,devices_status,hash_format,date_format

class Apolo11:

   mission_list = project_missions

   def generate_mission_files(missions,num_files):
     increment = lambda x: x + 1
     increment.counter = 0
     increment.counter += 1

     output_directory = f"SIMULACIONES/folder-{increment.counter}"


     if not os.path.exists(output_directory):
        os.makedirs(output_directory)

     all_files_data = []

     for mission in missions:
         name = mission["name"]
         component_data = []

         if name == "UNKN":
            name = "Unknown"
            components = "Unknown"
            status_components = "Unknown"
            component_data.append({"mission": name, "component": components, "status": status_components})
         else:
            components = mission["components"]
            status_components = {component : random.choice(devices_status) for component in components}
            component_data = [{"mission": name, "component": component, "status": status} for component, status in status_components.items()]    
         all_files_data.extend(component_data)

     selected_files_data = selected_files_data = random.choices(all_files_data, k=num_files)

     for file_data in selected_files_data:
         name = file_data["mission"]
         component = file_data["component"]
         status = file_data["status"]
         date_time = date_format()
         file_name = f"Mission_{name}_{component}_{date_time}_{random.randint(1, 100)}.txt"
         file_path = os.path.join(output_directory, file_name)

         with open(file_path, 'w') as file:
            if name == "Unknown":
               hash_m = "Unknown"
            else:
               hash_m = hash_format(date_time, name, component, status)

            file.write("Date: " + date_time + "\n")
            file.write("Mission: " + name + "\n")
            file.write("Device Type: " + component + "\n")
            file.write("Device Status: " + status + "\n")
            file.write("Hash: " + hash_m + "\n")

# Hola
# realizar cambio de prueba4











