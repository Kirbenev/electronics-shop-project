from src.item import Item


class MixinLang:
    """ Класс-Миксин для установки языка исполнения товара"""

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет язык исполнения товара
        """
        if self.__language == "EN":
            self.__language = "RU"

        else:
            self.__language = "EN"

        return self


class KeyBoard(Item, MixinLang):
    """Класс для представление клавиатуры. Содержит все атрибуты класса Item и
    дополнительно атрибут, содержащий информацию о раскладке клавиатуры"""

    def __init__(self, *args):
        super().__init__(*args)




