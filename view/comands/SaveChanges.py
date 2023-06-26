from view.comands.Comand import Comand
from view.View import View


class SaveChanges(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription(self):
        return "Сохранить изменения"

    def execute(self, console):
        console.saveChanges()

assert issubclass(SaveChanges, Comand)
assert isinstance(SaveChanges(), Comand)
