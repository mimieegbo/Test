from numpy import linspace


def crossing_2_graphs():
    N = int(input('Enter the number of points on graph: '))
    x = linspace(-4, 4, N)
    f = x
    g = x ** 2
    epsilon = float(input('Enter the allowable difference: '))
    guess = abs(f - g)
    result = []
    for i in range(len(x)):
        if guess[i] < epsilon:
            result.append(x[i])

    if not result:
        print('f does not cross g')
    else:
        print('f crosses g at these values', result)


crossing_2_graphs()
