from view.commands import Command
from view import View


class Finish(Command):

    def getDescription():
        return "Завершить работу приложения"

    def execute():
        View.finish()

assert issubclass(Finish, Command)
assert isinstance(Finish(), Command)
