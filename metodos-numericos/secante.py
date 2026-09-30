import pandas as pd

def f(x):
    return x**4+2*x**2-x-3

def steff(p1,p2,p3):
    return p1 - ((p2 - p1)**2)/(p3 - 2 * p2 + p1)

def sec(p0,p1):
    return p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))

p0 = [1]
p1 = [3]
p2 = []


for i in range (4):
    p2.append(sec(p0[i], p1[i]))
    p0.append(steff(p0[i], p1[i], p2[i]))
    p1.append(sec(p2[i], p0[i+1]))

p2.append(sec(p0[-1], p1[-1]))

df = pd.DataFrame({
    "p0": p0,
    "p1": p1,
    "p2": p2
})
print(df)
print(p2[-1])