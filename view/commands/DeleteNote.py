from view.commands import Command
from view import View


class DeleteNote(Command):

    def getDescription():
        return "Удалить заметку"

    def execute():
        View.deleteNote()

assert issubclass(DeleteNote, Command)
assert isinstance(DeleteNote(), Command)