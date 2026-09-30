import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 1*x**2 - 8*x + 2

def der_f(x):
    return 3*x**2 + 2 * x - 8

x = np.linspace(-6,4,100)
y = f(x)

fig, ax = plt.subplots()

# Highlight the horizontal and vertical origin lines
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)

plt.plot(x,y)

x_0 = float(input("Escoge tu x_0"))
err = 1

m_0 = der_f(x_0)

x_i = [-2,-1,0,1,2]

plt.plot(x, (m_0 * (x-x_0)) + f(x_0))
plt.scatter(x_0, f(x_0))
plt.ylim(top=50, bottom=-40)
x_1=-(f(x_0) / m_0) + x_0
print(x_1)
plt.scatter(x_1, 0)

plt.show()