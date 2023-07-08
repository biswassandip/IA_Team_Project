# --------------------------------------------------------------------
# file name: utils.py
# description: this class exposes static methods required for general
#              utility functions
# --------------------------------------------------------------------
from colorama import Fore, Style
import re
import os


class Utils:

    # ====================================================================
    # this static method print and to be used in private
    # 1 = INFO
    # 2 = INPUT
    # 3 = ERROR
    # 4 = GENERAL
    # ====================================================================
    @staticmethod
    def _print_it(prompt, msg_type=1, newline=False, plus_line=False):
        msg_color = None
        msg_prompt = prompt

        if msg_type == 1:
            msg_color = Fore.GREEN
        elif msg_type == 2:
            msg_color = Fore.BLUE
        elif msg_type == 3:
            msg_color = Fore.RED
            msg_prompt = "ERROR: " + msg_prompt
        elif msg_type == 4:
            msg_color = Fore.YELLOW
        else:
            msg_color = Fore.WHITE

        if newline:
            print(f"")

        if msg_type == 2:
            print(msg_color + f"{msg_prompt}" + Style.RESET_ALL, end='')
        else:
            print(msg_color + f"{msg_prompt}" + Style.RESET_ALL)

        if plus_line:
            print(f"")

    # ====================================================================
    # inputs
    # ====================================================================
    @staticmethod
    def custom_input(prompt):
        Utils._print_it(prompt=prompt, msg_type=2)
        user_input = input()  # take user input
        return user_input

    # ====================================================================
    # general messages
    # ====================================================================
    @staticmethod
    def custom_print(prompt, newline=False, plus_line=False):
        Utils._print_it(prompt=prompt, msg_type=4,
                        newline=newline, plus_line=plus_line)

    # ====================================================================
    # information messages
    # ====================================================================
    @staticmethod
    def information(prompt, newline=False, plus_line=False):
        Utils._print_it(prompt=prompt, msg_type=1,
                        newline=newline, plus_line=plus_line)

    # ====================================================================
    # error message print
    # ====================================================================
    @staticmethod
    def error_message(prompt, newline=False, plus_line=False):
        Utils._print_it(prompt=prompt, msg_type=3,
                        newline=newline, plus_line=plus_line)

    # ====================================================================
    # this static method will validate whether the directory is in correct format
    # ====================================================================
    @staticmethod
    def validate_dir_pattern(path):

        # the regex pattern to match a valid directory path
        pattern = r'/[a-zA-Z\./]*[\s]?'

        # check if the path matches the pattern
        if re.match(pattern, path):
            return True
        else:
            return False

    # ====================================================================
    # this static method will validate the ip address format
    # ====================================================================
    @staticmethod
    def validate_ip_pattern(ip):

        # the regex pattern to match an IP address
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

        # check if the IP address matches the pattern
        if re.match(pattern, ip):
            return True
        else:
            return False

    # ====================================================================
    # this static method will validate the port number format
    # ====================================================================
    @staticmethod
    def validate_port_pattern(port):

        # the regex pattern to match port number
        pattern = r'^[1-9]\d{0,4}$'

        # check if the port number matches the pattern
        if re.match(pattern, port):
            return True
        else:
            return False

    # ====================================================================
    # this static method will create the file path if it does not exist
    # ====================================================================
    @staticmethod
    def create_dir(file_path, is_file=False):
        if is_file:
            directory = os.path.dirname(file_path)
        else:
            directory = file_path

        if not os.path.exists(directory):
            os.makedirs(directory)

    # ====================================================================
    # this static method will get the full path
    # ====================================================================
    @staticmethod
    def full_path(file_path):
        return os.path.abspath(file_path)
