import numpy as np

class Editor:
    def __init__(self, matriz, creador, estado):
        self.matriz = matriz
        self.creador = creador
        self.estado = estado

    def editar_imagen(self, y, x, color):
        self.matriz[y][x] = color

    def rotar_derecha(self):
        self.matriz = np.rot90(self.matriz, -1).tolist()

    def rotar_izquierda(self):
        self.matriz = np.rot90(self.matriz).tolist()

    def reflejo_horizontal(self):
        self.matriz = np.flip(self.matriz, 1).tolist()

    def reflejo_vertical(self):
        self.matriz = np.flip(self.matriz, 0).tolist()

    def alto_contraste(self):
        self.matriz = [[9 if val > 4 else 0 for val in row] for row in self.matriz]

    def negativo(self):
        self.matriz = [[9 - val for val in row] for row in self.matriz]

    def cerrar_imagen(self):
        self.matriz = [[0 for _ in range(50)] for _ in range(50)]
    