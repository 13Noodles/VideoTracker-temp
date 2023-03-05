import os
from models.point import Point
from models.exportSettings import ExportSettings

class FileRepo:
    def transformDataToArray(self, points:list[Point], times: list[int],sortColumn:int=-1) -> list[list]:
        """
        Create an array that holds the data from the points & time
        The tuple are (time,pointX,pointY)
        if sortColumn is valid (ie. 0<=sortColumn<=2) the tuples are sorted using
        the this column (in ascending order)
        """
        data = []
        for dataId in range(len(points)):
            data.append((times[dataId],points[dataId].getX(),points[dataId].getY()))
        # sortColumn < 3 because the column ids are in the range [0,2]
        if(0 <= sortColumn <= 2):
            self.bubbleSortTuples(data,sortColumn)
        return data

    def transformDataToCSV(self, points:list[Point], times:list[int], exportSettings:ExportSettings,exportHeaders:dict) -> int:
        """
        Calls transformDataToArray then Saves data to savePath in CSV format (format: time;pointX;pointY)
        returns 0 if save successful
        returns -2 if allowOverwrite=False & the file already exists
        returns -1 if any other errors is raised
        """
        try:
            # splits savePath to keep only the dirs & tries to create any subdir necessary
            # (if savePath was invalid)
            dirsPath = "/".join(exportSettings.getExportPath().split("/")[:-1])
            if not os.path.exists(dirsPath):
                os.makedirs(dirsPath)
            elif not exportSettings.isOverwriteAllowed() and os.path.exists(exportSettings.getExportPath()):
                return -2
            
            data = self.transformDataToArray(points,times,exportSettings.getSortColumnId())
            separator = exportSettings.getSeparator()
            with open(exportSettings.getExportPath(), "w") as saveFile:
                saveFile.write(f"{exportHeaders['time']}{separator}{exportHeaders['posX']}{separator}{exportHeaders['posY']}\n")
                for dataTuple in data:
                    saveFile.write(f"{dataTuple[0]}{separator}{dataTuple[1]}{separator}{dataTuple[2]}\n")
            return 0
        except Exception as e:
            print("fileRepo.transformDataToCSV (or child) error :"+str(e))
            return -1

    def bubbleSortTuples(self,arr:list[list],keyId:int) -> list[list]:
        """
        arr : list of list/tuples to sort
        keyId : id of the key used to sort
        
        <!> this function doesn't check data types, number w/ multiple digits
        represented  as strings might not be sorted correctly <!>
        
        merci l'UE info2 :x
        """
        arr_length = len(arr)
        swaps_done = -1
        while swaps_done != 0:
            swaps_done = 0
            for subArrId in range(0,arr_length-1):
                if arr[subArrId][keyId] > arr[subArrId+1][keyId]:
                    # swap
                    temp = arr[subArrId]
                    arr[subArrId] = arr[subArrId+1]
                    arr[subArrId+1] = temp
                    swaps_done += 1
        return arr
