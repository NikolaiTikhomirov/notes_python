from . import Comand
from view import View


class SaveChanges(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Посмотреть заметки"

    def execute():
        View.View.saveChanges()

assert issubclass(SaveChanges, Comand)
assert isinstance(SaveChanges(), Comand)
