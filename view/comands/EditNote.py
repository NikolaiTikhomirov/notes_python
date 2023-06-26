from view.comands.Comand import Comand
from view.View import View


class EditNote(Comand):

    def __init__(self):
        """Конструктор"""
        # self.View = View

    def getDescription(self):
        return "Редактировать заметку"

    def execute(self, console):
        console.editNote()

assert issubclass(EditNote, Comand)
assert isinstance(EditNote(), Comand)
