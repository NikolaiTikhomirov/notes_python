# from ..model.Model import Model
# from presenter.Presenter import Presenterer
from view.View import View
from view.MainMenu import MainMenu
import datetime

class Consoler(View):
    __INPUT_ERROR = "Введенные данные некорректны, попробуйте еще раз"
    __work = True

    def __init__(self): #, presenter):
        """Конструктор"""
        # self.model = Model()
        # self.presenter = presenter
        # self.view = View()
        
        self.mainMenu = MainMenu()


    def print(text):
        """"""

    def start(self):
        """Запуск приложения"""
        print("Доброго времени суток")
        while (self.__work):
            self.__printMenu()
            self.__execute()
        

    def setPresenter(self, presenter):
        """"""
        self.presenter = presenter

    def addNote(self):
        """Добавить заметку"""
        addNoteWork = True
        while(addNoteWork):
            id = self.presenter.getNotebookLength() + 1
            title = input("Введите заголовок заметки:\n")
            body = input("Введите тело заметки:\n")
            date = datetime.datetime.now()
            self.presenter.addNote(id, title, body, date)
            addNoteWork = False
        # print("будем добавлять заметку")

    def deleteNote(self):
        """Удалить заметку"""
        print("будем удалять заметку") 

    def editNote(self):
        """Редактировать заметку"""
        print("будем редактировать заметку") 

    def getNotesList(self):
        """Посмотреть заметки"""
        self.presenter.getNotesList()
        # print("будем показывать заметки")

    def saveChanges(self):
        """Сохранить изменения"""
        self.presenter.saveChanges()
        # print("будем сохранять заметки") 

    def finish(self):
        """Завершить приложение"""
        print("До скорых встреч")
        self.__work = False

    # Внутренние функции

    def __printMenu(self):
        print(MainMenu.print(self.mainMenu))
    
    def __execute(self):
        line = input()
        if (self.__checkTextForInt(line)):
            numCommand = int(line)
            if (self.__checkCommand(numCommand)):
                MainMenu.execute(self.mainMenu, numCommand, self)
            
    def __checkCommand(self, numCommand):
        if (0 < numCommand <= MainMenu.size(self.mainMenu)):
            return True
        else:
            self.__inputError()
            print("chekCommand error")
            return False

    def __checkTextForInt(self, text):
        # text.isdigit()
        if (text.isdigit()):
            return True
        else:
            self.__inputError()
            print("isdigit error")
            return False
        
    def __inputError(self):
        print(self.__INPUT_ERROR)
    
    
    

# assert issubclass(Consoler, View)
# assert isinstance(Consoler(), View)
# assert issubclass(Consoler, Presenterer)
# assert isinstance(Consoler(), Presenterer)
# assert issubclass(Consoler, MainMenu)
# assert isinstance(Consoler(), MainMenu)

if __name__ == "__main__":
    pass
