# --------------------------------------------------------------------
# file name: fw_bot.py
# description: this class actually monitors and moves files based on
# the config file.
# --------------------------------------------------------------------
import time
from watchdog.observers import Observer
from common.file_event_handler import FileMoveEventHandler
from common.logger import Logger
import configparser

def is_client(config):
    b_client = True

    try:
        a_value = config.get("CLIENT","criteria1")
    except:
        b_client=False
    
    return b_client

def is_server(config):
    b_server = True

    try:
        a_value = config.get("SERVER","criteria1")
    except:
        b_server=False
    
    return b_server

def monitor_files(config):
    # create the event handler
    condition_map = {}
    
    if is_client(config):
        condition_map = {}
        # prepare the condition_map if it is a CLIENT
        for key, value in config.items("CLIENT"):
            
            # the * operator is used to assign multiple values from the result of value.split(',') to the variables key and value.
            criteria, file_type = key, *value.split(',')

            # populate the condition_map
            condition_map[criteria.strip()] = ("", file_type.strip(), "CLIENT")

    elif is_server(config):

        condition_map = {}
        # prepare the condition_map if it is a SERVER
        for key, value in config.items("SERVER"):
            
            # the * operator is used to assign multiple values from the result of value.split(',') to the variables key and value.
            criteria, search_word, file_type, destination_dir = key, *value.split(',')

            # populate the condition_map
            condition_map[criteria.strip()] = (search_word.strip(), file_type.strip(), destination_dir.strip())
    else:
        return False

    print(f"{condition_map}")
    # prepare for file move
    event_handler =  FileMoveEventHandler(config,condition_map)

    # start monitoring the source directory for file creation
    observer = Observer()
    source_dir = config.get('GENERAL', 'source_dir')
    observer.schedule(event_handler, source_dir, recursive=False)
    observer.start()

    # create the logger
    ini_file_path = config.get('GENERAL', 'ini_file_path')
    logger = Logger(ini_file_path)

    logger.info(f"Monitoring directory '{source_dir}'...")

    try:
        while True:
            time.sleep(1)

            # Check if the stop_flag is set to True in the config file
            config.read(ini_file_path)
            stop_flag = config.getboolean('FLAGS', 'stop_flag')
            
            if stop_flag:
                logger.info("Stopping the file monitoring.")
                break
        
        # means the process is stopped.
        observer.stop()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
