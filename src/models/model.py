import os # used the create directories if necessary when exportDir is changed
from models.fileRepo import FileRepo
from models.point import Point
from models.exportSettings import ExportSettings


class Model:
    def __init__(self, config):
        self.__config = config
        self.__points = []
        self.__times = []
        self.__exportSettings = ExportSettings(
            defaultExportDir=config["exportDefaults"]["defaultDirectory"],
            defaultExportFilename=config["exportDefaults"]["defaultFilename"],
            defaultAllowOverwriteOnSave=config["exportDefaults"]["defaultAllowOverwrite"],
            defaultSortColumn=config["exportDefaults"]["defaultSortColumn"]
        )
        self.__language = config["defaultLang"]
        self.__posDecimalPrecision = 2 # round all points pos to 2 decimal

    ###############
    #   GETTERS   #
    ###############
    
    def getPoint(self, pointId: int) -> Point|None:
        if(pointId<0 or pointId>len(self.__points)-1):
            return None
        return self.__points[pointId]

    def getPoints(self) -> list[Point]:
        return self.__points

    def getTime(self, timeId: int) -> int|None:
        if(timeId<0 or timeId>len(self.__temps)-1):
            return None
        return self.__times[timeId]
    
    def getTimes(self) -> list[int]:
        return self.__times
    
    def getPointCount(self) -> int:
        return len(self.__points)

    def getPosDecimalPrecision(self) -> int:
        return self.__posDecimalPrecision

    def getExportSettings(self) -> ExportSettings:
        return self.__exportSettings

    def getCurrenLanguage(self) -> str:
        return self.__language


    def getConfig(self) -> dict:
        """
        returns a dict holding all the configs

        <!> it's the default values, some might have been changed since the program has been started<!>
        """
        return self.__config

    def getConfigViewTexts(self) -> dict:
        """returns a dict holding all languages' view texts"""
        return self.__config["viewTexts"]


    def getConfigMessages(self) -> dict:
        """returns a dict holding all languages' messages"""
        return self.__config["messages"]


    def getCurrentViewTexts(self) -> dict:
        """returns a dict holding current language's view texts"""
        return self.__config["viewTexts"][self.__language]


    def getCurrentMessages(self) -> dict:
        """returns a dict holding current language's messages"""
        return self.__config["messages"][self.__language]
    
    def getCurrentExportHeaders(self) -> dict:
        """returns a dict holding current language's export headers"""
        return self.__config["exportHeaders"][self.__language]

    ###############
    #    OTHER    #
    ###############
    
    def addPoint(self, x: float, y: float, t: int) -> None:
        x = round(x,self.__posDecimalPrecision)
        y = round(y,self.__posDecimalPrecision)
        self.__points.append(Point(x,y))
        self.__times.append(t)

    
    def setLanguage(self,language:str) -> bool:
        if(language in self.__config["languagesSupported"]):
            self.__language = language
            return True
        #else:
        return False

    def switchSeparator(self):
        if(self.__exportSettings.getSeparator() == ";"):
            self.__exportSettings.setSeparatorComma()
        else:
            self.__exportSettings.setSeparatorSemiColon()