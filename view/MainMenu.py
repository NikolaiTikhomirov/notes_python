# from setuptools import setup, find_packages
# setup(
#     name = 'Main',
#     packages = find_packages()
# )


# from View import *
from .comands.AddNote import *
from .comands.DeleteNote import *
from .comands.EditNote import *
from .comands.Finish import * 
from .comands.GetNotesList import *
from .comands.SaveChanges import *
from .comands.Comand import *

class MainMenu():
    __comandList = []
    
    # __view = View()


    def __init__(self):
        """Конструктор"""
        # self.View = View
        # __commandList = new ArrayList<>();
        
        self.__comandList.append(AddNote())
        self.__comandList.append(DeleteNote())
        self.__comandList.append(EditNote())
        self.__comandList.append(GetNotesList())
        self.__comandList.append(SaveChanges())
        self.__comandList.append(Finish())

    def print(self):
        comandListBuilder = []
        for i in range(len(self.__comandList)):
            comandListBuilder.append(i+1)
            comandListBuilder.append(". ")
            comandListBuilder.append(Comand.Comand.getDescription(self.__comandList[i]))
            comandListBuilder.append("\n")
        
        # commandListBuilder.deleteCharAt(commandListBuilder.length()-1)
        return print(comandListBuilder) # commandListBuilder.toString()
    

    def execute(self, numComand):
        self.__comandList.get(numComand - 1).execute()
    

    # def size():
    #     return __commandList.size()
