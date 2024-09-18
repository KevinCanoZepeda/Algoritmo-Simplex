import sympy as sp
import numpy as np
class Simplex:
    def __init__(self,A,x,b,c):
        self.A = np.matrix(A)
        self.x = x
        self.b = b
        self.c = c
    def mostrar(self):
        p = ''
        x, y = self.A.shape
        for n in range(x):
            for m in range(y):
                if self.A[n,m] < 0:
                    p += f'-{self.A[n,m]}{self.x[m]} '
                if self.A[n,m] > 0 and m != 0:
                    p += f'+{self.A[n,m]}{self.x[m]} '
                if self.A[n,m] > 0 and m == 0:
                    p += f'{self.A[n,m]}{self.x[m]} '
                else:
                    pass
            p += '\n'
        p += str(c)
        print(p)

    def pivoteo(self,fila,columna):
        x, y = self.A.shape
        self.A[fila,:] /= self.A[fila,columna]
        for f in range(x):
            if f != fila:
                self.A[f,:] -= self.A[f,columna]*self.A[fila,:]

    def cocientes_minimos(self,columna):
        # la columna sera la dada por optimalidad
        lista = []
        for fila in range(columna):
            lista.append(self.A[fila,columna])
        cociente = max(lista)
        return lista.index(cociente)
            
    def optimalidad(self):
        posicion = None
        actual = 0
        for x in self.A[-1, :]:
            actual = x
            if x > 0:
                posicion = self.A.index(x)
                break
        return posicion, actual

a = [[1,2],[2,2]]
x = ['x1','x2']
c = [-1, 2]
a = Simplex(a,x,'',c)
a.mostrar()
print(a.optimalidad())