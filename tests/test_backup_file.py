import os
import shutil
from datetime import datetime

import pytest

from proyecto_final.DEVICES.backup import (move_files_reports,
                                           move_files_simulations)


# Config Tests
@pytest.fixture
def temp_directories():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    simulations_directory = os.path.join(current_directory, '..', 'proyecto_final', 'DEVICES', 'SIMULATIONS')
    backup_directory = os.path.join(current_directory, '..', 'proyecto_final', 'BACKUPS')
    reports_directory = os.path.join(current_directory, '..', 'proyecto_final', 'DEVICES','REPORTS')

    return simulations_directory, backup_directory, reports_directory

def test_move_files_simulations(temp_directories):
    print("****** Ejecutando test_move_files_simulations *******")
    source_path, destination_path, _ = temp_directories
    source_folder = os.path.join(source_path, 'simulation_folder')
    os.makedirs(source_folder)
    with open(os.path.join(source_folder, 'file1.txt'), 'w') as f:
        f.write("Contenido de file1.txt")

    move_files_simulations(source_path=source_path, destination_path=destination_path)

    assert not os.path.exists(os.path.join(source_folder, 'file1.txt')), "The origin file was move correctly"

    backups_content = os.listdir(destination_path)
    backup_directory_name = backups_content[0]

    backup_file_path = os.path.join(destination_path, backup_directory_name, 'simulation_folder', 'file1.txt')
    assert os.path.exists(backup_file_path), "The file exist"


def test_move_files_reports(temp_directories):

    simulations_directory, backup_directory, reports_directory = temp_directories

    date_formatted = "20220121"

    for i in range(3):
        with open(os.path.join(reports_directory, f"APLSTATS_{i}.log"), "w") as file:
            file.write(f"Sample content for APLSTATS_{i}")

    move_files_reports(source_path=reports_directory, destination_path=backup_directory, date_formatted=date_formatted)

    for i in range(3):
        source_file_path = os.path.join(reports_directory, f"APLSTATS_{i}.log")

        destination_file_path = os.path.join(backup_directory, date_formatted, f"APLSTATS_{i}.log")

        assert not os.path.exists(source_file_path)
        assert os.path.exists(destination_file_path)



