"""
**Module:** bot_setup.py

This module is the start module that has the responsibilities to fulfill the setup of the bot.

It provides the user with a menu that has options to choose from:

    * Setup requirements to create an ini file that the bot will use.
    * Start the bot.
    * Stop the bot.
    * Quit the setup.

Based on the chosen options, this module will decide on creating the required ini file (**bot_config.ini**).
The **User** is expected to review the ini file and update it as required before rerunning the bot_setup.py 
to start the process.
"""

from common.utils import Utils
from common.config import Config
import configparser
import common.fw_bot as fw_bot
import subprocess
import sys

def display_setup_menu():
    """
    **Method:** display_setup_menu

    This method is responsible to display the menu options.

    :param: None
    :return: None
    :rtype: None
    """

    Utils.custom_print(f"=================================================", True)
    Utils.custom_print(f"BOT SETUP MENU")
    Utils.custom_print(f"=================================================")
    Utils.custom_print(f"1. BOT setup")
    
    Utils.custom_print(f"2. Start process", True, True)
    Utils.custom_print(f"3. Stop process")
    
    Utils.custom_print(f"4. Quit", True, True)
    Utils.custom_print(f"=================================================",None,True)


def process_menu(option):
    """
    **Method:** process_menu

    This method is responsible to process the functionality behind the chosen option from the menu.

    :param option: This is the expected option between 1 to 4.
    :type option: int 
    :return: Responses with a boolean (True or False) after the functionality for an option is executed
    :rtype: boolean
    """

    match option:
        case 1:
            print(f"You selected option 1 for a BOT setup")
            print(f"")
            return bot_config_setup()

        case 2:
            print(f"You selected option 2 to START process")
            print(f"")
            return start_process()
        
        case 3:
            print(f"You selected option 3 to STOP process")
            print(f"")
            return stop_process()
        
        case 4:
            print(f"You selected option 4 to QUIT")
            print(f"")

        case _:
            print(f"The option selected is not correct")
            print(f"")


def bot_config_setup():
    """
    **Method:** bot_config_setup

    This method will trigger the creation of the actual config ini file.

    :rtype: boolean
    """

    b_setup = True

    # accept the data
    source_dir = Utils.custom_input(
        "1.1. Provide the directory to be monitored and then press ENTER: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(source_dir):
        Utils.error_message(
            prompt="The DIR path provided in 1.1. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:
        config = Config(source_dir=source_dir)

        b_setup = config.create_config()

    return b_setup

def start_process():
    """
    **Method:** start_process

    This method will start the file monitoring process by updating the stop_flag to False in the ini file
    and triggering the fw_bot.monitor_files.

    :rtype: boolean
    """

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

        try:
            process = subprocess.Popen(['nohup', 'python', './common/monitor_files.py', '&'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

            print(f"testing....")
        except:
            error_message = str(sys.exc_info()[1])
            Utils.error_message(error_message, True)
            b_setup =  False

    return b_setup

def stop_process():
    """
    **Method:** stop_process

    This method will stop the file monitoring process by updating the stop_flag to True in the ini file.

    :rtype: boolean
    """

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
    """
    **Method:** run

    This method is the main method that will execute the bot setup process.

    """

    while True:
        display_setup_menu()

        try:
            b_process = False
            option = int(Utils.custom_input(
                "Enter your options between 1-4: "))
            b_process = process_menu(option)

            if option == 4 or b_process:
                break
        except ValueError:
            print(f"")
            print(f"The entered option should be between 1-4!")
        except KeyboardInterrupt:
            print(f"")
            print(f"The program was exited by user!")
            break

# run the process
run()
