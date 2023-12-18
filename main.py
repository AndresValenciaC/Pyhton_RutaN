import schedule
import time
from proyecto_final.DEVICES.generate_mission_files import Generate_Files
from proyecto_final.DEVICES.project_dummy_data import project_missions

print("Script Start")

def file_generator():
    print("¡The function is running!")
    instance = Generate_Files()
    num_files = 5
    instance.generate_mission_files(project_missions,num_files)

def main():
    schedule.every(5).minutes.do(file_generator)

    while True:
        print("¡Testing schedule!")
        file_generator()
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
