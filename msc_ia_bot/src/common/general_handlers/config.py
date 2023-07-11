"""
**Module:** Config.py

This class is responsible to create the bot_config.ini file.
By default, the ini file is created within ./IA_BOT directory.

The entries within the ini file is used dynamically by the program to perform the required functionality based on the **BOT_RULES** configurations.
The **BOT_RULES** configuration is based on what is required for the criteria.
The criteria can be provided as comma separated rules for example:

Note that the structure the BOT_RULES criteria is a comma separated string that can comprise of:

    * criteria1 - this is the **MANDATORY** name given to the rule. The name of the rule **MUST** be **UNIQUE**.
    * search_word - this could be any word that needs to be searched. Either or Both search_word and file_type **MUST** be provided.
    * sftp_host - this is the sftp host or IP address. **Mandatory** only if the file needs to be SFTP'ed.
    * sftp_port - this is the port number. **Mandatory** only if the file needs to be SFTP'ed.
    * destination_dir - path where the file needs to be moved. This is **MANDATORY**

Some examples are given below:
    * Example; criteria1: business, *.doc, 22.22.22.22, 456, /remote/sftp/path/dir1
    In this case, if the word "business" is found in the file then it will be sftp'ed to the given directory.

    * Example; criteria1: business, , 22.22.22.22, 456, /remote/sftp/path/dir2
    In this case, if the word "business" is found in the any file then it will be sftp'ed to the given directory.

    * Example; criteria1: ,*.doc , 22.22.22.22, 456, /remote/sftp/path/dir3
    In this case, if the file type of *.doc then it will be sftp'ed to the given directory.

    * Example; criteria1: business ,*.doc , , , /local/dir1
    In this case, if the word "business" is found in the file then it will be moved to the given directory.

and so on....
"""

from configparser import ConfigParser
from common.general_handlers.utils import Utils
import common.general_handlers.constants as cons
from common.general_handlers.logger import Logger

import os
import sys
import paramiko
import os


class Config:

    """
    This class is initialized at the minimum with the ini file path so that the bot_config.ini file can be created.
    The ini files is created by default at "./IA_BOT/bot.ini".
    Note that if the source path is not provided then the current path will be considered source where all the files 
    will be processed.

    :param ini_file_path: Ths will be the path where the ini file needs to be created.
    :type option: string 

    :param source_dir: Ths will be the source directory that is required to be monitored.
    :type option: string 
    
    :return: None
    """

    def __init__(self,
                 ini_file_path=cons.INI_FILE_PATH,
                 source_dir=None,
                 ) -> None:



        self.ini_file_path = Utils.full_path(ini_file_path)
        self.source_dir = Utils.full_path(source_dir)
        self.log_file = Utils.full_path(cons.LOG_FILE)
        self.rotate_logs = cons.ROTATE_LOGS
        self.rotation_size = cons.ROTATION_SIZE
        self.num_processes = cons.NUM_PROCESSES
        self.scaling_factor = cons.SCALING_FACTOR
        self.min_processes = cons.MIN_PROCESSES

        self.cp_obj = ConfigParser()  # config parser object


    def create_config(self):
        """
        **Method:** create_config

        This method will create the actual config file with required configurations for:

        * [GENERAL] - consists of  general settings like ini file path, source directory, etc.
        * [SEARCH_IN_FILE_TYPES] - consists of filter types that will be included and excluded in word search.
        * [BOT_RULES] - consists of the various combinations for the rules criteria
        * [SFTP_KEYS] - provides with the private key path
        * [PROCESSES] -  settings for number of processes to be run
        * [FLAGS] - settings to stop the process (=True)
        
        :return: boolean
        """

        b_config = True

        try:

            # create the default config
            self.cp_obj[cons.INI_HEADER_GENERAL] = {
                cons.KEY_INI_FILE_PATH: self.ini_file_path,
                cons.KEY_SOURCE_DIR: self.source_dir,
                cons.KEY_LOG_FILE: self.log_file,
                cons.KEY_ROTATION_LOGS: self.rotate_logs,
                cons.KEY_ROTATION_SIZE: self.rotation_size
            }

            # create the search file types for include and exclude
            self.cp_obj[cons.INI_HEADER_SEARCH_IN_FILE_TYPES] = {
                cons.KEY_INCLUDE: cons.VALUE_INCLUDE,
                cons.KEY_EXCLUDE: cons.VALUE_EXCLUDE,
            }

            # create the search config
            self.cp_obj[cons.INI_HEADER_BOT_RULES] = {
                "criteria1": "search_word, file_type, sftp_host, sftp_port, destination_dir",
                "criteria2": "search_word, , sftp_host, sftp_port, destination_dir",
                "criteria3": ", file_type, sftp_host, sftp_port, destination_dir",
                "criteria4": "search_word, file_type, , , destination_dir",
                "criteria5": "search_word, , , , destination_dir",
                "criteria6": ", file_type, , , destination_dir",
            }

            # create the keys config
            self.cp_obj[cons.INI_HEADER_SFTP_KEYS] = {
                cons.KEY_PF_FILE: cons.PRIVATE_KEY_PATH,
            }

            # create the processes config
            self.cp_obj[cons.INI_HEADER_PROCESSES] = {
                cons.KEY_NUM_PROCESSES: self.num_processes,
                cons.KEY_SCALING_FACTOR: self.scaling_factor,
                cons.KEY_MIN_PROCESSES: self.min_processes
            }

            # create the flags config
            self.cp_obj[cons.INI_HEADER_FLAGS] = {
                cons.KEY_STOP_FLAG: cons.STOP_FLAG
            }

            # create the required directories
            Utils.create_dir(self.log_file, True)

            Utils.create_dir(cons.PRIVATE_KEY_PATH, True)
            Utils.create_dir(cons.PUBLIC_KEY_PATH, True)

            # if the config file does not exist then create it
            if not os.path.isfile(self.ini_file_path):
                # write it to the config.ini file
                with open(self.ini_file_path, 'w') as conf:
                    self.cp_obj.write(conf)

            Utils.information(
                "The ini file for configuration is created successfully at " + self.ini_file_path, True, True)

            # create the logger
            self.logger = Logger(config_file_path=self.ini_file_path)

            self.logger.info(
                "The ini file for configuration is created successfully")

            b_config = self.generate_ssh_key()
        except:
            error_message = str(sys.exc_info()[1])
            Utils.error_message(error_message, True)

            b_config = False

        return b_config

    def generate_ssh_key(self):
        """
        **Method:** generate_ssh_key

        This method generates the private and public key files.
        Please note that the private key file should not be shared with anyone and kept in a safe place.
        Update the private key file path in the bot_config.ini file so that it can be used to SFTP.

        To enable smooth SFTP, the public key must be shared with the SFTP server admin so that it can added to the server config.

        :return: boolean
        """

        b_generate = True

        try:

            key = paramiko.RSAKey.generate(2048)  # generate the ssh key pair

            # save it to a file
            Utils.information(
                "Generating the private key file required for SFTP.", True)
            private_key_path = Utils.full_path(cons.PRIVATE_KEY_PATH)
            key.write_private_key_file(private_key_path)
            Utils.information("The private key file generated at " +
                              os.path.abspath(private_key_path))

            # save the public key to a file
            Utils.information(
                "Generating the public key file required for SFTP.", True)
            public_key_path = Utils.full_path(cons.PUBLIC_KEY_PATH)
            with open(public_key_path, 'w') as f:
                f.write(f"{key.get_name()} {key.get_base64()}")
            Utils.information("The private key file generated at " +
                              os.path.abspath(public_key_path))

        except:
            error_message = str(sys.exc_info()[1])
            Utils.error_message(error_message, True)
            b_generate = False

        return b_generate
