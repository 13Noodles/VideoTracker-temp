import os
import random
from point import Point
from model import Model


def randomPoints(n: int) -> list:
    x_range = [-10.0,20.0]
    y_range = [-10.0,20.0]
    points = []
    for i in range(n):
        # uses random.uniform because Point's x & y properties are floats
        # random.randint would work too but using floats for the points properties
        # would be _pointLess_ then :')
        newPoint = Point(random.uniform(x_range[0], x_range[1]), random.uniform(y_range[0], y_range[1]))
        points.append(newPoint)
    return points

"""
Test to verify that Model.addPoint works and that we can get them back with Model.getPoint & Model.getTime
"""

def test_pointAndTime():
    print("running test_PointAndTime")

    x = [123.456,654.456]
    y = [-123,321]
    t = [1,3]
    model = Model()
    model.addPoint(x[0],y[0],t[0])
    model.addPoint(x[1],y[1],t[1])
    # checks that the points ids are the same as the order in which they've been added
    # and their properties values
    assert model.getPoint(pointId=0).getX() == x[0]
    assert model.getPoint(pointId=0).getY() == y[0]
    assert model.getTemps(tempsId=0) == t[0]
    assert model.getPoint(pointId=1).getX() == x[1]
    assert model.getPoint(pointId=1).getY() == y[1]
    assert model.getTemps(tempsId=1) == t[1]
    assert model.getPointCount() == 2
    print("-> Test OK")

"""
Test to verify that FileRepo.transformDataToCSV(..) works when it gets a valid path
"""
def test_saveExistingDir():
    print("running test_saveExistingDir")
    if not os.path.exists("testData"):
        os.mkdir("testData")
    # instantiate a model, add some points, then try to save
    model = Model(defaultSaveDir="testData")
    for p in randomPoints(10):
        model.addPoint(p.getX(), p.getY(), t=random.randint(0, 50))
    testResult = model.exportToCSV("testSaveExistingDir.csv")
    assert testResult == 0
    print("-> Test OK")

"""
Test to verify that FileRepo.transformDataToCSV(..) tries to create the necessary directories if it's given an invalid path (if there's a file in the path with the same name as one of the dirs it'll still fail tho)
"""
def test_saveNewDir():
    print("running test_saveNewDir")
    # create a subdir in testData to avoid affecting the other tests
    if os.path.isfile("testData/saveNewDir/testSaveNewDir.csv"):
        os.remove("testData/saveNewDir/testSaveNewDir.csv")
    if os.path.isdir("testData/saveNewDir"):
        os.rmdir("testData/saveNewDir")

    # instantiate a model, add some points, then try to save
    model = Model(defaultSaveDir="testData/saveNewDir")
    for p in randomPoints(10):
        model.addPoint(p.getX(), p.getY(), t=random.randint(0, 50))
    testResult = model.exportToCSV("testSaveNewDir.csv")
    assert testResult == 0
    print("-> Test OK")



def run_tests(testSeed: int):
    random.seed(testSeed)
    print("Test seed : "+str(testSeed))
    test_pointAndTime()
    test_saveExistingDir()
    test_saveNewDir()
    print("No assertion error, all the tests are ok I guess.")



run_tests(testSeed=0)

