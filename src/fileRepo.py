import os
from point import Point

class FileRepo:
    def transformDataToCSV(self, points: list[Point], temps: list[int], savePath:str) -> int:
        try:
            # découpe savePath pour ne garder que le chemin des dossiers
            # et créer les dossiers necessaires si possible quand le chemin est invalide
            dirsPath = "/".join(savePath.split("/")[:-1])
            if not os.path.exists(dirsPath):
                os.makedirs(dirsPath)
            
            with open(savePath, "w") as saveFile:
                saveFile.write("temps;positionX;positionY\n");
                for dataId in range(len(points)):
                    saveFile.write(f"{temps[dataId]};{points[dataId].getX()};{points[dataId].getY()}\n")
            return 0
        except Exception as e:
            return -1

