# --------------------------------------------------------------------
# file name: logger.py
# description: this class is used for logging to log file
# --------------------------------------------------------------------

import logging
from logging.handlers import RotatingFileHandler
import common.constants as cons
import configparser


class Logger:

    # ====================================================================
    # initialize the config
    # ====================================================================
    def __init__(self, config_file_path) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
        self.init_logger()

    # ====================================================================
    # initialize the logger
    # ====================================================================
    def init_logger(self):
        self.logger = logging.getLogger(cons.LOGGING_ID)
        self.logger.setLevel(logging.INFO)

        self.log_file = self.config.get('GENERAL', 'log_file')

        handler = RotatingFileHandler(
            self.log_file, maxBytes=1024*1024, backupCount=5)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    # ====================================================================
    # log the info
    # ====================================================================
    def info(self, text):
        self.logger.info(f"{text}")

    # ====================================================================
    # log the warning
    # ====================================================================
    def warning(self, text):
        self.logger.warning(f"{text}")

    # ====================================================================
    # log the error
    # ====================================================================
    def error(self, text):
        self.logger.error(f"{text}")
