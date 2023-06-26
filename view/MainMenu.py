# from setuptools import setup, find_packages
# setup(
#     name = 'MainMenu',
#     packages = find_packages()
# )

# from .View import View
# from view import view
# from view import comands
from view.comands.AddNote import AddNote
from view.comands.DeleteNote import DeleteNote
from view.comands.EditNote import EditNote
from view.comands.Finish import Finish
from view.comands.GetNotesList import GetNotesList
from view.comands.SaveChanges import SaveChanges
# from view.comands.Comand import Comand

class MainMenu():
    __comandList = []

    def __init__(self): #, view):
        """Конструктор"""
        # __commandList = new ArrayList<>();
        # self.view = view
        # self.console = console
        
        self.__comandList.append(AddNote())
        self.__comandList.append(DeleteNote())
        self.__comandList.append(EditNote())
        self.__comandList.append(GetNotesList())
        self.__comandList.append(SaveChanges())
        self.__comandList.append(Finish())

    def print(self):
        comandListBuilder = ""
        # comandListBuilder = []
        for i in range(len(self.__comandList)):
            comandListBuilder += str(i+1)
            comandListBuilder += ". "
            comandListBuilder += self.__comandList[i].getDescription()
            comandListBuilder += "\n"
            # comandListBuilder.append(i+1)
            # comandListBuilder.append(". ")
            # comandListBuilder.append(self.__comandList[i].getDescription())
            # comandListBuilder.append("\n")
        
        # commandListBuilder.deleteCharAt(commandListBuilder.length()-1)
        return print(comandListBuilder) # commandListBuilder.toString()
    

    def execute(self, numComand, console):
        self.__comandList[numComand - 1].execute(console)
    
    def size(self):
        return len(self.__comandList)
    
# MainMenu.print()
if __name__ == "__main__":
    pass
