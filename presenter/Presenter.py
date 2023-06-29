# from model.Model import Modeler
# from view.View import View
# from view.Console import Consoler
# from model.Notebook import Notebook


class Presenterer:

    def __init__(self, console, model):
        """Конструктор"""
        # self.view = View()
        self.console = console
        self.model = model
        self.console.setPresenter(self)

    def addNote(self, id, title, body, date):
        """Добавить заметку"""
        self.model.addNote(id, title, body, date)

    def deleteNote():
        """Удалить заметку"""

    def editNote():
        """Редактировать заметку"""

    def getNotesList(self):
        """Посмотреть заметки"""
        print(self.model.getNotesList())

    def saveChanges(self):
        """Сохранить изменения"""
        self.model.saveChanges()

    def getNotebookLength(self):
        return self.model.getNotebookLength()



if __name__ == "__main__":
    pass