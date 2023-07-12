import src.bot_setup as bs
from src.common.file_handlers.file_event_handler import FileMoveEventHandler as fe
import src.common.general_handlers.constants as cons
import configparser
import pytest
from src.common.file_handlers.file_event_handler import KeywordInFile
from src.common.general_handlers.config import Config

pytestmark = pytest.mark.random_order(disabled=True)

con_ini_file_path = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/retest/IA_BOT/bot.ini"
con_source_dir = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/retest/IA_BOT/test-files/source"


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

# @pytest.fixture
# def file_searcher():
#     # Create a FileSearcher instance with a test configuration file
#     config_file = con_ini_file_path
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     return KeywordInFile()

# def test_search_keyword_in_txt(file_searcher):
#     assert file_searcher.search_keyword_in_text_file("/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/IA_BOT/test-files/source/sample.txt","sample")

# def test_search_files_with_keyword(file_searcher):
#     # Test searching for files containing the keyword
#     result = file_searcher.search_files_with_keyword()
#     files = result['files']
#     print(f"dddddd {len(files)}")
#     assert True

# def test_search_files_with_invalid_directory(file_searcher):
#     # Test searching with an invalid directory path
#     file_searcher.directory_or_file = con_source_dir
#     result = file_searcher.search_files_with_keyword()
#     files = result['files']
#     assert True

# def test_search_files_with_invalid_file(file_searcher):
#     # Test searching with an invalid file path
#     file_searcher.directory_or_file = con_source_dir
#     result = file_searcher.search_files_with_keyword()
#     files = result['files']
#     assert True

# def test_search_files_with_invalid_keyword(file_searcher):
#     # Test searching with an invalid keyword
#     file_searcher.keyword = 'invalid_keyword'
#     result = file_searcher.search_files_with_keyword()
#     files = result['files']
#     assert True

# def test_search_files_with_no_common_file_types(file_searcher):
#     # Test searching with no common file types
#     file_searcher.common_file_types = []
#     result = file_searcher.search_files_with_keyword()
#     files = result['files']
#     assert True

if __name__ == '__main__':
    # config_file = con_ini_file_path
    # config = configparser.ConfigParser()
    # config.read(config_file)
    # kw= KeywordInFile()
    # file_path = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/IA_BOT/test-files/source/sample.txt"
    # keyword = "sample"

    # common_file_types = [ext.strip() for ext in config[cons.INI_HEADER_SEARCH_IN_FILE_TYPES][cons.KEY_INCLUDE].split(',')]
    # print(f"{common_file_types}")

    # print(f"{kw.search_keyword_in_files(file_path,keyword,common_file_types)}")
    test_process_start()