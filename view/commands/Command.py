from abc import ABC, abstractmethod


class Command():

    def __init__(self):
        """Конструктор"""
        # self.View = View

    @abstractmethod
    def getDescription():
        """Описние команды"""

    @abstractmethod
    def execute():
        """Выполнить"""
