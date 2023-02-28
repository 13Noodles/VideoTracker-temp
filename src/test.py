from point import Point
import random


def randomPoints(n: int) -> list[Point]:
    x_range = [-10.0,20.0]
    y_range = [-10.0,20.0]
    points = []
    for i in range(n):
        # uses random.uniform because Point's x & y properties are floats
        # random.randint would work too but using floats would be _pointless_ then :')
        newPoint = Point(random.uniform(x_range[0],x_range[1]),random.uniform(y_range[0],y_range[1]))
        points.append(newPoint)
    return points

