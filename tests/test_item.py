"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)

def test_item_init(test_item):
    assert test_item.name == "Смартфон"

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200000

def test_apply_discount(test_item):
    Item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 5000

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[-1].name == 'Клавиатура'

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('11.789') == 11

def test_item_repr(test_item):
    assert repr(test_item) == "Item('Смартфон', 10000, 20)"

def test_item_str(test_item):
    assert str(test_item) == 'Смартфон'

def test_item_add(test_item):
    assert test_item + test_item == 40
