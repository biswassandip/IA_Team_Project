import pytest
from unittest import mock
from watchdog.events import FileSystemEvent
from src.common.file_handlers.file_event_handler import FileMoveEventHandler

cons_source_dir = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/source_dir/"
cons_ini_file = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/IA_BOT/bot.ini"
cons_destination_dir = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/destination_dir"

@pytest.fixture
def mock_config():
    # Create a mock configuration object
    config = mock.Mock()
    config.get.return_value = cons_ini_file
    return config

@pytest.fixture
def mock_event():
    # Create a mock FileSystemEvent object
    event = mock.Mock(spec=FileSystemEvent)
    event.is_directory = False
    event.src_path = cons_source_dir+'file.txt'
    return event

def test_filemoveeventhandler_init(mock_config):
    # Test the initialization of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    assert file_move_handler.config == mock_config
    assert file_move_handler.ini_file_path == cons_ini_file

def test_filemoveeventhandler_rules_exists(mock_config):
    # Test the _rules_exists method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)

    # Case when rules exist in the config
    mock_config.get.side_effect = lambda *args: 'criteria1' if args[1] == 'bot_rules' else None
    assert file_move_handler._rules_exists() == True

    # Case when rules do not exist in the config
    mock_config.get.side_effect = KeyError()
    assert file_move_handler._rules_exists() == False

def test_filemoveeventhandler_get_condition_map(mock_config):
    # Test the _get_condition_map method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)

    # Case when rules exist in the config
    mock_config.items.return_value = [
        ('criteria1', 'example, .txt, , , {cons_destination_dir}'),
        ('criteria2', 'example, .docx, , , {cons_destination_dir}')
    ]
    condition_map = file_move_handler._get_condition_map()
    assert condition_map == {
        'criteria1': ('example, .txt, , , {cons_destination_dir}'),
        'criteria2': ('example, .docx, , , {cons_destination_dir}')
    }

    # Case when no rules exist in the config
    mock_config.items.return_value = []
    condition_map = file_move_handler._get_condition_map()
    assert condition_map == {}

def test_filemoveeventhandler_on_created(mock_config, mock_event):
    # Test the on_created method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    file_move_handler.process_files = mock.Mock(return_value=True)

    file_move_handler.on_created(mock_event)

    assert file_move_handler.process_files.call_count == 1
    assert file_move_handler.process_files.call_args == mock.call( cons_source_dir+'file.txt')

def test_filemoveeventhandler_process_existing_files(mock_config):
    # Test the process_existing_files method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    file_move_handler.logger = mock.Mock()

    # Case when processing succeeds
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['file1.txt', 'file2.txt']
        file_move_handler.process_files = mock.Mock(return_value=True)
        result = file_move_handler.process_existing_files()
        assert result == True
        assert file_move_handler.process_files.call_count == 2
        assert file_move_handler.logger.error.call_count == 0

    # Case when an exception occurs during processing
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.side_effect = Exception('Error')
        file_move_handler.process_files = mock.Mock(return_value=True)
        result = file_move_handler.process_existing_files()
        assert result == False
        assert file_move_handler.process_files.call_count == 0
        assert file_move_handler.logger.error.call_count == 1
        assert str(file_move_handler.logger.error.call_args[0][0]) == 'Error'

def test_filemoveeventhandler_process_files(mock_config):
    # Test the process_files method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    file_move_handler.condition_map = {
        'criteria1': ('example, .txt, , , {cons_destination_dir}'),
        'criteria2': ('example, .docx, , , {cons_destination_dir}')
    }
    file_move_handler.logger = mock.Mock()
    file_move_handler.search_word_in_file = mock.Mock(return_value=True)
    file_move_handler.move_file_to_destination = mock.Mock()

    # Case when processing succeeds and matches criteria 1
    result = file_move_handler.process_files(cons_source_dir+'file.txt')
    assert result == True
    assert file_move_handler.search_word_in_file.call_count == 1
    assert file_move_handler.move_file_to_destination.call_count == 1
    assert file_move_handler.logger.warning.call_count == 0
    assert file_move_handler.logger.info.call_count == 1

    # Case when processing succeeds and matches criteria 2
    result = file_move_handler.process_files(cons_source_dir+'file.txt')
    assert result == True
    assert file_move_handler.search_word_in_file.call_count == 2
    assert file_move_handler.move_file_to_destination.call_count == 2
    assert file_move_handler.logger.warning.call_count == 1
    assert file_move_handler.logger.info.call_count == 2

    # Case when an exception occurs during processing
    file_move_handler.search_word_in_file.side_effect = Exception('Error')
    result = file_move_handler.process_files(cons_source_dir+'file.txt')
    assert result == False
    assert file_move_handler.search_word_in_file.call_count == 3
    assert file_move_handler.move_file_to_destination.call_count == 2
    assert file_move_handler.logger.warning.call_count == 2
    assert file_move_handler.logger.error.call_count == 1
    assert str(file_move_handler.logger.error.call_args[0][0]) == 'Error'

def test_filemoveeventhandler_search_word_in_file(mock_config):
    # Test the search_word_in_file method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    file_move_handler.common_file_types = ['.txt', '.docx']
    keyword_in_file = mock.Mock()
    keyword_in_file.search_keyword_in_files.return_value = True
    file_move_handler.KeywordInFile = mock.Mock(return_value=keyword_in_file)

    # Case when keyword search succeeds
    result = file_move_handler.search_word_in_file(cons_source_dir+'file.txt', 'example', ['.txt'])
    assert result == True
    assert file_move_handler.KeywordInFile.call_count == 1
    assert keyword_in_file.search_keyword_in_files.call_count == 1

    # Case when keyword search fails
    result = file_move_handler.search_word_in_file(cons_source_dir+'file.txt', 'example', ['.docx'])
    assert result == False
    assert file_move_handler.KeywordInFile.call_count == 2
    assert keyword_in_file.search_keyword_in_files.call_count == 2

def test_filemoveeventhandler_move_file_to_destination(mock_config):
    # Test the move_file_to_destination method of FileMoveEventHandler
    file_move_handler = FileMoveEventHandler(mock_config)
    file_move_handler.logger = mock.Mock()
    shutil = mock.Mock()
    shutil.move.return_value = None
    file_move_handler.Utils = mock.Mock()
    file_move_handler.Utils.get_file_name.return_value = 'file.txt'

    # Case when file move succeeds
    result = file_move_handler.move_file_to_destination(cons_source_dir+'file.txt', )
    assert result == True
    assert file_move_handler.Utils.create_dir.call_count == 1
    assert shutil.move.call_count == 1
    assert file_move_handler.logger.error.call_count == 0

    # Case when file move fails
    shutil.move.side_effect = Exception('Error')
    result = file_move_handler.move_file_to_destination(cons_source_dir+'file.txt', cons_destination_dir)
    assert result == False
    assert file_move_handler.Utils.create_dir.call_count == 2
    assert shutil.move.call_count == 2
    assert file_move_handler.logger.error.call_count == 1
    assert str(file_move_handler.logger.error.call_args[0][0]) == 'Error'
