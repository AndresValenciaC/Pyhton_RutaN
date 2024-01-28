
def hash_format(date, mission, device_type, device_status):
    """Generates unique hash for each simulation mission.Using and concatenating all the information of mission

    :param date: we use the date function to bring the information from generate_mission_files.py.
    :type date: str
    :param mission: we use the date function to bring the information from generate_mission_files.py
    :type mission: str
    :param device_type: we use the date function to bring the information from generate_mission_files.py
    :type device_type: str
    :param device_status: we use the date function to bring the information from generate_mission_files.py
    :type device_status: str
    :return: we use the date function to bring the information from generate_mission_files.py
    :rtype: str
    """
    return date + "_" + mission + "_" + device_type + "_" + device_status
