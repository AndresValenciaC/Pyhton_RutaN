import os
import shutil
from datetime import datetime 

# Source and destination paths
current_dic_path = os.path.dirname(os.path.abspath(__file__))
# print(f"current_dic_path : {current_dic_path}")

proyecto_final_dic = os.path.abspath(os.path.join(current_dic_path, '..'))
# print(f"proyecto_final_dic : {proyecto_final_dic}")

backUps_dic_path = os.path.abspath(os.path.join(proyecto_final_dic, 'BACKUPS'))
# print(f"backUp_dic : {backUps_dic_path}")

backUps_dic_r_path = os.path.abspath(os.path.join(backUps_dic_path, 'REPORTS'))
# print(f"backUp_dic : {backUps_dic_path}")

backUps_dic_s_path = os.path.abspath(os.path.join(backUps_dic_path, 'SIMULATIONS'))
# print(f"backUp_dic : {backUps_dic_path}")

r_dic_path = os.path.abspath(os.path.join(current_dic_path, 'REPORTS'))
# print(f"reports_dic_path : {reports_dic_path}")

s_dic_path = os.path.abspath(os.path.join(current_dic_path, 'SIMULATIONS'))
# print(f"reports_dic_path : {simulations_dic_path}")


#################################################################


class FileMover:
    def __init__(self, source_path, destination_path, name):
        self.source_path = source_path
        self.destination_path = destination_path
        self.name = name

    def move_files(self):
        files = os.listdir(self.source_path)

        try:
            if not files:
                raise FileNotFoundError(f"No files were found in the source folder: {self.source_path}")

            destination_folder = os.path.join(self.destination_path, self.name)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            for file in files:
                source_file_path = os.path.join(self.source_path, file)
                destination_file_path = os.path.join(destination_folder, file)

                try:
                    shutil.move(source_file_path, destination_file_path)
                except FileNotFoundError as e:
                    print(f"Error: File not found - {e}")
                except PermissionError as e:
                    print(f"Error: Permission denied - {e}")
                except Exception as e:
                    print(f"Error: Unexpected error - {e}")

        except FileNotFoundError as e:
            print(f"Error: Source folder not found - {e}")

    def display_info(self):
        """
        Display information about the FileMover.
        """
        return f"FileMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"

class ReportsMover(FileMover):
    def __init__(self, name):
        super().__init__(r_dic_path, backUps_dic_s_path, name)

    def display_info(self):
        """
        Override the display_info method for ReportsMover.
        """
        return f"ReportsMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"

class SimulationsMover(FileMover):
    def __init__(self, name):
        super().__init__(s_dic_path, backUps_dic_r_path, name)

    def display_info(self):
        """
        Override the display_info method for SimulationsMover.
        """
        return f"SimulationsMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"
    
def main():
    current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    reports_mover = ReportsMover(current_date)
    simulations_mover = SimulationsMover(current_date)
    reports_mover.move_files()
    info_reports_mover = reports_mover.display_info()
    simulations_mover.move_files()
    info_simulations_mover = simulations_mover.display_info()
    print(info_reports_mover)
    print(info_simulations_mover)

if __name__ == "_main_":
    main()