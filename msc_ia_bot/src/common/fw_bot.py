import time
from watchdog.observers import Observer
from common.file_handlers.file_event_handler import FileMoveEventHandler
from common.general_handlers.logger import Logger
import common.general_handlers.constants as cons

"""
**Module: fw_bot**

This module is used to trigger the file processing within the file_handler module.
"""

def monitor_files(config, sleep_time, b_execute_once=False):

    """
    This is function creates the on_created event for file handling with class FileMoveEventHandler.
    It also executes the function to process all the files within the file handling class.

    Args:
        config (object): The config file from the bot config.
        sleep_time (int): This is used to delay in checking the config stop_flag value.
        b_execute_once (boolean): Default False. Used to execute only once.

    Returns:
        boolean
    """
    
    # prepare for file move
    event_handler =  FileMoveEventHandler(config)
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

                if b_execute_once:
                    break
    
        observer.stop()
    except KeyboardInterrupt:
        observer.stop()
            
    observer.join()
    return True