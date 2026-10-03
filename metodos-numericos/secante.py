import pandas as pd


def steff(p1,p2,p3):
    return p1 - ((p2 - p1)**2)/(p3 - 2 * p2 + p1)

def sec(p0,p1, f):
    return p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))


def secante(f, a, b, j):
    p0 = [a]
    p1 = [b]
    p2 = []


    for i in range (j):
        p2.append(sec(p0[i], p1[i], f))
        p0.append(steff(p0[i], p1[i], p2[i]))
        p1.append(sec(p2[i], p0[i+1], f))

    p2.append(sec(p0[-1], p1[-1], f))

    df = pd.DataFrame({
        "p0": p0,
        "p1": p1,
        "p2": p2
    })
    return (df, df['p2'][j])
