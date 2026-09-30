import pandas as pd
import cmath

def f(x):
    return 3 * x ** 5 - 7 * x ** 4 + 8 * x ** 3 - 30


def muller(p0, p1, p2):
    f0, f1, f2 = f(p0), f(p1), f(p2)

    h1 = p1 - p0
    h2 = p2 - p1
    delta1 = (f1 - f0) / h1
    delta2 = (f2 - f1) / h2

    a = (delta2 - delta1) / (h2 + h1)
    b = a * h2 + delta2
    c = f2

    print("Parabola:",a,b,c)
    print("Puntos", p0,p1,p2)

    discriminante = cmath.sqrt(b ** 2 - 4 * a * c)

    if abs(b + discriminante) > abs(b - discriminante):
        den = b + discriminante
    else:
        den = b - discriminante

    if abs(den) < 1e-15:
        return p2

    return p2 - (2 * c) / den

pi, pi1, pi2, aprox = [], [], [], []


p0 = 1
p1 = 2
p2 = 3
it = 5

for i in range(it):
    pi.append(p0)
    pi1.append(p1)
    pi2.append(p2)
    ap = muller(p0,p1,p2)
    aprox.append(ap)
    p0,p1,p2 = p1,p2, ap
data = {
    "pi": pi,
    "pi+1": pi1,
    "pi+2": pi2,
    "aprox": aprox,
}
df = pd.DataFrame(data)
print(df)
print('Aproximacion:', aprox[-1])
print(f(aprox[-1]))