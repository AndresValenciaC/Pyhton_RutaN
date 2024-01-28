import os
import shutil
from datetime import datetime

# Source and destination paths
repo_dic_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\DEVICES\REPORTS'
simul_dic_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\DEVICES\SIMULATIONS'
backUps_repo_dic_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\BACKUPS\REPORTS'
backUps_simul_dic_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\BACKUPS\SIMULATIONS'

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
                except Exception as e:
                    # Handle the error as needed
                    pass

        except FileNotFoundError as e:
            # Handle the error as needed
            pass

    def display_info(self):
        """
        Display information about the FileMover.
        """
        return f"FileMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"

class ReportsMover(FileMover):
    def __init__(self, name):
        super().__init__(repo_dic_path, backUps_repo_dic_path, name)

    def display_info(self):
        """
        Override the display_info method for ReportsMover.
        """
        return f"ReportsMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"

class SimulationsMover(FileMover):
    def __init__(self, name):
        super().__init__(simul_dic_path, backUps_simul_dic_path, name)

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

if __name__ == "__main__":
    main()