from view.comands.Comand import Comand
from view.View import View


class GetNotesList(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription(self):
        return "Посмотреть заметки"

    def execute(self, console):
        console.getNotesList()

assert issubclass(GetNotesList, Comand)
assert isinstance(GetNotesList(), Comand)
