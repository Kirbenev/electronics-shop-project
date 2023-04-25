import pytest
from src.phone import Phone

@pytest.fixture
def test_phone():
    return Phone("Смартфон", 10000, 20, 2)

def test_phone_init(test_phone):
    assert test_phone.number_of_sim == 2
