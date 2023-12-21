import configparser
import time
from proyecto_final.DEVICES.generate_mission_files import Generate_Files
from proyecto_final.DEVICES.project_dummy_data import project_missions

config = configparser.ConfigParser()
config.read('config.ini')

num_files_config = config.get('general', 'num_files')
time_cycle_config = config.get('general', 'time_cycle')
print("Script Start")
generate_files_instance = Generate_Files()

def file_generator():
    print("¡The function is running!")
    num_files = int(num_files_config)
    generate_files_instance.generate_mission_files(project_missions,num_files)

def main():

    while True:
        print("¡Testing schedule!")
        file_generator()

        time.sleep(int(time_cycle_config))


if __name__ == "__main__":
    main()
