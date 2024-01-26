import os
import shutil
from datetime import datetime

import yaml

# Source and destination paths
current_dic_path = os.path.dirname(os.path.abspath(__file__))
# print(f"current_dic_path : {current_dic_path}")

proyecto_final_dic = os.path.abspath(os.path.join(current_dic_path, '..'))
# print(f"proyecto_final_dic : {proyecto_final_dic}")

backUps_dic_path = os.path.abspath(os.path.join(proyecto_final_dic, 'BACKUPS'))
# print(f"backUp_dic : {backUps_dic_path}")

r_dic_path = os.path.abspath(os.path.join(current_dic_path, 'REPORTS'))
# print(f"reports_dic_path : {reports_dic_path}")

s_dic_path = os.path.abspath(os.path.join(current_dic_path, 'SIMULATIONS'))
# print(f"reports_dic_path : {simulations_dic_path}")

#################################################################

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

date_format = config_data['general']['date_format']

current_date = datetime.now().strftime(date_format)

#################################################################


def move_files_simulations(source_path=s_dic_path, destination_path=backUps_dic_path, name=current_date):
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


def move_files_reports(source_path=r_dic_path, destination_path=backUps_dic_path, date_formatted=current_date):
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

        destination_folder = os.path.join(destination_path, date_formatted)

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
