import configparser
import schedule
import time
import os
from proyecto_final.DEVICES.generate_mission_files import Generate_Files
from proyecto_final.DEVICES import backup

config = configparser.ConfigParser()
config.read('config.ini')

num_files_initial = config.getint('general', 'num_files_initial')
num_files_final = config.getint('general', 'num_files_final')
time_cycle_config = config.getint('general', 'time_cycle')
time_limit_config = config.getint('general', 'time_limit')

print("Script Start")
generate_files_instance = Generate_Files()

def file_generator():
    print("Job function file_generator")
    generate_files_instance.generate_files(num_files_initial, num_files_final)

def report_generator():
    print("Job function report_generator")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.abspath(os.path.join(current_dir,'proyecto_final','DEVICES','reports.py'))
    os.system(f'python {reports_dir}')

def main():
    print("main")
    job_file_generation = schedule.every(time_cycle_config).seconds.do(file_generator)
    job_report_generation =  schedule.every(time_cycle_config).seconds.do(report_generator)

    time_start = time.time()

    try:
        while time.time() - time_start < time_limit_config:

            schedule.run_pending()
            time.sleep(1)

        schedule.cancel_job(job_file_generation)
        schedule.cancel_job(job_report_generation)

        backup.move_files()
        backup.delete_simulations_files()

    except KeyboardInterrupt:
        print("Interruption by key board")


if __name__ == "__main__":
 main()
