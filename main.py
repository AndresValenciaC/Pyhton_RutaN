import configparser
import schedule
import time
from proyecto_final.DEVICES.generate_mission_files import Generate_Files

config = configparser.ConfigParser()
config.read('config.ini')


num_files_initial = config.getint('general', 'num_files_initial')
num_files_final = config.getint('general', 'num_files_final')
time_cycle_config = config.getint('general', 'time_cycle')

print("Script Start")
generate_files_instance = Generate_Files()

def file_generator():
    print("Job function")
    generate_files_instance.generate_files(num_files_initial, num_files_final)


def main():
    print("main")
    schedule.every(time_cycle_config).seconds.do(file_generator)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
 main()