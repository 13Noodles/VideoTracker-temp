class Point:
    def __init__(self,x:float, y:float):
        self.__x = x
        self.__y = y

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y
