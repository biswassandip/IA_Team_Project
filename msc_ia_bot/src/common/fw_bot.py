# --------------------------------------------------------------------
# file name: fw_bot.py
# description: this class actually monitors and moves files based on
# the config file..
# --------------------------------------------------------------------
import time
from watchdog.observers import Observer
from common.file_event_handler import FileMoveEventHandler
from common.logger import Logger
import configparser

def rules_exists(config):
    b_exists = True

    try:
        a_value = config.get("BOT_RULES","criteria1")
    except:
        b_exists=False
    
    return b_exists

def monitor_files(config):

    # create the event handler
    condition_map = {}
    
    if not rules_exists(config):
        return False
    
    # prepare the condition_map if it is a CLIENT
    condition_map = {}
    # prepare the condition_map if it is a SERVER
    for key, value in config.items("BOT_RULES"):
        
        # the * operator is used to assign multiple values from the result of value.split(',') to the variables key and value.
        criteria, search_word, file_type, sftp_host, sftp_port, destination_dir = key, *value.split(',')

        # populate the condition_map
        condition_map[criteria.strip()] = (search_word.strip(), file_type.strip(), sftp_host.strip(), sftp_port.strip(), destination_dir.strip())

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

        # Check if the stop_flag is set to True in the config file
        config.read(ini_file_path)
        stop_flag = config.getboolean('FLAGS', 'stop_flag')

        while (not stop_flag):
            time.sleep(2)

            # Check if the stop_flag is set to True in the config file
            config.read(ini_file_path)
            stop_flag = config.getboolean('FLAGS', 'stop_flag')
            
            if stop_flag:
                logger.info("Stopping the file monitoring.")
                print(f"The file monitoring process has been stopped")
                break
    
        observer.stop()
    except KeyboardInterrupt:
        observer.stop()
            
    observer.join()
    return True