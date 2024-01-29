import os
import shutil

# Source and destination paths
current_dic_path = os.path.dirname(os.path.abspath(__file__))

proyecto_final_dic = os.path.abspath(os.path.join(current_dic_path, '..'))

backUps_dic_path = os.path.abspath(os.path.join(proyecto_final_dic, 'BACKUPS'))

backUps_dic_r_path = os.path.abspath(os.path.join(backUps_dic_path, 'REPORTS'))

backUps_dic_s_path = os.path.abspath(os.path.join(backUps_dic_path, 'SIMULATIONS'))

r_dic_path = os.path.abspath(os.path.join(current_dic_path, 'REPORTS'))

s_dic_path = os.path.abspath(os.path.join(current_dic_path, 'SIMULATIONS'))


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
        super().__init__(r_dic_path, backUps_dic_r_path, name)

    def display_info(self):
        """
        Override the display_info method for ReportsMover.
        """
        return f"ReportsMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"


class SimulationsMover(FileMover):
    def __init__(self, name):
        super().__init__(s_dic_path, backUps_dic_s_path, name)

    def display_info(self):
        """
        Override the display_info method for SimulationsMover.
        """
        return f"SimulationsMover - Source: {self.source_path}, Destination: {self.destination_path}, Name: {self.name}"
