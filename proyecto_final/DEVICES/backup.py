import os
import shutil
from datetime import datetime


# Source and destination paths
current_directory_path = os.path.dirname(os.path.abspath(__file__))
print(f"current_directory_path : {current_directory_path}")

proyecto_final_directory = os.path.abspath(os.path.join(current_directory_path, '..'))
print(f"proyecto_final_directory : {proyecto_final_directory}")

backUps_directory_path = os.path.abspath(os.path.join(proyecto_final_directory, 'BACKUPS'))
print(f"backUp_directory : {backUps_directory_path}")

reports_directory_path = os.path.abspath(os.path.join(current_directory_path, 'REPORTS'))
print(f"reports_directory_path : {reports_directory_path}")

simulations_directory_path = os.path.abspath(os.path.join(current_directory_path, 'SIMULATIONS'))
print(f"reports_directory_path : {simulations_directory_path}")

def move_files(source_path = reports_directory_path, destination_path = backUps_directory_path):
    """
    Move files starting with 'APLSTATS' from source to destination folder.

    :param source_path: Path to the source folder.
    :type source_path: str
    :param destination_path: Path to the destination folder.
    :type destination_path: str
    """
    # Get the list of files in the reports folder
    files = os.listdir(source_path)
    print(f" files reports folder -- {files}")

    # Filter files that start with "APLSTATS"
    aplstats_files = [file for file in files if file.startswith("APLSTATS")]
    print(f"aplstats_files -- {aplstats_files}")

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


def delete_simulations_files(simulations_path = simulations_directory_path):
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
