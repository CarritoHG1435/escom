def f(x):
    return x**4+2*x**2-x-3

def g(x):
    return (3 + x -2*(x**2))**0.25

def steff(p1,p2,p3):
    return p1 - ((p2 - p1)**2)/(p3 - 2 * p2 + p1)

s = [1.1]
n = 1
p = 0
try:
    while n < 30:
        if n % 3 == 0:
            s.append(steff(s[n-1], s[n-2], s[n-3]))
        else:
            s.append(g(s[n-1]))
        n+=1
except:
    print("Final")
    s.pop()
    s.pop()
    n-=2
    p = s[n-1]
print(s)
