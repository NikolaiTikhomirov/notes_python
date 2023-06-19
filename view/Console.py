from view import View

class Console(View):

    def print(text):
        """"""

    def start():
        """Запуск приложения"""

    def setPresenter(presenter):
        """"""

    def addNote():
        """Добавить заметку"""

    def deleteNote():
        """Удалить заметку"""

    def editNote():
        """Редактировать заметку"""

    def getNotesList():
        """Посмотреть заметки"""

    def saveChanges():
        """Сохранить изменения"""

    def finish():
        """Завершить приложение"""

assert issubclass(Console, View)
assert isinstance(Console(), View)
