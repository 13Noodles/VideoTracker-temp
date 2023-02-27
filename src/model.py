from fileRepo import FileRepo
from point import Point

class Model:
    def __init__(self, defaultSaveDir:str="saves"):
        self.__points = []
        self.__temps = []
        self.__saveDir = defaultSaveDir
        self.fileRepo = FileRepo()

    def getPoint(self, pointId: int) -> Point:
        if(pointId<0 or pointId>len(self.__points)-1):
            return None
        return self.__points[pointId]

    def getTemps(self, tempsId: int) -> int:
        if(tempsId<0 or tempsId>len(self.__temps)-1):
            return None
        return self.__points[pointId]

    def exportToCSV(self, filename: str):
        savePath = self.__saveDir+"/"+filename
        self.fileRepo.transformDataToCSV(self.__points,self.__temps,savePath)

