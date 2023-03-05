import tkinter as tk
import yaml
import os

from controllers.controller import Controller
from models.model import Model
from views.view import View
from models.colorProfile import ColorProfile

class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("VideoTracker - toasts")

        # create a view (UI)
        view = View(self)

        # create the model (DB)
        currentDir,_ = os.path.split(os.path.realpath(__file__))
        model = Model(currentDir,"config.yaml")

        # create a controller
        controller = Controller(model, view)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()

