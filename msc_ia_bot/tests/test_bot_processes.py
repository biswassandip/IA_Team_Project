import src.bot_setup as bs
from src.common.file_handlers.file_event_handler import FileMoveEventHandler as fe
import src.common.general_handlers.constants as cons
import configparser
import pytest
from src.common.file_handlers.file_event_handler import KeywordInFile
from src.common.general_handlers.config import Config

pytestmark = pytest.mark.random_order(disabled=True)

con_ini_file_path = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/IA_BOT/bot.ini"
con_source_dir = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/IA_BOT/source_dir"


def test_create_config():
    cf= Config(con_ini_file_path,con_source_dir)
    cf.create_config()


def test_process_start():
    """
    This test case is to test the process start
    """
    assert bs.process(True, con_ini_file_path, 0, True)


def test_process_stop():
    """
    This test case is to test the process stop
    """
    assert bs.process(False, con_ini_file_path)


def test_process_existing_files():
    """
    This test case is to test the files in the source directory and 
    verify it works as per the test ini file
    """

    config_file = con_ini_file_path
    config = configparser.ConfigParser()
    config.read(config_file)

    file_event = fe(config)
    assert file_event.process_existing_files()
