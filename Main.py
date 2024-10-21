class Simplex:
    def __init__(self,A,b,c,tipo = 'Max'):
        self.A = A
        self.b = b
        self.c = c
        self.modelo = None
        self.tipo = tipo
    def construir(self):
        # cosntruimos una matriz de ceros
        self.modelo = [ [0 for i in range(len(self.A[0])+1)] for i in range(len(self.b) + 1)]
        # construccion de la A principal
        for i in range(len(self.A)):# filas
            for j in range(len(self.A[0])): # columnas
                self.modelo[i][j] = self.A[i][j]
        # construccion de la fila de c
        for j in range(len(self.A[0])):
            self.modelo[-1][j] = self.c[j]
        # cosntruccion de la columna b
        for i in range(len(self.A)):
            self.modelo[i][-1] = self.b[i]
        self.mostrar()
    def mostrar(self):
        for x in range(len(self.b)+1):
            print(self.modelo[x])
    def encontrar_pivote(self):
        pass
    def pivotear(self):
    # Volvemos 1 la fila del pivote
        if self.encontrar_pivote() != False:
            i, j = self.encontrar_pivote()  # Encontrar el índice del pivote

            # Dividimos toda la fila del pivote para que el elemento pivote sea 1
            for y in range(len(self.modelo[0])):
                self.modelo[i][y] /= self.modelo[i][j]

            # Hacemos 0 en todas las demás filas de la columna del pivote
            for x in range(len(self.modelo)):
                if x != i:
                    factor = self.modelo[x][j]  # Factor para la fila x
                    for y in range(len(self.modelo[0])):
                        # Restamos el factor multiplicado por la fila pivote
                        self.modelo[x][y] -= factor * self.modelo[i][y]





prueba = Simplex([[0,3,-3],
                  [0,1,1]], [10,-2],[3,2,7,0])
prueba.construir()
prueba.encontrar_pivote()
prueba.pivotear()
#prueba.mostrar()

