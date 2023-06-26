# from setuptools import setup, find_packages
# setup(
#     name = 'MainMenu',
#     packages = find_packages()
# )
# from view.MainMenu import *

# import console
# from .model.Model import Model
# from .view.View import View
# from .view.Console import Console

# import view

# m = MainMenu()
# m.print()
from view.Console import Consoler
from model.Model import Modeler
from presenter.Presenter import Presenterer

class Main:

    def __init__():
        """Конструктор"""
        # self.view = View()
        

mod = Modeler()
cons = Consoler()
pres = Presenterer(cons, mod)
cons.start()


if __name__ == "__main__":

    pass