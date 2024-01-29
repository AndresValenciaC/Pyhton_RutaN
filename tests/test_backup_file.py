import os
from datetime import datetime

import pytest

from proyecto_final.DEVICES.backup import ReportsMover, SimulationsMover

current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
# Config Tests
@pytest.fixture
def temp_directories():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    simulations_directory = os.path.join(current_directory, '..', 'proyecto_final', 'DEVICES', 'SIMULATIONS')
    backup_directory = os.path.join(current_directory, '..', 'proyecto_final', 'BACKUPS')

    reports_directory = os.path.join(current_directory, '..', 'proyecto_final', 'DEVICES', 'REPORTS')

    return simulations_directory, backup_directory, reports_directory


def test_move_files_simulations(temp_directories):
    source_path, destination_path, _ = temp_directories
    source_folder = os.path.join(source_path, 'simulation_folder')
    os.makedirs(source_folder)
    with open(os.path.join(source_folder, 'file1.txt'), 'w') as f:
        f.write("Contenido de file1.txt")

    simulations_mover = SimulationsMover(current_date)
    simulations_mover.move_files()

    assert not os.path.exists(os.path.join(source_folder, 'file1.txt')), "The origin file was move correctly"

    backups_content = os.listdir(destination_path)
    print(f" backups_content {backups_content}")
    #backups_content ['SIMULATIONS', 'REPORTS']
    backup_directory_name = backups_content[0]
    print(f" backup_directory_name {backup_directory_name}")
    backup_file_path = os.path.join(destination_path, backup_directory_name, 'simulation_folder', 'file1.txt')
    print(f" backup_file_path {backup_file_path}")


