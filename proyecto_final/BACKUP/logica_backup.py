import os
import shutil
from datetime import datetime

def delete_simulation_files(simulations_path):
    """
    Delete all files within the SIMULATIONS folder.

    :param simulations_path: Path to the SIMULATIONS folder.
    :type simulations_path: str
    """
    # Delete all files within SIMULATIONS
    for folder in os.listdir(simulations_path):
        folder_path = os.path.join(simulations_path, folder)
        try:
            shutil.rmtree(folder_path)
        except Exception as e:
            print(f"Error deleting folder {folder_path}: {e}")

def move_files(source_path, destination_path):
    """
    Move files starting with 'APLSTATS' from source to destination folder.

    :param source_path: Path to the source folder.
    :type source_path: str
    :param destination_path: Path to the destination folder.
    :type destination_path: str
    """
    # Get the list of files in the source folder
    files = os.listdir(source_path)

    # Filter files that start with "APLSTATS"
    aplstats_files = [file for file in files if file.startswith("APLSTATS")]

    try:
        # If no 'APLSTATS' files are found, raise an exception
        if not aplstats_files:
            raise FileNotFoundError("No files with the name 'APLSTATS' were found.")

        # Create a folder with the current date in the format YYYYMMDD
        current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
        destination_folder = os.path.join(destination_path, current_date)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move each file to the destination folder
        for file in aplstats_files:
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(destination_folder, file)
            try:
                shutil.move(source_file_path, destination_file_path)
                print(f"File {file} moved to {destination_file_path}")
            except Exception as e:
                print(f"Error moving file {source_file_path} to {destination_file_path}: {e}")

    except FileNotFoundError as e:
        print(e)
        
# Source and destination paths
source_path = os.path.abspath(r'Pyhton_RutaN\proyecto_final\DEVICES\REPORTS')
destination_folder = os.path.abspath(r'Pyhton_RutaN\proyecto_final\BACKUP')
simulations_path = os.path.abspath(r'Pyhton_RutaN\proyecto_final\DEVICES\SIMULATIONS')


delete_simulation_files(simulations_path)
move_files(source_path, destination_folder) 
