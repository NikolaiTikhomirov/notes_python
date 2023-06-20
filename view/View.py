from abc import ABC, abstractmethod
import Presenter

class View():

    def __init__(self):
        """Конструктор"""
        # self.View = View

    @abstractmethod
    def print(text):
        """"""

    @abstractmethod
    def start():
        """Запуск приложения"""

    @abstractmethod
    def setPresenter(presenter):
        """"""

    @abstractmethod
    def addNote():
        """Добавить заметку"""

    @abstractmethod
    def deleteNote():
        """Удалить заметку"""

    @abstractmethod
    def editNote():
        """Редактировать заметку"""

    @abstractmethod
    def getNotesList():
        """Посмотреть заметки"""

    @abstractmethod
    def saveChanges():
        """Сохранить изменения"""

    @abstractmethod
    def finish():
        """Завершить приложение"""
