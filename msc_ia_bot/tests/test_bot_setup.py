"""
**Module:** test_bot_setup.py

This module contains the pytest test cases for the bot_setup.py module.
"""

import pytest
from src.bot_setup import bot_config_setup, process_menu, start_process, stop_process

@pytest.fixture
def mock_custom_input(monkeypatch):
    """
    Fixture to mock the custom_input method of Utils class.
    """
    def mock_input(prompt):
        if "directory to be monitored" in prompt:
            return "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/source_dir"
        elif "bot.ini file path" in prompt:
            return "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/IA_BOT/bot.ini"
        else:
            return "1"

    monkeypatch.setattr('bot_setup.Utils.custom_input', mock_input)

@pytest.fixture
def mock_validate_dir_pattern(monkeypatch):
    """
    Fixture to mock the validate_dir_pattern method of Utils class.
    """
    def mock_validate_dir(path):
        return True

    monkeypatch.setattr('bot_setup.Utils.validate_dir_pattern', mock_validate_dir)

def test_bot_config_setup(mock_custom_input, mock_validate_dir_pattern):
    """
    Test case to verify bot configuration setup.
    """
    assert bot_config_setup() == True

def test_process_menu():
    """
    Test case to verify process_menu function for different options.
    """
    assert process_menu(1) == True
    assert process_menu(2) == True
    assert process_menu(3) == True
    assert process_menu(4) == None

def test_start_process(mock_custom_input, mock_validate_dir_pattern):
    """
    Test case to verify starting the process.
    """
    assert start_process() == True

def test_stop_process(mock_custom_input, mock_validate_dir_pattern):
    """
    Test case to verify stopping the process.
    """
    assert stop_process() == True
