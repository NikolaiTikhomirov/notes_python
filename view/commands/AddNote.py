from view.commands import Command
from view import View


class AddNote(Command):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Добавить заметку"

    def execute():
        View.addNote()

assert issubclass(AddNote, Command)
assert isinstance(AddNote(), Command)
