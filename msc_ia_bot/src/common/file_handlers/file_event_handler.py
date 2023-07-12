# --------------------------------------------------------------------
# file name: fw_bot.py
# description: this class actually monitors and moves files based on
# the config file
# --------------------------------------------------------------------
import os, sys
import shutil
import fnmatch
from watchdog.events import FileSystemEventHandler
from common.general_handlers.logger import Logger
from common.general_handlers.utils import Utils
import common.general_handlers.constants as cons
from src.common.file_handlers.search_in_files import SearchInFiles

class FileMoveEventHandler(FileSystemEventHandler):

    # ====================================================================
    # initialize the config
    # ====================================================================
    def __init__(self, config, condition_map):
        self.config = config
        self.ini_file_path = self.config.get(cons.INI_HEADER_GENERAL, cons.KEY_INI_FILE_PATH)
        self.condition_map = condition_map

        # create the logger
        self.logger = Logger(config_file_path=self.ini_file_path)

        # get all the default paths
        self.source_dir = config.get(cons.INI_HEADER_GENERAL, cons.KEY_SOURCE_DIR)

        # to handle redundant file events
        self.last_processed_timestamp = None 

        # self.process_existing_files()


    # ====================================================================
    # when a file is created event
    # ====================================================================
    def on_created(self, event):

        if not event.is_directory:

            file_path = event.src_path
            file_name = os.path.basename(file_path)

            self.process_files(file_path, file_name)


    # ====================================================================
    # process all files in the existing source_dir when executed for the first time
    # ====================================================================
    def process_existing_files(self):

        b_return = True

        try:
            files = os.listdir(self.source_dir)
            for file_name in files:
                file_path = os.path.join(self.source_dir, file_name)
                self.process_files(file_path,file_name)
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return
        


    # ====================================================================
    # common rule for processing the file
    # ====================================================================
    def process_files(self, file_path, file_name):

        b_return = True

        try:

            for criteria, condition in self.condition_map.items():

                # get the respective criteria values
                search_word = self.condition_map[criteria][0]
                file_type = self.condition_map[criteria][1]
                sftp_host = self.condition_map[criteria][2]
                sftp_port = self.condition_map[criteria][3]
                destination_dir = self.condition_map[criteria][4]

                # booleans for respective operations
                b_search_on_file_type = False
                b_search_on_any_file = False
                b_file_type_only = False

                # if no destination directory is provided then skip
                if (not destination_dir):
                    self.logger.warning(f"No destination provided for criteria '{criteria}'")
                    b_matched = True
                    break

                # when search_word is provide and file_type is provided
                if (search_word and file_type):
                    # if the file create matches with the file_type
                    if fnmatch.fnmatch(file_name, file_type):
                        b_search_on_file_type = self.search_word_in_file(file_path, search_word)
                
                # when search_word is provide and file_type is NOT provided
                if (search_word and not file_type):
                    b_search_on_any_file = self.search_word_in_file(file_path, search_word)

                # when search_word is provide and file_type is NOT provided
                if (not search_word and file_type):
                    # if the file create matches with the file_type
                    if fnmatch.fnmatch(file_name, file_type):
                        b_file_type_only = True
                    elif (file_type=="*.*"):
                        b_file_type_only = True

                if (b_search_on_file_type or b_search_on_any_file or b_file_type_only):
                    self.move_file_to_destination(file_path,file_name,destination_dir)                    
                    self.logger.info(f"Moved file '{file_path}' to '{destination_dir}'")
                    b_matched = True
                    break
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return


    # ====================================================================
    # search a word in the file
    # ====================================================================
    def search_word_in_file(self, file_path, search_word):

        results = SearchInFiles(self.config, file_path, search_word)
        if len(results["files"])>0:
            return True
        else:
            return False


    # ====================================================================
    # move the file to destination
    # ====================================================================
    def move_file_to_destination(self, file_path, file_name, destination_dir):

        b_return = True

        try:
            Utils.create_dir(destination_dir)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(file_path, destination_path)
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return
