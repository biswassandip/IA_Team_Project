import src.bot_setup as bs
import pytest

def test_process_start():
    assert bs.process(True, "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/IA_BOT/bot.ini",0)

def test_process_stop():
    assert bs.process(False, "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/IA_BOT/bot.ini")
    

if __name__ == '__main__':
    test_process_start()
