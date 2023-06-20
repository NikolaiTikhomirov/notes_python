from Comand import *
from ...view.View import *


class AddNote(Comand):
    

    def __init__(self):
        """Конструктор"""
        # self.view = View()

    def getDescription():
        return "Добавить заметку"

    def execute(self):
        View.addNote()

assert issubclass(AddNote, Comand)
assert isinstance(AddNote(), Comand)
