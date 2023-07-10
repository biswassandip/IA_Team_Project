# --------------------------------------------------------------------
# file name: bot_setup.py
# description: this program is the starting point to deploying and
# creating the required files and configurations to setup the bot
# --------------------------------------------------------------------


# ====================================================================
# 1.1. create the ini file - bot_config.ini
# ====================================================================
from common.utils import Utils
from common.config import Config
import configparser
import common.fw_bot as fw_bot

dir_to_monitor = None
move_files_to = None
sftp_ip = None
sftp_port = None
sftp_path = None


def display_setup_menu():

    Utils.custom_print(
        f"=================================================", True)
    Utils.custom_print(f"BOT SETUP MENU")
    Utils.custom_print(f"=================================================")
    Utils.custom_print(f"1. Client BOT setup")
    Utils.custom_print(f"2. Server BOT setup")
    Utils.custom_print(f"3. Start process", True, True)
    Utils.custom_print(f"4. Stop process")
    Utils.custom_print(f"5. Quit", True, True)


def process_menu(option):

    match option:
        case 1:
            print(f"You selected option 1 for a CLIENT setup")
            print(f"")
            return client_setup()

        case 2:
            print(f"You selected option 2 for a SERVER setup")
            print(f"")
            return server_setup()

        case 3:
            print(f"You selected option 3 to START process")
            print(f"")
            return start_process()
        
        case 4:
            print(f"You selected option 4 to STOP process")
            print(f"")
            return stop_process()
        
        case 5:
            print(f"You selected option 5 to QUIT")
            print(f"")

        case _:
            print(f"The option selected is not correct")
            print(f"")


def client_setup():

    b_setup = True

    # accept the data
    source_dir = Utils.custom_input(
        "1.1. Provide the directory to be monitored and then press ENTER: ")
    sftp_ip = Utils.custom_input(
        "1.2. Provide the SFTP host IP/address and then press ENTER: ")
    sftp_port = Utils.custom_input(
        "1.3. Provide the SFTP port number and then press ENTER: ")
    sftp_path = Utils.custom_input(
        "1.4. Provide the SFTP remote path and then press ENTER: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(source_dir):
        Utils.error_message(
            prompt="The DIR path provided in 1.1. is not valid!")
        b_setup = False

    if not Utils.validate_ip_pattern(sftp_ip):
        Utils.error_message(
            prompt="The IP address provided in 1.3. is not valid!")
        b_setup = False

    if not Utils.validate_port_pattern(sftp_port):
        Utils.error_message(
            prompt="The Port Number provided in 1.4. is not valid!")
        b_setup = False

    if not Utils.validate_dir_pattern(sftp_path):
        Utils.error_message(
            prompt="The Remote Path provided in 1.5. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:
        config = Config(source_dir=source_dir, sftp_ip=sftp_ip,
                        sftp_port=sftp_port, sftp_path=sftp_path)

        b_setup = config.create_config()

    return b_setup

def server_setup():

    b_setup = True

    # accept the data
    source_dir = Utils.custom_input(
        "2.1. Provide the directory to be monitored and then press ENTER: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(source_dir):
        Utils.error_message(
            prompt="The DIR path provided in 2.1. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:
        config = Config(source_dir=source_dir,is_client_config=False)

        b_setup = config.create_config()

    return b_setup

def start_process():

    b_setup = True

    # accept the data
    config_file_path = Utils.custom_input(
        "3.1. Provide the bot.ini file path: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(config_file_path):
        Utils.error_message(
            prompt="The bot.ini path provided in 3.1. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:
        # read the existing config file
        config = configparser.ConfigParser()
        config.read(config_file_path)

        # update the value of the stop_flag option
        config.set('FLAGS', 'stop_flag', 'False')

        # Write the updated config file
        with open(config_file_path, 'w') as config_file:
            config.write(config_file)


        config_file = config_file_path
        config = configparser.ConfigParser()
        config.read(config_file)
        fw_bot.monitor_files(config)

    return b_setup

def stop_process():

    b_setup = True

    # accept the data
    config_file_path = Utils.custom_input(
        "4.1. Provide the bot.ini file path: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(config_file_path):
        Utils.error_message(
            prompt="The bot.ini path provided in 4.1. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:

        # read the existing config file
        config = configparser.ConfigParser()
        config.read(config_file_path)

        # update the value of the stop_flag option
        config.set('FLAGS', 'stop_flag', 'True')

        # Write the updated config file
        with open(config_file_path, 'w') as config_file:
            config.write(config_file)

    return b_setup

def run():
    while True:
        display_setup_menu()

        try:
            b_process = False
            option = int(Utils.custom_input(
                "Enter your options between 1-5: "))
            b_process = process_menu(option)

            if option == 5 or b_process:
                break
        except ValueError:
            print(f"")
            print(f"The entered option should be between 1-5!")
        except KeyboardInterrupt:
            print(f"")
            print(f"The program was exited by user!")
            break

run()
