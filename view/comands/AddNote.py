from view.comands.Comand import Comand
# from view.Console import Consoler


class AddNote(Comand):
    

    def __init__(self):
        """Конструктор"""
        # self.console = console

    def getDescription(self):
        return "Добавить заметку"

    def execute(self, console):
        console.addNote()

assert issubclass(AddNote, Comand)
assert isinstance(AddNote(), Comand)
