import os
import time
import pytest
from proyecto_final.DEVICES.generate_mission_files import Generate_Files

def test_create_output_directory():
    generator_instance = Generate_Files()
    num_folder = 5
    times_stamp = 123456789
    output_directory = generator_instance.create_output_directory(num_folder,times_stamp)
    assert output_directory == "/Users/andrescampovalencia/Desktop/proyecto_final/proyecto_final/DEVICES/SIMULATIONS/Folder-5-123456789"

def test_generate_file_data():
    generator_instance = Generate_Files()
    file_data = generator_instance.generate_file_data()
    print(file_data)
    assert "name" in file_data
    assert "component" in file_data
    assert "status" in file_data

def test_verify_file_format():
    output_directory = "/Users/andrescampovalencia/Desktop/proyecto_final/proyecto_final/DEVICES/SIMULATIONS/"
    instance = Generate_Files()
    num_files_from, num_files_to = 5, 10

    instance.generate_files(num_files_from, num_files_to)

    generated_folders  = os.listdir(output_directory)
    print(f"generated_folders: {generated_folders}") # folders

    for generated_folder in generated_folders:
        folder_path = os.path.join(output_directory, generated_folder)

        if os.path.isdir(folder_path):
            print(f"Processing contents of folder: {folder_path}")
            folder_files = os.listdir(folder_path)

            for file_name in folder_files:
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        content = file.read()

                        assert "Date:" in content
                        assert "MissionS:" in content
                        assert "Device Type:" in content
                        assert "Device Status:" in content
                        assert "Hash:" in content












