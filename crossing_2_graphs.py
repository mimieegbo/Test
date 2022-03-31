from numpy import linspace

def crossing_2_graphs():

    N = int(input('Enter the number of points on graph: '))
    x = linspace(-4, 4, N)
    f = x
    g = x**2
    epsilon = float(input('Enter the allowable difference: '))
    guess = abs(f -g)
    for i in range(len(x)):
        if guess[i] < epsilon:
            print(x[i], 'is a value where', f, 'crosses', g)
        if x[i] == x[-1]:
            break
    else:
        print(f, 'does not cross', g)

crossing_2_graphs()