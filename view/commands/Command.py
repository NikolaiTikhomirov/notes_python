from abc import ABC, abstractmethod


class Command():

    @abstractmethod
    def getDescription():
        """Описние команды"""

    @abstractmethod
    def execute():
        """Выполнить"""
