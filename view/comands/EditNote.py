from . import Comand
from view import View


class EditNote(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription():
        return "Редактировать заметку"

    def execute():
        View.View.editNote()

assert issubclass(EditNote, Comand)
assert isinstance(EditNote(), Comand)
