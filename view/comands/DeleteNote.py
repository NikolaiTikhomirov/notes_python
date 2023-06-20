from . import Comand
from view import View


class DeleteNote(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Удалить заметку"

    def execute():
        View.View.deleteNote()

assert issubclass(DeleteNote, Comand)
assert isinstance(DeleteNote(), Comand)
