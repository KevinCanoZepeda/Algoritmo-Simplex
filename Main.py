import sympy as sp
class Simplex:
    def __init__(self,A,x,b,z):
        self.A = A
        self.x = x
        self.b = b
        self.z = z
    def mostrar(self):
        p = ''
        for n in range(len(self.A)):
            for m in range(len(self.A[0])):
                if self.A[n][m] < 0:
                    p += f'-{self.A[n][m]}{self.x[m]} '
                if self.A[n][m] > 0 and m != 0:
                    p += f'+{self.A[n][m]}{self.x[m]} '
                if self.A[n][m] > 0 and m == 0:
                    p += f'{self.A[n][m]}{self.x[m]} '
                else:
                    pass
            p += '\n'
        print(p)
a = Simplex([[1,2],[2,2]],['x1','x2'],'','')
a.mostrar()