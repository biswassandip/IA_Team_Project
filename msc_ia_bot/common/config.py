# --------------------------------------------------------------------
# file name: config.py
# description: this class is used for config related methods
# --------------------------------------------------------------------
from configparser import ConfigParser
from common.utils import Utils
import common.constants as cons
from common.logger import Logger

import os
import sys
import paramiko
import keyring
import os


class Config:

    # ====================================================================
    # initialize all the required values
    # ====================================================================
    def __init__(self,
                 ini_file_path=cons.INI_FILE_PATH,
                 source_dir=None,
                 is_client_config=True,
                 log_file=cons.LOG_FILE,
                 error_dir=cons.ERROR_DIR,
                 unmatched_dir=cons.UNMATCHED_DIR,
                 rotate_logs=cons.ROTATE_LOGS,
                 rotation_size=cons.ROTATION_SIZE,
                 num_processes=cons.MIN_PROCESSES,
                 scaling_factor=cons.SCALING_FACTOR,
                 min_processes=cons.MIN_PROCESSES,
                 sftp_ip=None,
                 sftp_port=None,
                 sftp_path=None,
                 ) -> None:

        self.ini_file_path = Utils.full_path(ini_file_path)
        self.source_dir = Utils.full_path(source_dir)
        self.is_client_config=is_client_config
        self.log_file = Utils.full_path(log_file)
        self.error_dir = Utils.full_path(error_dir)
        self.unmatched_dir = Utils.full_path(unmatched_dir)
        self.rotate_logs = rotate_logs
        self.rotation_size = rotation_size
        self.num_processes = num_processes
        self.scaling_factor = scaling_factor
        self.min_processes = min_processes
        self.sftp_ip = sftp_ip
        self.sftp_port = sftp_port
        self.sftp_path = sftp_path

        self.cp_obj = ConfigParser()  # config parser object


    # ====================================================================
    # creates the initial config required for the bot to work
    # ====================================================================
    def create_config(self):
        b_config = True

        try:

            # create the default config
            self.cp_obj["GENERAL"] = {
                "ini_file_Path": self.ini_file_path,
                "source_dir": self.source_dir,
                "log_file": self.log_file,
                "error_dir": self.error_dir,
                "unmatched_dir": self.unmatched_dir,
                "rotate_logs": self.rotate_logs,
                "rotation_size": self.rotation_size
            }

            # create the search config
            if self.is_client_config:
                self.cp_obj["CLIENT"] = {
                    "criteria1": "*.*"
                }

                # create the sftp config
                self.cp_obj["SFTP"] = {
                    "sftp_ip": self.sftp_ip,
                    "sftp_port": self.sftp_port,
                    "sftp_path": self.sftp_path,
                    "keystore_service_name": cons.KEYSTORE_SERVICE_NAME,
                    "keystore_pem_name": cons.KEYSTORE_PEM_NAME,
                    "private_key_path": Utils.full_path(cons.PRIVATE_KEY_PATH)
                }
            else:
                self.cp_obj["SERVER"] = {
                    "criteria1": "search_word1, , /path/to/destination_directory1",
                    "criteria2": ", file_type2, /path/to/destination_directory2",
                    "criteria3": "search_word3, file_type3, /path/to/destination_directory3",
                }

                # create the processes config
                self.cp_obj["PROCESSES"] = {
                    "num_processes": self.num_processes,
                    "num_processes_scaling_factor": self.scaling_factor,
                    "min_processes": self.min_processes
                }

            # create the flags config
            self.cp_obj["FLAGS"] = {
                "stop_flag": "False"
            }

            # create the required directories
            Utils.create_dir(self.log_file, True)
            Utils.create_dir(self.error_dir)
            Utils.create_dir(self.unmatched_dir)

            if self.is_client_config:
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

            if self.is_client_config:
                b_config = Config.generate_ssh_key()
        except:
            error_message = str(sys.exc_info()[1])
            Utils.error_message(error_message, True)

            b_config = False

        return b_config

    # ====================================================================
    # get the config file data
    # ====================================================================
    def read_config(self):
        return self.cp_obj.read(self.ini_file_path)

    # ====================================================================
    # store the pem file to keystore
    # ====================================================================
    def store_pem_to_keystore(service_name, private_key_name, private_key_path):
        keyring.set_password(service_name, private_key_name, private_key_path)

    # ====================================================================
    # get the pem file from the keystore
    # ====================================================================
    def get_pem_from_keystore(service_name, private_key_name):
        private_key_path = keyring.get_password(service_name, private_key_name)
        return private_key_path

    # ====================================================================
    # generate the private and public key file
    # ====================================================================
    def generate_ssh_key():

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

            # store it to keystore
            Config.store_pem_to_keystore(
                cons.KEYSTORE_SERVICE_NAME, cons.KEYSTORE_PEM_NAME, private_key_path)

            # delete the local private key pem file once stored in the keystore
            private_key_from_keystore = Config.get_pem_from_keystore(
                cons.KEYSTORE_SERVICE_NAME, cons.KEYSTORE_PEM_NAME)
            if private_key_from_keystore == private_key_path:
                Utils.information(
                    "Private key file stored in the keystore successfully", True)
            else:
                Utils.error_message(
                    "Could not store the private key file to keystore", True)
                b_generate = False
        except:
            error_message = str(sys.exc_info()[1])
            Utils.error_message(error_message, True)
            b_generate = False

    # ====================================================================
    # remove the local private key file after the keystore
    # ====================================================================
    def delete_local_private_file(file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied. Unable to delete the file.")
