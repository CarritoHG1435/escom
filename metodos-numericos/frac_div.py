import numpy as np
import os
import matplotlib.pyplot as plt

f = lambda x : x * x * np.sin(x)
arr_x = np.array([- np.pi,  -(3/4) * np.pi, 0, (3/4) * np.pi, (3/2) * np.pi])
arr_f = np.array([f(xi) for xi in arr_x])

def dif_div(arr_x, arr_f, dif = 1):
    arr_coef = [arr_f[0]]
    arr_div = np.array(arr_f)
    arr_subdiv = []

    while len(arr_div) > 1:
        for i in range(len(arr_div) - 1):
            arr_subdiv.append((arr_div[i+1] - arr_div[i]) / (arr_x[i+dif] - arr_x[i]))
        arr_coef.append(arr_subdiv[0])
        arr_div = np.array(arr_subdiv)
        dif += 1
        arr_subdiv = []
    return arr_coef
if __name__ == '__main__':
    arr_coef = dif_div(arr_x, arr_f)
    print("Coeficientes:", arr_coef)

    x = np.linspace(-5, 5, 100)
    yOg = f(x)
    yPol = 0
    for i in range(len(arr_x)):
        prod = 1;
        for j in range(i):
            prod *= x - arr_x[j]
        yPol += arr_coef[i] * prod

    fig, ax = plt.subplots(figsize =(8,5))

    ax.plot(x, yOg, label='Funcion original')
    ax.plot(x, yPol, label='Polinomio interpolado')
    ax.scatter(arr_x, arr_f, color='black', zorder=5, label='Puntos evaluados')
    ax.legend()



    filename = 'polinomio-interpolado.png'

    fig.savefig(filename)
    os.system(f'explorer.exe {filename}')
