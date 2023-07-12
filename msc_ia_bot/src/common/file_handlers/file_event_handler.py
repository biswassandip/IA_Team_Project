import os, sys
import shutil
import fnmatch
from watchdog.events import FileSystemEventHandler
from common.general_handlers.logger import Logger
from common.general_handlers.utils import Utils
import common.general_handlers.constants as cons
from src.common.file_handlers.keyword_in_file import KeywordInFile

"""
**class: FileMoveEventHandler**

This class is responsible to perform the actual processing of the files as defined within the bot config file.
It gets all the files from the source directory and performs processing as per the bot rules.
This class also raises an even when a new file is created within the source dir.
"""


class FileMoveEventHandler(FileSystemEventHandler):

    """
    This class is used to trigger the processing when
    1. The program is run for initially by processing on the files within the directory.
    2. The event triggered when a file is created.

    init args:
        config (object): The config ini file.
        condition_map: The conditions that needs to be applied.
    """

    def __init__(self, config):

        self.config = config
        self.ini_file_path = self.config.get(cons.INI_HEADER_GENERAL, cons.KEY_INI_FILE_PATH)

        # create the logger
        self.logger = Logger(config_file_path=self.ini_file_path)

        # get all the default paths
        self.source_dir = config.get(cons.INI_HEADER_GENERAL, cons.KEY_SOURCE_DIR)

        # to handle redundant file events
        self.last_processed_timestamp = None 

        self.condition_map = self._get_condition_map()
        self.common_file_types = [ext.strip() for ext in self.config[cons.INI_HEADER_SEARCH_IN_FILE_TYPES][cons.KEY_INCLUDE].split(',')]


    def _rules_exists(self):

        """
        This function checks whether there are rules defined or not

        Returns:
            boolean
        """
    
        b_exists = True

        try:
            self.config.get(cons.INI_HEADER_BOT_RULES, "criteria1")
        except:
            b_exists=False
        
        return b_exists


    def _get_condition_map(self):

        """
        This function creates the condition map based on the bot rules within the config file.

        Returns:
            condition_map (list): It is a list of all the rule items
        """

        bot_rules_map = {}

        if self._rules_exists():
            
            for key, value in self.config.items(cons.INI_HEADER_BOT_RULES):
                
                # the * operator is used to assign multiple values from the result of value.split(',') to the variables key and value.
                criteria, search_word, file_type, sftp_host, sftp_port, destination_dir = key, *value.split(',')

                # populate the condition_map
                bot_rules_map[criteria.strip()] = (search_word.strip(), file_type.strip(), sftp_host.strip(), sftp_port.strip(), destination_dir.strip())

        return bot_rules_map


    def on_created(self, event):

        """
        This function will be triggered when a file is created.

        Args:
            event: This is created whenever a file is created
        """

        if not event.is_directory:

            file_path = event.src_path
            self.process_files(file_path)


    def process_existing_files(self):

        """
        This function will process on all the files within a directory.
        """

        b_return = True

        try:
            files = os.listdir(self.source_dir)
            for file_name in files:
                file_path = os.path.join(self.source_dir, file_name)
                self.process_files(file_path)
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return
        

    def process_files(self, file_path):

        """
        This is the main function that will process the file based on the condition map or bot rules.

        Args:
            file_path (str): File path to be processed.

        Returns:
            boolean
        """

        b_return = False
        file_name = Utils.get_file_name(file_path)

        try:

            for criteria, condition in self.condition_map.items():

                # get the respective criteria values
                search_word = self.condition_map[criteria][0]
                file_type = self.condition_map[criteria][1]
                sftp_host = self.condition_map[criteria][2]
                sftp_port = self.condition_map[criteria][3]
                destination_dir = self.condition_map[criteria][4]

                # if no destination directory is provided then skip
                if (not destination_dir):
                    self.logger.warning(f"No destination provided for criteria '{criteria}'")
                    b_return = False
                    break

                # when search_word is provide and file_type is provided
                if (search_word and file_type):
                    # if the file create matches with the file_type
                    if fnmatch.fnmatch(file_name, "*"+file_type):
                        b_return = self.search_word_in_file(file_path, search_word, self.common_file_types)
                
                # when search_word is provide and file_type is NOT provided
                elif (search_word and not file_type):
                    b_return = self.search_word_in_file(file_path, search_word, self.common_file_types)

                # when search_word is NOT provided and file_type is provided
                elif (not search_word and file_type):
                    # if the file create matches with the file_type
                    if (fnmatch.fnmatch(file_name, "*"+file_type) or file_type=="*.*"):
                        b_return = True

                if b_return:
                    self.move_file_to_destination(file_path, destination_dir)                    
                    self.logger.info(f"Moved file '{file_path}' to '{destination_dir}'")
                    break
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return


    def search_word_in_file(self, file_path, keyword, common_file_types):
        """
        This is the function that triggers keyword searching within given file types.

        Args:
            file_path (str): File path to be processed.
            keyword (str): keyword to find

        Returns:
            boolean
        """
        keywordInFile = KeywordInFile()
        results = keywordInFile.search_keyword_in_files(file_path, keyword, common_file_types)
        return results


    def move_file_to_destination(self, file_path, destination_dir):

        """
        This is the function moves the file based on the destination.

        Args:
            file_path (str): File path to be processed.
            file_name (str): File name to be processed.
            destination_dir(str): The destination directory.

        Returns:
            boolean
        """

        b_return = True
        file_name = Utils.get_file_name(file_path)

        try:
            Utils.create_dir(destination_dir)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(file_path, destination_path)
        except:
            self.logger.error(str(sys.exc_info()[1]))
            b_return = False

        return b_return


if __name__ == '__main__':
    print(f"")