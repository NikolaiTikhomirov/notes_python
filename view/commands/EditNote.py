from view.commands import Command
from view import View


class EditNote(Command):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Редактировать заметку"

    def execute():
        View.editNote()

assert issubclass(EditNote, Command)
assert isinstance(EditNote(), Command)
