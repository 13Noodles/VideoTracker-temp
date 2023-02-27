from view import View
from model import Model
from controller import Controller

class Application():
    def __init__(self):
        view = View()
        model = Model()
        controller = Controller(model,view)

    def run(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.run()

