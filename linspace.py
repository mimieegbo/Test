from numpy import linspace
L_values = linspace(1, 3, 3)
for elem in L_values:
    V = L_values**3
print(V)

import matplotlib.pyplot as pt
pt.plot(L_values, V)
pt.xlabel('Length')
pt.ylabel('Volume')


