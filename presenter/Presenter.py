# from model.Model import Modeler
# from view.View import View
# from view.Console import Consoler


class Presenterer:

    def __init__(self, console, model):
        """Конструктор"""
        # self.view = View()
        self.console = console
        self.model = model
        self.console.setPresenter(self)

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



if __name__ == "__main__":
    pass