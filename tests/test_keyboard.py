import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def test_keyboard():
    return KeyBoard("Dell", 5000, 20)

def test_keyboard_init(test_keyboard):
    assert test_keyboard.language == "EN"

def test_keyboard_change_lang(test_keyboard):
    test_keyboard.change_lang()
    assert test_keyboard.language == "RU"