import os
from .Config import Config
from mimecast.logger import log

Config = Config()


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
        return data
    except Exception as e:
        log.error('Error reading file ' + file_name + '. Cannot continue. Exception: ' + str(e))
        quit()


def append_file(file_name, data_to_write):  # Do not append duplicate data to file
    try:
        found = False
        logfile = open(file_name, 'r')
        loglist = logfile.readlines()
        for line in loglist:
            if str(data_to_write) in line:
                found = True

        if not found:
            with open(file_name, 'a+', encoding="utf-8") as f:
                f.write(data_to_write + '\n')
    except Exception as e:
        log.error('Error reading file ' + file_name + '. Cannot continue. Exception: ' + str(e))
        quit()


def write_file(file_name, data_to_write, path=None):
    try:
        if path is not None:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}/{file_name}", 'w', encoding="utf-8") as f:
                f.write(data_to_write)
        else:
            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(data_to_write)
    except Exception as e:
        log.error('Error writing file ' + file_name + '. Cannot continue. Exception: ' + str(e))
        quit()


def delete_file(file_name):
    try:
        os.remove(file_name)
    except Exception as e:
        log.error('Error deleting file ' + file_name + '. Cannot continue. Exception: ' + str(e))
        quit()
