from view.commands import Command
from view import View


class GetNotesList(Command):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Посмотреть заметки"

    def execute():
        View.getNotesList()

assert issubclass(GetNotesList, Command)
assert isinstance(GetNotesList(), Command)
