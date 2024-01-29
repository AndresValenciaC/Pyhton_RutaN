import os

from proyecto_final.DEVICES.generate_mission_files import Generate_Files

current_directory = os.path.dirname(os.path.abspath(__file__))
simulations_directory = os.path.join(current_directory, '..', 'proyecto_final', 'DEVICES', 'SIMULATIONS')

def test_create_output_directory():
    generator_instance = Generate_Files()
    num_folder = 5
    times_stamp = 123456789
    expected_output_directory = os.path.join(simulations_directory, f"Folder-{num_folder}-{times_stamp}")
    output_directory = generator_instance.create_output_directory(num_folder, times_stamp)
    assert output_directory == expected_output_directory


def test_generate_file_data():
    generator_instance = Generate_Files()
    file_data = generator_instance.generate_file_data()
    assert "name" in file_data
    assert "component" in file_data
    assert "status" in file_data


def test_verify_file_format():

    instance = Generate_Files()
    num_files_from, num_files_to = 5, 10

    instance.generate_files(num_files_from, num_files_to)

    generated_folders = os.listdir(simulations_directory)
    print(f"generated_folders: {generated_folders}")

    for generated_folder in generated_folders:
        folder_path = os.path.join(simulations_directory, generated_folder)

        if os.path.isdir(folder_path):
            print(f"Processing contents of folder: {folder_path}")
            folder_files = os.listdir(folder_path)
            print(f"Processing contents of folder_files: {folder_files}")

            for file_name in folder_files:
                file_path = os.path.join(folder_path, file_name)
                print(f"file path {file_path}")

                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        content = file.read()

                        assert "Date:" in content
                        assert "Mission:" in content
                        assert "Device Type:" in content
                        assert "Device Status:" in content
                        assert "Hash:" in content
