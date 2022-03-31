

def polyarea(x, y):
    c1 = c2 = 0
    for i in range(len(x)-1):
        c1 += x[i]*y[i+1]
        c2 += y[i]*x[i+1]

    c1 += x[-1]*y[0]
    c2 += y[-1]*x[0]

    return 0.5*(abs(c1-c2))

print(polyarea([1, 2], [12, 10]))
