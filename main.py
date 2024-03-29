import argparse
import logging
import os
import time
from datetime import datetime

import schedule
import yaml

from proyecto_final.DEVICES.backup import ReportsMover, SimulationsMover
# from proyecto_final.DEVICES import backup
from proyecto_final.DEVICES.generate_mission_files import Generate_Files

current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
#################################################################
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

num_files_initial_config_yaml = config_data['general']['num_files_initial']
num_files_final_config_yaml = config_data['general']['num_files_final']
time_cycle_config_yaml = config_data['general']['time_cycle']

#################################################################
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.basicConfig(level=logging.WARNING, format='%(message)s')
logging.info("Welcome to APOLO 11 Project, it's activate")
logging.info("Program start")


def file_generator():
    logging.warning("Job function file_generator")
    generate_files_instance.generate_files(args.num_files_initial, args.num_files_final)


def report_generator():
    logging.warning("Job function report_generator")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.abspath(os.path.join(current_dir, 'proyecto_final', 'DEVICES', 'reports.py'))
    os.system(f'python {reports_dir}')


def main():
    logging.warning("main Running")
    schedule.every(args.time_cycle).seconds.do(file_generator)
    schedule.every(args.time_cycle).seconds.do(report_generator)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram finished by user. Back up folder with reports")
        reports_mover = ReportsMover(current_date)
        simulations_mover = SimulationsMover(current_date)
        reports_mover.move_files()
        simulations_mover.move_files()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nasa Python project')
    parser.add_argument('--num_files_initial',
                        type=int,
                        default=num_files_initial_config_yaml,
                        help="Number initial of files")
    parser.add_argument('--num_files_final',
                        type=int,
                        default=num_files_final_config_yaml,
                        help="Final number of files")
    parser.add_argument('--time_cycle',
                        type=int,
                        default=time_cycle_config_yaml,
                        help="Time in seconds for running the program")

    args = parser.parse_args()
    generate_files_instance = Generate_Files()
    main()
