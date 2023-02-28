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

    def addPoint(self, x: int, y: int, t: int) -> None:
        self.__points.append(Point(x,y))
        self.__temps.append(t)

    def exportToCSV(self, filename: str) -> int:
        savePath = self.__saveDir+"/"+filename
        saveState = self.fileRepo.transformDataToCSV(self.__points,self.__temps,savePath)
        if(saveState == -1):
            print(f"Data export failed (saveDir:{self.__saveDir}, filename:{filename})")
            return -1
        return 0
