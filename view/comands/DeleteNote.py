from view.comands.Comand import Comand
# from view.Console import Consoler


class DeleteNote(Comand):

    def __init__(self):
        """Конструктор"""
        # self.console = Consoler()

    def getDescription(self):
        return "Удалить заметку"

    def execute(self, console):
        console.deleteNote()

assert issubclass(DeleteNote, Comand)
assert isinstance(DeleteNote(), Comand)
