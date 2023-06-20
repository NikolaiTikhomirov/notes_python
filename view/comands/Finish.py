from . import Comand
from view import View


class Finish(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Завершить работу приложения"

    def execute():
        View.View.finish()

assert issubclass(Finish, Comand)
assert isinstance(Finish(), Comand)
