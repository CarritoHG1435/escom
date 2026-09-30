import numpy as np

class Polinomio:
    def __init__(self, grado):
        self.grado = grado
        self.coef = np.zeros(grado+1)

    def __str__(self):
        output = ""
        for i in range(self.grado + 1):
            if self.coef[i] != 0 and i > 0:
                sign = '+' if self.coef[i] > 0 else '-'
                output += str(f' {sign} {abs(self.coef[i])} * x ^ {i}')
            if self.coef[i] != 0 and i == 0:
                output += str(self.coef[i])
        return output if output != "" else "Polinomio vacio"

    def __add__(self, other): 
        r = Polinomio(max(self.grado, other.grado))
        for i in range(self.grado + 1):
            r.coef[i] += self.coef[i]

        for i in range(other.grado + 1): 
            r.coef[i] += other.coef[i]
        return r

    def __sub__(self, other):
        r = Polinomio(max(self.grado, other.grado))
        for i in range(self.grado + 1):
            r.coef[i] += self.coef[i]

        for i in range(other.grado+1):
            r.coef[i] -= other.coef[i]
        return r.opt()

    def opt(self):
        cof = self.coef
        index_max = self.grado
        for i in range(self.grado + 1):
            if i == 0:
                continue

            if cof[i] == 0 and index_max == self.grado:
                index_max = i - 1
            else:
                index_max = self.grado
        newPol = Polinomio(index_max)
        newPol.coefs(self.coef[:index_max + 1])
        return newPol

    def __mul__(self, other):
        if self.grado > other.grado:
            polMax, polMin = self, other
        else:
            polMax, polMin = other, self
        dim = polMax.grado + 1
        M = np.zeros([2 * dim - 1, dim])
        for i in range(dim):
            vec = np.full(dim, polMax.coef[dim - i - 1])
            np.fill_diagonal(M[i:, :], vec)
        arr_min = np.array([*polMin.coef[::-1], *np.zeros(dim - polMin.grado - 1)])
        resul = M @ arr_min
        resul = resul[:dim + polMin.grado]
        polResul = Polinomio(len(resul) - 1)
        polResul.coefs(resul[::-1])
        return polResul

    def coefs(self, coefs):
        self.coef = np.array(coefs)

    def div_sint(self):
        """
            Considerando la formula P(x) = (x - r) * Q(x) 
            Retornando en una lista [P(x), b0]
        """

        q = Polinomio(self.grado - 1)
        q.coef[q.grado] = self.coef[self.grado];

        for i in range(q.grado - 1, -1, -1,-1):



p = Polinomio(3)
print(p.coef)
p.coef[0] = 7
p.coef[1] = 4
p.coef[2] = 2
p.coef[3] = 1

q = Polinomio(3)
q.coefs([1,2,3, 1])
print('P1 ', p)
print('P2 ', q)
r =  p - q
print(r)
