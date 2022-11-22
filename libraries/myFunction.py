import os
import psutil


def get_process_id():
    pid = os.getppid()
    return pid


def list_all_process_ids():
    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process detail as dictionary
        pInfoDict = proc.as_dict(attrs=['pid', 'name'])
        # Append dict of process detail in list
        listOfProcessNames.append(pInfoDict)
    return listOfProcessNames