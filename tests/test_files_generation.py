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

    generated_files = os.listdir(output_directory)
    print(f"output_directory: {output_directory}")

    for generated_file in generated_files:
        file_path = os.path.join(output_directory, generated_file)

        if os.path.isfile(file_path):
            print(f"file_path: {file_path}")

            with open(file_path, 'r') as file:
                content = file.read()
                print(f"File Content:\n{content}")

                assert "Date:" in content
                assert "Mission:" in content
                assert "Device Type:" in content
                assert "Device Status:" in content
                assert "Hash:" in content

