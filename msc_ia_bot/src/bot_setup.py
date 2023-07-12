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

from common.general_handlers.utils import Utils
from common.general_handlers.config import Config
import configparser
import common.fw_bot as fw_bot
import sys

def display_setup_menu():
    """
    This method is responsible to display the menu options.
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
    This method is responsible to process the functionality behind the chosen option from the menu.

    Args:
        option (int): This is the option value between 1-4 chosen by the user.

    Returns:
        boolean
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
    This method will trigger the creation of the actual config ini file.

    Returns:
        boolean
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


def process(b_start, config_file_path, sleep_time=5, b_execute_once=False):

    """
    This is function processes based on chosen option 2 to start and 3 to stop.

    Args:
        b_start (boolean): True = to start and False = to stop.
        config_file_path (str): The file path for the cot config ini file.
        sleep_time (int): Default 5 seconds.
        b_execute_once (boolean): Default False.

    Returns:
        boolean
    """

    b_setup = False

    try:
        # read the existing config file
        config = configparser.ConfigParser()
        config.read(config_file_path)


        # update the value of the stop_flag option
        if b_start:
            config.set('FLAGS', 'stop_flag', 'False')
        else:
            config.set('FLAGS', 'stop_flag', 'True')

        # Write the updated config file
        with open(config_file_path, 'w') as config_file:
            config.write(config_file)
            
        config_file = config_file_path
        config = configparser.ConfigParser()
        config.read(config_file)

        # if the process has to be started then start the monitoring
        if b_start:
            b_setup=fw_bot.monitor_files(config,sleep_time,b_execute_once)
        else:
            b_setup=True
            
    except:
        error_message = str(sys.exc_info()[1])
        Utils.error_message(error_message, True)
        b_setup =  False

    return b_setup


def start_process():

    """
    This is function is to trigger processes to start it.

    Returns:
        boolean
    """

    b_setup = True

    # accept the data
    config_file_path = Utils.custom_input(
        "2.1. Provide the bot.ini file path: ")

    # validate the inputs
    if not Utils.validate_dir_pattern(config_file_path):
        Utils.error_message(
            prompt="The bot.ini path provided in 2.1. is not valid!")
        b_setup = False

    # now create the required config
    if b_setup:
        process(True,config_file_path)

    return b_setup


def stop_process():

    """
    This is function is to trigger processes to stop it.

    Returns:
        boolean
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

    # now stop the process
    if b_setup:
        process(False,config_file_path)

    return b_setup


def run():

    """
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


if __name__ == '__main__':
    run()