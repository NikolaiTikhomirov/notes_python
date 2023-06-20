from . import Comand
from view import View


class GetNotesList(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Посмотреть заметки"

    def execute():
        View.View.getNotesList()

assert issubclass(GetNotesList, Comand)
assert isinstance(GetNotesList(), Comand)
