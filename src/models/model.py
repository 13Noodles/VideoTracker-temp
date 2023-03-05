import os # used the create directories if necessary when exportDir is changed
import random # used by Model.addRandomPoint()
import yaml

from models.fileRepo import FileRepo
from models.point import Point
from models.exportSettings import ExportSettings
from models.colorProfile import ColorProfile

class Model:
    def __init__(self, workingDir:str,configFilePath:str):
        
        self.__points = []
        self.__times = []
        self.__config = {}
        self.__colorProfiles = []
        self.__currentColorProfileId = None
        self.__workingDir = workingDir

        if(self.__loadConfigs(configFilePath) == -1):
            print("Model init error : couldn't read config file")
            exit(1)
        if(self.__loadColorProfiles(self.__config["profilesFilePath"]) == -1):
            print("Model init error : couldn't read color profiles file")
            exit(1)

        self.__exportSettings = ExportSettings(
            defaultExportDir=self.__config["exportDefaults"]["defaultDirectory"],
            defaultExportFilename=self.__config["exportDefaults"]["defaultFilename"],
            defaultAllowOverwriteOnSave=self.__config["exportDefaults"]["defaultAllowOverwrite"],
            defaultSortColumn=self.__config["exportDefaults"]["defaultSortColumn"]
        )
        self.__language = self.__config["defaultLang"]
        self.__posDecimalPrecision = self.__config["pointsConfig"]["decimalPrecision"] # round all points pos to 2 decimal
        self.__pointPosXrange = (self.__config["pointsConfig"]["xMin"],self.__config["pointsConfig"]["xMax"])
        self.__pointPosYrange = (self.__config["pointsConfig"]["yMin"],self.__config["pointsConfig"]["yMax"])
        self.__pointPosTrange = (self.__config["pointsConfig"]["tMin"],self.__config["pointsConfig"]["tMax"])


    ##############################
    #       INITIALIZERS         #
    ##############################
    def __loadConfigs(self,configFilePath) -> int:
        try:
            with open(self.__workingDir+"/"+configFilePath) as f:
                self.__config = yaml.load(f, Loader=yaml.FullLoader)
            return 0
        except Exception as e:
            return -1
    
    def __loadColorProfiles(self, profilesFilePath) -> int:
        """
        - loads the file at profilesFilePath then iterate through it to create 
        new ColorProfile objects and add them to Model.__colorProfiles
        - checks for the key "default" in each profile, if it exists and is set to
        true, the current profile of the Model will be set to this profile
            - if multiple profiles have the "defaut" key set to true, the last one will
            be used as current profile for the model
            - if no profile has the "default" key set to true, the last profile will be used
            as current profile for the model
        - return 
            - 0 if profile load successfull
            - 1 if couldn't read profilesFilePath & set the default profile
            - -1 for any other error
        """
        try:
            with open(self.__workingDir+"/"+profilesFilePath) as f:
                profilesFileData = yaml.load(f, Loader=yaml.FullLoader)
                for profileId,profile in enumerate(profilesFileData["profiles"]):
                    if("default" in profilesFileData["profiles"][profile] and profilesFileData["profiles"][profile]["default"] is True):
                        self.__currentColorProfileId = profileId
                    self.__colorProfiles.append(ColorProfile(profilesFileData["profiles"][profile]))
            return 0
        except FileNotFoundError:
            print(f"WARN Model.__loadColorProfiles : {self.__workingDir}/{profilesFilePath} couldn't be read, loaded default profile (as defined in ColorProfile)")
            self.__colorProfiles = [ColorProfile()]
            self.__currentColorProfileId = 0
            return 1
        except Exception as e:
            print(e)
            return -1


    ##############################
    #          GETTERS           #
    ##############################
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

    
    def getConfigPoints(self) -> dict:
        """returns a dict holding points' config"""
        return self.__config["pointsConfig"]


    ##############################
    #           OTHER            #
    ##############################
    def addPoint(self, x: float, y: float, t: int) -> tuple:
        """
        Add a point to the Model & return a tuple in the form (time,Point)
        - x,y and t values are clamped/rounded to fit in the range specified in the config
        """
        # Might want to remove the clamps later, #DEBUG
        x = round(x,self.__posDecimalPrecision)
        x = self.clamp(x,self.__pointPosXrange[0],self.__pointPosXrange[1])
        y = round(y,self.__posDecimalPrecision)
        y = self.clamp(y,self.__pointPosYrange[0],self.__pointPosYrange[1])
        t = self.clamp(t,self.__pointPosTrange[0],self.__pointPosTrange[1])
        self.__points.append(Point(x,y))
        self.__times.append(t)
        return (t,self.__points[-1])


    def addRandomPoint(self) -> tuple:
        """Add a random point to the Model & return a tuple in the form (time,Point)"""

        # Might want to remove the clamps & this function later, #DEBUG
        x = random.uniform(self.__pointPosXrange[0],self.__pointPosXrange[1])
        y = random.uniform(self.__pointPosYrange[0],self.__pointPosYrange[1])
        t = random.randint(self.__pointPosTrange[0],self.__pointPosTrange[1])
        x = round(x,self.__posDecimalPrecision)
        y = round(y,self.__posDecimalPrecision)
        # skip Model.addPoint call to avoid 4 checks 
        # (they're useless because this function already do those checks)
        self.__points.append(Point(x,y))
        self.__times.append(t)
        return (self.__points[-1],self.__times[-1])
    
    def setLanguage(self,language:str) -> int:
        """
        change Model's current language
        - return 0 if the language has been changed
        - return 1 if the language is already the one provided
        - return -1 if the language provided isn't found
        """
        if(self.__language == language):
            return 1
        elif(language in self.__config["languagesSupported"]):
            self.__language = language
            return 0
        #else:
        return -1

    def switchSeparator(self):
        if(self.__exportSettings.getSeparator() == ";"):
            self.__exportSettings.setSeparatorComma()
        else:
            self.__exportSettings.setSeparatorSemiColon()

    def clamp(self,value,valueMin,valueMax):
        return max(valueMin,min(valueMax,value))

    def switchColorMode(self) -> ColorProfile:
        """
        switch to the next color profile
        returns the new color profile
        """

        # add 1 to __currentColorProfileId, 
        # if it more than the numer of profiles, set it back to 0 
        self.__currentColorProfileId = (self.__currentColorProfileId+1)%len(self.__colorProfiles)
        return self.__colorProfiles[self.__currentColorProfileId]
    
    def getCurrentColorProfile(self) -> ColorProfile:
        return self.__colorProfiles[self.__currentColorProfileId]

    def getProfile(self,profileName:str) -> ColorProfile|None:
        """
        returns the first color profile with the name provided
        - <!> profiles might not have a name when they're 
        loaded (the name defaults to unspecified)
        """
        for profile in self.__colorProfiles:
            if(profile.name == profileName):
                return profile
        return None