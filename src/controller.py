from view import View
from model import Model

class Controller:
    def __init__(self, model:Model, view:View):
        self.__model = model
        self.__view = view
