import numpy as np

def f(x):
    return x**2 * np.sin(x)

x = [1,1.2,1.4,1.6]
y = []
xVal = 1.3
for i in x:
    y.append((f(i)))

matrixNev = []
for i in range(len(x)):
    matrixNev.append(np.zeros(len(x)))
matrixNev = np.array(matrixNev)
for i in range(len(x)):
    matrixNev[i][0] = y[i]

for j in range(1, len(x)):
    for i in range(j, len(x)):
        matrixNev[i][j] = ((xVal - x[i - j]) * matrixNev[i][j - 1] - (xVal - x[i]) * matrixNev[i - 1][j - 1]) / (x[i] - x[i - j])

print(matrixNev)