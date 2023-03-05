import os

class ExportSettings:
    def __init__(self,
        defaultExportDir:str="saves",defaultExportFilename:str="data",defaultAllowOverwriteOnSave:bool=False,defaultSortColumn:int=0,defaultSeparator:str=";") -> None:
        self.setExportDir(defaultExportDir)
        self.setExportFilename(defaultExportFilename)
        self.__defaultExportFilename = defaultExportFilename
        self.__separator = defaultSeparator

        self.__isOverwriteAllowed = defaultAllowOverwriteOnSave
        self.__sortColumnId = defaultSortColumn

    def setExportFilename(self,filename: str) -> None:
        """
        change the export filename
        - if filename is empty or '', exportFilename is set to Model.defaultExportFilename
        - if filename contains any subdir ('/') only the part after the last '/' will be kept
        - if filename constains any extensions (after any '.'), only the part before the first '.' will be kept
        """
        if(filename == ""):
            self.__exportFilename = self.__defaultExportFilename
        else:
            # takes the part after the last "/" if there's one or more
            # (remove any subdirs that might be in the filename)
            filename = filename.split("/")[-1] 
            # takes the part before the first "." if there's one or more 
            # (removes any extensions that might be in the filename)
            filename = filename.split(".")[0] 
            self.__exportFilename = filename

    def setExportDir(self,dirPath:str) -> None:
        """<!> might fail if a file in dirPath with the same name as the correponding directory already exist"""
        # if dirPath doesn't exist, create the directory (or subDirs)
        if(not os.path.exists(dirPath)):
            os.makedirs(dirPath)

        self.__exportDir = dirPath


    def enableOverwriteOnExport(self) -> None:
        self.__isOverwriteAllowed = True

    def disableOverwriteOnExport(self) -> None:
        self.__isOverwriteAllowed = False 

    def getExportFilename(self) -> str:
        """returns the export filename (without extension)"""
        return self.__exportFilename

    def getExportDir(self) -> str:
        """returns the export directory"""
        return self.__exportDir

    def getExportPath(self) -> str:
        """returns the full export path (save directory & filename with extension)"""
        return self.__exportDir+"/"+self.__exportFilename+".csv"

    def getSortColumnId(self) -> int:
        return self.__sortColumnId

    def getSortColumnStr(self) -> str:
        if(self.__sortColumnId == 0):
            return "temps"
        elif(self.__sortColumnId == 1):
            return "positionX"
        elif(self.__sortColumnId == 2):
            return "positionY"
        else:
            return "None"

    def getSeparator(self) -> str:
        return self.__separator

    def isOverwriteAllowed(self) -> bool:
        return self.__isOverwriteAllowed

    def setSeparatorComma(self):
        self.__separator = ","

    def setSeparatorSemiColon(self):
        self.__separator = ";"