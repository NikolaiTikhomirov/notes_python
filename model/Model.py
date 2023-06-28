# from view.Console import Consoler
# from presenter.Presenter import Presenterer
from model.FileHandler import FileHandler

class Modeler:

    def __init__(self): #, consoler, presenterer'''):
        """Конструктор"""
        # self.view = consoler
        # self.presenter = presenterer
        filePath = "notes.csv"
        self.notebook = FileHandler.read(filePath)

    
    def addNote(self, id, title, body, date):
        """Добавить заметку"""
        note = [id, title, body, date]
        self.notebook.append(note)


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