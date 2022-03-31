from math import ceil, sqrt

from random import random, randint, choice

import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, i):
        if not i:
            return self.x
        else:
            if i > 1:
                raise IndexError()
            else:
                return self.y

    def __repr__(self):
        return f'Coordinate({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


class Polygon:
    """
    A Polygon definition that takes Coordinates as the argument
    """

    def __init__(self, *coords):
        """
        :param coords: type(coords) == Coordinate
        """
        self.iscoor_ = True if isinstance(coords[0], Coordinate) else False
        if isinstance(coords[0], Line):
            if len(coords) < 2:
                raise ValueError('Not a Polygon')

        if len(coords) < 3:
            raise ValueError('Not a Polygon')

        self.coordinates = coords
        self._area = self.area()
        self._perimeter = self.perimeter()

    def __repr__(self):
        coord = self.coordinates
        coord = str(coord)[1:-1]
        return f'Polygon({coord})'

    def area(self):
        coordinates = self.coordinates
        c1 = c2 = 0
        for i in range(1, len(coordinates)):
            xf, yf = coordinates[i - 1]
            xs, ys = coordinates[i]

            c1 += xf * ys
            c2 += yf * xs
        x1, y1 = coordinates[0]
        xn, yn = coordinates[-1]

        c1 += xn * y1
        c2 += yn * x1

        return 0.5 * abs(c1 - c2)

    def perimeter(self):
        coordinates = self.coordinates
        summ = Line(coordinates[0], coordinates[-1])
        if not self.iscoor_:
            return summ + sum(coordinates)
        coordinates = coordinates
        for i in range(1, len(coordinates)):
            summ = Line(coordinates[i - 1], coordinates[i]) + summ

        return summ

    def draw(self):
        coords = self.coordinates
        u_list = []
        for i in range(1, len(coords)):
            xp, yp = prevcoord = coords[i-1]
            xc, yc = curr_coord = coords[i]
            u_list.extend([(xp, xc), (yp, yc)])

        x1, y1 = firstcoord = coords[0]
        xl, yl = lastcoord = coords[-1]

        u_list.extend([(x1, xl), (y1, yl)])
        print(u_list)

        Draw(*u_list)

class Line:
    def __init__(self, c1, c2):
        if not isinstance(c1, Coordinate):
            self.__c1 = Coordinate(*c1)
        else:
            self.__c1 = c1
        if not isinstance(c2, Coordinate):
            self.__c2 = Coordinate(*c2)
        else:
            self.__c2 = c2

    def __add__(self, other):
        return len(self) + abs(other)

    def __len__(self):
        x1, y1 = self.__c1
        x2, y2 = self.__c2
        return ceil(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))

    def __abs__(self):
        return self.__len__()

    def __repr__(self):
        return f'Line({self.__c1.__repr__()}, {self.__c2.__repr__()})'

    def __str__(self):
        return f'Line({self.__c1}, {self.__c2})'

    def null(self):
        return Line((0, 0), (0, 0))


def g(a):
    assert type(a) == int, str(a) + ' is not an int!'
    if a < 1:
        return
    def g_n():
        return choice([1, -1]) * random() * choice([50, 100])
    ls = []
    for i in range(a):
        ls.append(Coordinate(g_n(), g_n()))

    if len(ls) == 1:
        return ls[0]
    if len(ls) == 2:
        return Line(*ls)

    return Polygon(*ls)

def Draw(*coords):
    assert len(coords) % 2 == 0

    plt.plot(*coords)
    plt.show()


if __name__ == "__main__":
    cases = [g(randint(1, 10)) for i in range(10)]

    for test in cases:
        print(test)
        print('\n-----------\n')


