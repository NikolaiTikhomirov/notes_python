from abc import ABC, abstractmethod


class Comand():

    def __init__():
        """Конструктор"""
        # self.View = View

    @abstractmethod
    def getDescription():
        """Описние команды"""

    @abstractmethod
    def execute():
        """Выполнить"""
