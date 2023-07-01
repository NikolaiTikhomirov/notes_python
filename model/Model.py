# from view.Console import Consoler
# from presenter.Presenter import Presenterer
from model.FileHandler import FileHandler
from model.Notebook import Notebook
from model.Note import Note

class Modeler:

    def __init__(self): #, consoler, presenterer'''):
        """Конструктор"""
        # self.view = consoler
        # self.presenter = presenterer
        self.filePath = "notes.csv"
        self.notebook = FileHandler.read(self.filePath)

    
    def addNote(self, id, title, body, date):
        """Добавить заметку"""
        note = [id, title, body, date]
        # print(type(self.notebook))
        self.notebook.addNoteToBook(note)


    def deleteNote():
        """Удалить заметку"""

    def editNote():
        """Редактировать заметку"""

    def getNotesList(self):
        """Посмотреть заметки"""
        print(Notebook.toString(self.notebook))

    def saveChanges(self):
        """Сохранить изменения"""
        FileHandler.save(self.filePath, self.notebook)

    def getNotebookLength(self):
        """Возвращает колличество заметок в записной книжке"""
        res = 0
        try:
            res = len(self.notebook)
        except:
            pass
        return res
    

if __name__ == "__main__":
    pass