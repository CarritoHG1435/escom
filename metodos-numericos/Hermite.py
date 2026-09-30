import numpy as np
import matplotlib.pyplot as plt
import math
from frac_div import dif_div

f = lambda x:  x**2 * np.sin(x)

df = lambda x:  x**2 * np.cos(x) + 2*x*np.sin(x)

arr_xi = np.array([-2,-1,0,1,2,3])
arr_fxi = np.array([f(xi) for xi in arr_xi])
arr_dfxi = np.array([df(xi) for xi in arr_xi])

def dif_hermite(arr_xi, arr_fxi, arr_dfxi):
    coefs = []
    arr_xf = []
    arr_ff = []
    for i in range(len(arr_fxi) + len(arr_dfxi)): 
        index = math.floor(i/2)
        arr_xf.append(index)
        if i % 2 == 0:
            arr_ff.append(arr_fxi[index])
        else:
            arr_ff.append(arr_dfxi[index])

    arr_xf, arr_ff = np.array(arr_xf), np.array(arr_ff)
    coefs.append(arr_ff[0])

    arr_init = []
    count = 0
    for i in range(1,len(arr_xf)):
        den = arr_xf[i] - arr_xf[i-1]
        if den != 0:
            exp = (arr_ff[i] - arr_ff[i-1]) / (arr_xf[i] - arr_xf[i-1])
            arr_init.append(exp)
        else:
            arr_init.append(arr_dfxi[count])
            count+=1
    coefs.append(arr_init[0])

    print(len(arr_xf[1:]))
    print(len(arr_init))

dif_hermite(arr_xi, arr_fxi, arr_dfxi)
