from tkinter import *
from tkinter import filedialog, messagebox
from Clase import Editor
import os

def Matriz(canvas, filas=50, columnas=50, ancho=12, alto=12):
    for fila in range(filas):
        for columna in range(columnas):
            canvas.create_rectangle(columna * ancho, fila * alto, (columna + 1) * ancho, (fila + 1) * alto, fill="white", outline="black")

def crear_botones(ventana, colores, filas=2, columnas=5):
    frame_botones = Frame(ventana)
    frame_botones.pack(side=TOP, padx=10, pady=5)
    color_keys = list(colores.keys())

    for i in range(filas):
        for j in range(columnas):
            idx = i * columnas + j
            if idx < len(color_keys):
                color = color_keys[idx]
                boton_color = Button(frame_botones, bg=colores[color], command=lambda color=color: seleccionar_color(color), width=5, height=2)
                boton_color.grid(row=i, column=j)

def crear_botones_funcionalidades(ventana, funcionalidades, filas=5, columnas=2):
    frame_funcionalidades = Frame(ventana)
    frame_funcionalidades.pack(side=LEFT, padx=10, pady=5)
    funcionalidad_keys = list(funcionalidades.keys())

    for i in range(filas):
        for j in range(columnas):
            idx = i * columnas + j
            if idx < len(funcionalidad_keys):
                texto = funcionalidad_keys[idx]
                comando = funcionalidades[texto]
                boton_funcionalidad = Button(frame_funcionalidades, text=texto, command=comando, width=12, height=2)
                boton_funcionalidad.grid(row=i, column=j)

def seleccionar_color(color):
    global selected_color
    selected_color = color

def dibujar(event):
    x, y = event.x // pixel_size, event.y // pixel_size
    if 0 <= x < 50 and 0 <= y < 50:
        editor.editar_imagen(y, x, selected_color)
        actualizar_matriz(canvas, editor.matriz, colores)

def actualizar_matriz(canvas, matriz, colores):
    canvas.delete("all")
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            color = colores[matriz[fila][columna]]
            canvas.create_rectangle(columna * pixel_size, fila * pixel_size, (columna + 1) * pixel_size, (fila + 1) * pixel_size, fill=color, outline="black")

def actualizar_matriz_numerica(canvas, matriz):
    canvas.delete("all")
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            canvas.create_text(columna * pixel_size, fila * pixel_size, text=str(matriz[fila][columna]), fill="black")

def actualizar_matriz_ascii(canvas, matriz):
    canvas.delete("all")
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            canvas.create_text(columna * pixel_size, fila * pixel_size, text=matriz[fila][columna], fill="black")

def zoom_in():
    global pixel_size
    pixel_size += 2
    actualizar_matriz(canvas, editor.matriz, colores)

def zoom_out():
    global pixel_size
    pixel_size = max(2, pixel_size - 2)
    actualizar_matriz(canvas, editor.matriz, colores)

def rotar_derecha():
    editor.rotar_derecha()
    actualizar_matriz(canvas, editor.matriz, colores)

def rotar_izquierda():
    editor.rotar_izquierda()
    actualizar_matriz(canvas, editor.matriz, colores)

def reflejo_horizontal():
    editor.reflejo_horizontal()
    actualizar_matriz(canvas, editor.matriz, colores)

def reflejo_vertical():
    editor.reflejo_vertical()
    actualizar_matriz(canvas, editor.matriz, colores)

def alto_contraste():
    editor.alto_contraste()
    actualizar_matriz(canvas, editor.matriz, colores)

def negativo():
    editor.negativo()
    actualizar_matriz(canvas, editor.matriz, colores)

def cerrar_imagen():
    editor.cerrar_imagen()
    actualizar_matriz(canvas, editor.matriz, colores)

def ver_imagen():
    actualizar_matriz(canvas, editor.matriz, colores)

def guardar_imagen():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if archivo:
        with open(archivo, 'w') as f:
            for row in editor.matriz:
                f.write(' '.join(map(str, row)) + '\n')

def cargar_imagen():
    archivo = filedialog.askopenfilename(title="Cargar imagen", filetypes=[("Text files", "*.txt")])
    if archivo and os.path.exists(archivo):
        with open(archivo, 'r') as f:
            nueva_matriz = [list(map(int, line.strip().split())) for line in f]
            editor.matriz = nueva_matriz
            actualizar_matriz(canvas, editor.matriz, colores)
    else:
        messagebox.showerror("Error", "Archivo no encontrado")

def ascii_art():
    conversion = ['.', ':', '-', '=', '!', '&', '$', '%', '@', ' ']
    ascii_matrix = [[conversion[val] for val in row] for row in editor.matriz]
    actualizar_matriz_ascii(canvas, ascii_matrix)

ventana = Tk()
ventana.title("Paintxel")
ventana.geometry("1000x700")  # Ampliar para dar espacio a los botones
ventana.resizable(0, 0)

menubar = Menu(ventana)
menubar.add_command(label="Cargar Imagen", command=cargar_imagen)
menubar.add_command(label="Guardar Imagen", command=guardar_imagen)
menubar.add_command(label="Limpiar Matriz", command=cerrar_imagen)
menubar.add_command(label="Ver Imagen", command=ver_imagen)
menubar.add_command(label="Ver Matriz Numérica", command=lambda: actualizar_matriz_numerica(canvas, editor.matriz))
ventana.config(menu=menubar)

canvas = Canvas(ventana, width=600, height=600)
canvas.pack(side=LEFT, padx=10, pady=10)

# Crear instancia de Editor
matriz_inicial = [[0 for _ in range(50)] for _ in range(50)]
editor = Editor(matriz_inicial, "Creador", "creado")

colores = {
    0: "white",
    1: "green",
    2: "yellow",
    3: "red",
    4: "blue",
    5: "aquamarine",
    6: "magenta",
    7: "purple",
    8: "light green",
    9: "black"
}

funcionalidades = {
    "Zoom In": zoom_in,
    "Zoom Out": zoom_out,
    "Rotar Derecha": rotar_derecha,
    "Rotar Izquierda": rotar_izquierda,
    "Reflejo Horizontal": reflejo_horizontal,
    "Reflejo Vertical": reflejo_vertical,
    "Alto Contraste": alto_contraste,
    "Negativo": negativo,
    "ASCII Art": ascii_art
}

selected_color = 0

# Crear botones de colores
crear_botones(ventana, colores)

# Crear botones de funcionalidades
crear_botones_funcionalidades(ventana, funcionalidades)

canvas.bind("<B1-Motion>", dibujar)

pixel_size = 12  # Tamaño inicial de los píxeles

Matriz(canvas)
actualizar_matriz(canvas, editor.matriz, colores)

ventana.mainloop()
