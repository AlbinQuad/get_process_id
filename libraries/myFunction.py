import os

def get_process_id():
    pid = os.getppid()
    return pid