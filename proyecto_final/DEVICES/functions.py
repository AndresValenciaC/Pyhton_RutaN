from datetime import datetime

def date_format():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')


def hash_format(date,mission,device_type,device_status):
    return date+"_"+mission+"_"+device_type+"_"+device_status