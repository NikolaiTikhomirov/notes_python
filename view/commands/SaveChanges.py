from view.commands import Command
from view import View


class SaveChanges(Command):

    def getDescription():
        return "Посмотреть заметки"

    def execute():
        View.saveChanges()

assert issubclass(SaveChanges, Command)
assert isinstance(SaveChanges(), Command)