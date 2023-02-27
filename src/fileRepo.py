from point import Point

class FileRepo:
    def transformDataToCSV(points: list[Point], temps: list[int], savePath:str):
        try:
            with open(savePath, "w") as saveFile:
                saveFile.write("temps;positionX;positionY\n");
                for dataId in range(len(points)):
                    saveFile.write(f"{temps[dataId]};{points[dataId].getX()};{points[dataId].getY()}\n")
        except Exception as e:
            print("transformDataToCSV error : "+str(e))

