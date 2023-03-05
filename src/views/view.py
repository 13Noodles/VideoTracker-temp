from tkinter import *

class View(Frame):

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent
        self.info_lbl = Label(self.parent, width='20', height = '5', font = ('Arial', 25), bg='ivory')
        self.info_lbl.pack(side=TOP, padx=5, pady=5,fill='x')
        
        self.langFR_btn = Button(self.parent,text="langFR_btn init?")
        self.langFR_btn.pack(side=LEFT,padx=5,pady=5)
        self.langEN_btn = Button(self.parent,text="langEN_btn init?")
        self.langEN_btn.pack(side=LEFT,padx=5,pady=5)
        
        self.separatorSwitch_btn = Button(self.parent,text="switch_separator_btn init?")
        self.separatorSwitch_btn.pack(side=LEFT,padx=5,pady=5)

        self.addPoint_btn = Button(self.parent,text="addPoint_btn init?")
        self.addPoint_btn.pack(side=LEFT,padx=5,pady=5)

        self.export_btn = Button(self.parent, text="export_btn init?")
        self.export_btn.pack(side=RIGHT, padx=5, pady=5)

        self.exportFilename_entry = Entry(self.parent)
        self.exportFilename_entry.pack(side=RIGHT)

        self.exportFilename_lbl = Label(self.parent,text="export_lbl init?", height='1', font = ('Arial', 10))
        self.exportFilename_lbl.pack(side=RIGHT,padx=5,pady=5)

    def update(self, text : str) -> None:
        self.info_lbl.config(text = text)
