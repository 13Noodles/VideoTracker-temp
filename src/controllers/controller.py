import random
from models.fileRepo import FileRepo

class Controller:
    def __init__(self, model, view):
        self.__view = view
        self.__model = model
        self.__fileRepo = FileRepo()
        self.__info_text = "No info"

        #Binding
        self.updateView()

        #callbacks
        self.__view.langEN_btn.config(command = self.setViewTextEnglish)
        self.__view.langFR_btn.config(command = self.setViewTextFrench)
        self.__view.export_btn.config(command = self.exportData)
        self.__view.separatorSwitch_btn.config(command = self.switchSeparator)
        # add model's default export filename as a placeholder
        self.__view.exportFilename_entry.insert(0,self.__model.getExportSettings().getExportFilename())

        self.setViewLang(self.__model.getConfig()["defaultLang"])
        

        self.updateView()

    def exportData(self) -> None:
        """Callback, Calls Model's exportToCSV & update view info_text (used for debugging) w/ export resultCode"""
        self.updateSaveFilename()
        saveState = self.__fileRepo.transformDataToCSV(
            points=self.__model.getPoints(),
            times=self.__model.getTimes(),
            exportSettings=self.__model.getExportSettings(),
            exportHeaders=self.__model.getCurrentExportHeaders()
        )
        if(saveState == 0):
            self.__info_text = self.__model.getCurrentMessages()['exportSuccess']+self.__model.getExportSettings().getExportPath()
        elif(saveState == -2):
            self.__info_text = self.__model.getCurrentMessages()['exportErrorOverwrite']
        elif(saveState == -1):
            self.__info_text = self.__model.getCurrentMessages()['exportErrorUnknown']
        self.updateView()

    def updateSaveFilename(self) -> None:
        """Sets export filename w/ view's entry text"""
        self.__model.getExportSettings().setExportFilename(self.__view.exportFilename_entry.get())

    def setViewTextFrench(self) -> None:
        """Callback"""
        self.setViewLang("fr")

    def setViewTextEnglish(self) -> None:
        """Callback"""
        self.setViewLang("en")

    def updateView(self) -> None:
        self.__view.update(self.__info_text)
        

    """
    updates the view w/ the target language texts
    if the language provided is invalid the view & the current language isn't changed
    """
    def setViewLang(self,language:str) -> None:
        if(self.__model.setLanguage(language)):
            config_texts = self.__model.getCurrentViewTexts()
            self.__view.addPoint_btn.config(command = self.addRandomPoint,text=config_texts["addPointButton"])
            self.__view.exportFilename_lbl.config(text = config_texts["exportLabel"])
            self.__view.export_btn.config(text = config_texts["exportButton"])
            self.__view.langFR_btn.config(text = config_texts["langFrenchButton"])
            self.__view.langEN_btn.config(text = config_texts["langEnglishButton"])
            self.__view.separatorSwitch_btn.config(text = config_texts["separatorSwitchButton"])

    ##### TEST THINGY #####
    def addRandomPoint(self) -> None:
        x = random.uniform(-10.0,10.0)
        y = random.uniform(-10.0,10.0)
        t = random.randint(0,100)
        self.__model.addPoint(x,y,t)
        x = round(x,self.__model.getPosDecimalPrecision())
        y = round(y,self.__model.getPosDecimalPrecision())
        self.__info_text = f"{self.__model.getCurrentMessages()['addPoint']}t={t}, x={x}, y={y}"
        self.updateView()

    def switchSeparator(self):
        self.__model.switchSeparator()
        self.__info_text = f"{self.__model.getCurrentMessages()['separatorSwitch']} '{self.__model.getExportSettings().getSeparator()}'"
        self.updateView()