from shapes import Coordinate, Polygon


def polyarea(x, y):
    coordinates = []
    for i in range(len(x)):
        coordinates.append(Coordinate(x[i], y[i]))

    return Polygon(*coordinates).area()


print(polyarea([1, 2], [12, 10]))
