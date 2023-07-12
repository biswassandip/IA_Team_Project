# --------------------------------------------------------------------
# file name: logger.py
# description: this class is used for logging to log file
# --------------------------------------------------------------------

import logging
from logging.handlers import RotatingFileHandler
import common.general_handlers.constants as cons
import configparser

"""
**class: Logger*

This class is responsible to log into files when invoked by the program to be logged with proper formats.
The log also makes sure that it is rotated and the rotation values are given in the bot config ini file.
"""


class Logger:


    def __init__(self, config_file_path) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
        self.init_logger()


    def init_logger(self):

        """
        Initializes the actual logging rotation and formatting values
        """

        self.logger = logging.getLogger(cons.LOGGING_ID)
        self.logger.setLevel(logging.INFO)

        self.log_file = self.config.get(cons.INI_HEADER_GENERAL, cons.KEY_LOG_FILE)

        handler = RotatingFileHandler(
            self.log_file, maxBytes=1024*1024, backupCount=5)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


    def info(self, text):

        """
        Logs information descriptions

        Args:
            text (str): The description
        """

        self.logger.info(f"{text}")


    def warning(self, text):

        """
        Logs warning descriptions

        Args:
            text (str): The description
        """
        
        self.logger.warning(f"{text}")


    def error(self, text):

        """
        Logs error descriptions

        Args:
            text (str): The description
        """
        
        self.logger.error(f"{text}")
