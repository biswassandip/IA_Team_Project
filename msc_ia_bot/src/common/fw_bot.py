# --------------------------------------------------------------------
# file name: fw_bot.py
# description: this class actually monitors and moves files based on
# the config file..
# --------------------------------------------------------------------
import time
from watchdog.observers import Observer
from common.file_handlers.file_event_handler import FileMoveEventHandler
from common.general_handlers.logger import Logger
import common.general_handlers.constants as cons


def rules_exists(config):
    b_exists = True

    try:
        config.get(cons.INI_HEADER_BOT_RULES, "criteria1")
    except:
        b_exists=False
    
    return b_exists

def monitor_files(config, sleep_time):
    
    if not rules_exists(config):
        return False
    
    # prepare the condition_map if it is a CLIENT
    condition_map = {}
    # prepare the condition_map if it is a SERVER
    for key, value in config.items(cons.INI_HEADER_BOT_RULES):
        
        # the * operator is used to assign multiple values from the result of value.split(',') to the variables key and value.
        criteria, search_word, file_type, sftp_host, sftp_port, destination_dir = key, *value.split(',')

        # populate the condition_map
        condition_map[criteria.strip()] = (search_word.strip(), file_type.strip(), sftp_host.strip(), sftp_port.strip(), destination_dir.strip())

    # prepare for file move
    event_handler =  FileMoveEventHandler(config,condition_map)
    event_handler.process_existing_files() # process the existing files

    # start monitoring the source directory for file creation
    observer = Observer()
    source_dir = config.get(cons.INI_HEADER_GENERAL, cons.KEY_SOURCE_DIR)
    observer.schedule(event_handler, source_dir, recursive=False)
    observer.start()

    # create the logger
    ini_file_path = config.get(cons.INI_HEADER_GENERAL, cons.KEY_INI_FILE_PATH)
    logger = Logger(ini_file_path)

    logger.info(f"Monitoring directory '{source_dir}'...")

    try:

        # Check if the stop_flag is set to True in the config file
        config.read(ini_file_path)
        stop_flag = config.getboolean(cons.INI_HEADER_FLAGS, cons.KEY_STOP_FLAG)

        if sleep_time>0:
            while (not stop_flag):
                time.sleep(sleep_time)

                # Check if the stop_flag is set to True in the config file
                config.read(ini_file_path)
                stop_flag = config.getboolean(cons.INI_HEADER_FLAGS, cons.KEY_STOP_FLAG)
                
                if stop_flag:
                    logger.info("Stopping the file monitoring.")
                    print(f"The file monitoring process has been stopped")
                    break
    
        observer.stop()
    except KeyboardInterrupt:
        observer.stop()
            
    observer.join()
    return True