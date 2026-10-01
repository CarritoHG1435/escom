import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

puntos = np.array([(1,-2),(1.5, 1), (2.4,4), (3.2,2), (4,-1), (4.5,3), (6,5), (6.7,2)])
px, py =  puntos[:, 0], puntos[:,1]

arr_h = []
for i in range(len(puntos) - 1):
    arr_h.append(puntos[i+1][0] - puntos[i][0])

mtx_A = np.zeros([len(puntos), len(puntos)])
mtx_A[0][0] = 1

l = len(puntos) - 1
mtx_A[l][l] = 1
vec_b = np.zeros(len(puntos))

for i in range(1,l):
    mtx_A[i][i] = 2 * (arr_h[i-1] + arr_h[i])
    mtx_A[i][i-1] = arr_h[i-1]
    mtx_A[i][i+1] = arr_h[i]
    vec_b[i] = ((3 / arr_h[i]) * (puntos[i+1][1] - puntos[i][1])) - ((3 / arr_h[i-1]) * (puntos[i][1] - puntos[i-1][1]))

arr_c = np.linalg.solve(mtx_A, vec_b)


arr_d = []
arr_b = []

for j in range(l):
    arr_d.append((arr_c[j+1] - arr_c[j]) / (3 * arr_h[j]))
    arr_b.append( ((puntos[j+1][1] - puntos[j][1]) / arr_h[j]) - ((arr_h[j] / 3) * (2 * arr_c[j] + arr_c[j + 1])))

for i in range(l):
    plt.scatter(puntos[i][0], puntos[i][1])
    x = np.linspace(puntos[i][0], puntos[i+1][0], 100)
    x0 = puntos[i][0]
    Si = puntos[i][1] + arr_b[i] * (x - x0) + arr_c[i] * (x - x0) ** 2 + arr_d[i] * (x - x0) ** 3
    plt.plot(x, Si)
plt.scatter(puntos[-1][0], puntos[-1][1])

plt.savefig('spline.png')
data = {
        "x" : px,
        "a" : py,
        "b" : [*arr_b, 'N/A'],
        "c" : arr_c,
        "d" : [*arr_d, 'N/A'],
        }
df = pd.DataFrame(data)
print(df)
