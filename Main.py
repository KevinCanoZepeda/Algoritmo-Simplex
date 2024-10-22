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
        i = None
        j = None
        # Recorremos las columnas de la fila de costos (última fila) para encontrar una positiva
        for y in range(len(self.modelo[0]) - 1):
            if self.modelo[-1][y] > 0:  # Si el costo es positivo, es una variable candidata para entrar
                j = y  # Columna candidata
                posibles_posiciones = []
                valor_minimo = []
                
                # Recorremos las filas, excepto la última, para encontrar la fila del pivote
                for x in range(len(self.modelo) - 1):
                    if self.modelo[x][j] > 0:  # Si el coeficiente es positivo
                        posibles_posiciones.append(x)  # Guardamos el índice de la fila
                        valor_minimo.append(self.modelo[x][-1] / self.modelo[x][j])  # Cociente b_i/a_ij
                
                # Si encontramos posibles posiciones, seleccionamos la de menor cociente
                if len(posibles_posiciones) > 0:
                    i = posibles_posiciones[valor_minimo.index(min(valor_minimo))]
                    #print(f'El pivote es {i},{j}')
                    return i, j  # Retornamos las posiciones del pivote (i, j)
        
        return False  # Si no se encontró pivote, retornamos None, None

    def pivotear(self):
    # Volvemos 1 la fila del pivote
        while self.encontrar_pivote() != False:
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
            print("\n")
            self.mostrar()
            print("\n")
        print(f'El valor de z = {self.modelo[-1][-1]*-1}')





prueba = Simplex([[1,1,1,1,0,0],
                  [0,1,1,0,1,0],
                  [0,0,1,0,0,1]], [10,12,30],[2,3,-1,0,0,0])
prueba.construir()
prueba.encontrar_pivote()
prueba.pivotear()
#prueba.mostrar()

