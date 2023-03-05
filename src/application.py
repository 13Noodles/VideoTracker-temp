import tkinter as tk
import yaml
import os

from controllers.controller import Controller
from models.model import Model
from views.view import View
print(yaml.__version__)
class Application(tk.Tk):

    def __init__(self,config):

        super().__init__()
        self.title(config["windowName"])

        # create a view (UI)
        view = View(self)

        # create the model (DB)
        model = Model(config)

        # create a controller
        controller = Controller(model, view)
        

if __name__ == '__main__':
    # load configs
    currentDir,filename = os.path.split(os.path.realpath(__file__))
    config = None
    with open(currentDir+"/config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    #print("config : "+str(config))

    app = Application(config)
    app.mainloop()

