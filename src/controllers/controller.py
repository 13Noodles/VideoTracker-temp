import random
from models.fileRepo import FileRepo

class Controller:
    def __init__(self, model, view):
        self.__view = view
        self.__model = model
        self.__fileRepo = FileRepo()
        self.__info_text = "No info"

        #callbacks
        self.__view.set_button_callback("langFR",self.setViewTextFrench)
        self.__view.set_button_callback("langEN",self.setViewTextEnglish)
        self.__view.set_button_callback("colorSwitch",self.switchColorMode)
        self.__view.set_button_callback("export",self.exportData)
        self.__view.set_button_callback("separatorSwitch",self.switchSeparator)
        self.__view.set_button_callback("addPoint",self.addRandomPoint)

        # add model's default export filename as a placeholder
        self.__view.set_entry_text("exportFilename",self.__model.getExportSettings().getExportFilename())

        self.setViewLang(self.__model.getConfig()["defaultLang"])
        self.updateViewColors()       

        self.updateView()

    def exportData(self) -> None:
        """Callback, Call Model's exportToCSV"""
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
        else:
            self.__info_text = self.__model.getCurrentMessages()['exportErrorUnknown']
        self.updateView()

    def updateSaveFilename(self) -> None:
        """Sets export filename w/ View's exportFilename entry text"""
        # give the entry for the filename of Model's exportSettings
        entryText = self.__view.get_entry_text("exportFilename")
        self.__model.getExportSettings().setExportFilename(entryText)
        # update the entry text w/ Model's exportSettings filename because it may have
        # removed some parts from the string it's been given
        self.__view.set_entry_text("exportFilename",self.__model.getExportSettings().getExportFilename())


    def setViewTextFrench(self) -> None:
        """Callback"""
        self.setViewLang("fr")

    def setViewTextEnglish(self) -> None:
        """Callback"""
        self.setViewLang("en")

    def updateView(self) -> None:
        """update View's texts with Model's messages & current language"""

        self.__view.set_label_text("info",self.__info_text) # used for debugging

        config_texts = self.__model.getCurrentViewTexts()
        self.__view.set_label_text("exportFilename",config_texts["exportLabel"])
        self.__view.set_label_text("profileInfo",f"{config_texts['colorProfile']}{self.__model.getCurrentColorProfile().name()}")
        self.__view.set_button_text("addPoint",config_texts["addPointButton"])
        self.__view.set_button_text("export",config_texts["exportButton"])
        self.__view.set_button_text("colorSwitch",config_texts["colorSwitch"])
        self.__view.set_button_text("langFR",config_texts["langFrenchButton"])
        self.__view.set_button_text("langEN",config_texts["langEnglishButton"])
        self.__view.set_button_text("separatorSwitch",config_texts["separatorSwitchButton"])

    def setViewLang(self,language:str) -> None:
        """
        Change the current language (stored in the Model) & update View's texts
        - if the language provided is invalid the view & the current language isn't changed
        """
        if(self.__model.setLanguage(language) == 0):
            self.__info_text = f"{self.__model.getCurrentMessages()['languageChanged']} {self.__model.getCurrenLanguage()}"
            self.updateView()

    ##### TEST THINGY #####
    def addRandomPoint(self) -> None:
        pointAdded,timeAdded = self.__model.addRandomPoint()
        self.__info_text = f"{self.__model.getCurrentMessages()['addPoint']}t={timeAdded}, x={pointAdded.getX()}, y={pointAdded.getY()}"
        self.updateView()

    def switchSeparator(self):
        self.__model.switchSeparator()
        self.__info_text = f"{self.__model.getCurrentMessages()['separatorSwitch']} '{self.__model.getExportSettings().getSeparator()}'"
        self.updateView()

    def switchColorMode(self):
        self.__model.switchColorMode()
        self.updateViewColors()
        self.updateView()

    def updateViewColors(self):
        colorProfile = self.__model.getCurrentColorProfile()
        self.__view.setColors(colorProfile)
