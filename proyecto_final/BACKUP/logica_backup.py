import os
import shutil
from datetime import datetime

# Source and destination paths
reports_directory_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\DEVICES\REPORTS'
simulations_directory_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\DEVICES\SIMULATIONS'
backUps_reports_directory_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\BACKUPS\REPORTS'
backUps_simulations_directory_path = r'C:\Users\miguel.mulcue\OneDrive - Inversiones Internacionales Grupo Sura S.A\Escritorio\Pyhton_RutaN\proyecto_final\BACKUPS\SIMULATIONS'


current_date = datetime.now().strftime("%Y%m%d-%H%M%S")

def move_files_reports(source_path=reports_directory_path, destination_path=backUps_reports_directory_path, name = current_date):
    """
    Move all reports from source to destination folder.

    :param source_path: Path to the source folder.
    :type source_path: str
    :param destination_path: Path to the destination folder.
    :type destination_path: str
    :param name: Unique identifier created with the current date and time.
    :type name: str
    """
    # Get the list of all files in the source folder
    files = os.listdir(source_path)

    try:
        # If no files are found, raise an exception
        if not files:
            raise FileNotFoundError("No files were found in the source folder.")

        # Create a folder with the current date in the format YYYYMMDD
        destination_folder = os.path.join(destination_path, name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move each file to the destination folder
        for file in files:
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(destination_folder, file)
            try:
                shutil.move(source_file_path, destination_file_path)
            except Exception as e:
                print(f"Error moving file {source_file_path} to {destination_file_path}: {e}")

    except FileNotFoundError as e:
        print(e)

def move_files_simulations(source_path=simulations_directory_path, destination_path=backUps_simulations_directory_path, name = current_date):
    """
    Move all simulations from source to destination folder.

    :param source_path: Path to the source folder.
    :type source_path: str
    :param destination_path: Path to the destination folder.
    :type destination_path: str
    :param name: Unique identifier created with the current date and time.
    :type name: str
    """
    # Get the list of all files in the source folder
    files = os.listdir(source_path)

    try:
        # If no files are found, raise an exception
        if not files:
            raise FileNotFoundError("No files were found in the source folder.")

        # Create a folder with the current date in the format YYYYMMDD
        destination_folder = os.path.join(destination_path, name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move each file to the destination folder
        for file in files:
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(destination_folder, file)
            try:
                shutil.move(source_file_path, destination_file_path)
            except Exception as e:
                print(f"Error moving file {source_file_path} to {destination_file_path}: {e}")

    except FileNotFoundError as e:
        print(e)

move_files_reports()
move_files_simulations()
