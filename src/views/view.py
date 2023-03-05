from tkinter import *
from models import colorProfile

class View(Frame):

    def __init__(self, parent):

        super().__init__(parent)
        self.__buttons = {}
        self.__labels = {}
        self.__entries = {}

        self.parent = parent
        self.__labels["profileInfo"] = Label(self.parent, width='20', height = '1', font = ('Arial', 25), bg='ivory')
        self.__labels["profileInfo"].pack(side=TOP, padx=5, pady=5,fill='x')
        
        self.__labels["info"] = Label(self.parent, width='20', height = '5', font = ('Arial', 25), bg='ivory')
        self.__labels["info"].pack(side=TOP, padx=5, pady=5,fill='x')
        
        self.__buttons["langFR"] = Button(self.parent,text="langFR_btn init?")
        self.__buttons["langFR"].pack(side=LEFT,padx=5,pady=5)
        self.__buttons["langEN"] = Button(self.parent,text="langEN_btn init?")
        self.__buttons["langEN"].pack(side=LEFT,padx=5,pady=5)

        self.__buttons["colorSwitch"] = Button(self.parent, text="colorSwitch_btn init?")
        self.__buttons["colorSwitch"].pack(side=RIGHT, padx=5, pady=5)

        self.__buttons["separatorSwitch"] = Button(self.parent,text="switch_separator_btn init?")
        self.__buttons["separatorSwitch"].pack(side=LEFT,padx=5,pady=5)

        self.__buttons["addPoint"] = Button(self.parent,text="addPoint_btn init?")
        self.__buttons["addPoint"].pack(side=LEFT,padx=5,pady=5)

        self.__buttons["export"] = Button(self.parent, text="export_btn init?")
        self.__buttons["export"].pack(side=RIGHT, padx=5, pady=5)

        self.__entries["exportFilename"] = Entry(self.parent)
        self.__entries["exportFilename"].pack(side=RIGHT)

        self.__labels["exportFilename"] = Label(self.parent,text="export_lbl init?", height='1', font = ('Arial', 10))
        self.__labels["exportFilename"].pack(side=RIGHT,padx=5,pady=5)

    ##############################
    #           SETTERS          #
    ##############################
    def set_button_callback(self,buttonKey:str,callback) -> int:
        if(buttonKey in self.__buttons and callable(callback)):
            self.__buttons[buttonKey].config(command = callback)
            return 0
        else:
            print(f"View.set_button_callback error : no button with the key {buttonKey}")
            return -1    

    def set_button_text(self,buttonKey:str,newText:str) -> int:
        if(buttonKey in self.__buttons):
            self.__buttons[buttonKey].config(text = newText)
            return 0
        else:
            print(f"View.set_button_text error : no button with the key {buttonKey}")
            return -1

    def set_label_text(self,labelKey:str,newText:str) -> int:
        if(labelKey in self.__labels):
            self.__labels[labelKey].config(text = newText)
            return 0
        else:
            print(f"View.set_label_text error : no label with the key {labelKey}")
            return -1

    def set_entry_text(self,entryKey:str, text:str) -> int:
        if(entryKey in self.__entries):
            # clears the entry text
            self.__entries[entryKey].delete(0,len(self.__entries[entryKey].get()))
            # insert the new text
            self.__entries[entryKey].insert(0,text)
            return 0
        else:
            print(f"View.set_entry_text error : no entry with the key {entryKey}")  
            return -1    

    def setColors(self,profile:colorProfile):
        self.parent.config(bg=profile.windowBackground())
        for button in self.__buttons.values():
            button.config(
                fg=profile.buttonText(),
                bg=profile.buttonBackground(),
                highlightbackground=profile.buttonBorder(),
                activebackground=profile.buttonBackgroundOver()
            )
        for label in self.__labels.values():
            label.config(
                fg=profile.labelText(),
                bg=profile.labelBackground(),
                highlightbackground=profile.labelBackground()
            )
        for entry in self.__entries.values():
            entry.config(
                fg=profile.entryText(),
                bg=profile.entryBackground(),
                highlightbackground=profile.entryBackground()
            )

    ##############################
    #           GETTERS          #
    ##############################
    def get_buttons(self) -> dict:
        return self.__buttons
    def get_labels(self) -> dict:
        return self.__labels
    def get_entries(self) -> dict:
        return self.__entries
    
    def get_entry_text(self,entryKey:str) -> str|None:
        if(entryKey in self.__entries):
            return self.__entries[entryKey].get()
        else:
            print(f"View.get_entry_text error : no entry with the key {entryKey}")  
            return None