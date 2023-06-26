from view.comands.Comand import Comand
from view.View import View


class Finish(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription(self):
        return "Завершить работу приложения"

    def execute(self, console):
        console.finish()

assert issubclass(Finish, Comand)
assert isinstance(Finish(), Comand)
