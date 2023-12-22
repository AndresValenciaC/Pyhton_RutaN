import configparser
import schedule
import time
import random
from proyecto_final.DEVICES.generate_mission_files import Generate_Files


config = configparser.ConfigParser()
config.read('config.ini')

num_files_initial = random(config.get('general', 'num_files_initial'))
num_files_final = random(config.get('general', 'num_files_final'))
time_cycle_config = config.get('general', 'time_cycle')

print("Script Start")
generate_files_instance = Generate_Files()

def file_generator():
    generate_files_instance.generate_files(num_files_initial,num_files_final)

    def main():
     schedule.every(time_cycle_config).minutes.do(file_generator)

     while True:
        print("¡Testing schedule!")
        schedule.run_pending()
        time.sleep(1)


    if __name__ == "__main__":
     main()