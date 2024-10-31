
import numpy as np
import tkinter as tk
from tkinter import messagebox

def obtenerTamanoMatriz():
    size = int(tamano_matriz.get())
    crearVentanaMatriz(size)

def crearVentanaMatriz(size):
    ventana_matriz = tk.Toplevel()
    ventana_matriz.title("Ingrese los elementos de la matriz")
    matriz_entries = []

    for i in range(size):
        fila_entries = []
        for j in range(size):
            entry = tk.Entry(ventana_matriz, width=3)
            entry.grid(row=i, column=j)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

    # Botón para procesar la matriz
    btn_process = tk.Button(ventana_matriz, text="Procesar", command=lambda: procesarMatriz(matriz_entries, size))
    btn_process.grid(row=size, columnspan=size)

def procesarMatriz(matriz_entries, size):
    matriz = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):
            matriz[i, j] = int(matriz_entries[i][j].get())

    solucion = solucionarLightsOut(matriz)

    if solucion is not None:
        mostrarSolucion(solucion)
    else:
        messagebox.showinfo("Resultado", "El sistema no tiene solución")

def solucionarLightsOut(matriz):
    cantidad_elementos = matriz.size
    sistema_ecuaciones = []
    valores_finales = []

    # Generación del sistema de ecuaciones
    for f in range(len(matriz)):
        ecuacion = []
        for c in range(len(matriz[f])):
            if matriz[f][c] == 1:
                ecuacion.append((f, c))  # Guarda coordenadas
            # Añade vecinos
            if c + 1 < len(matriz[f]):
                ecuacion.append((f, c + 1))
            if f + 1 < len(matriz):
                ecuacion.append((f + 1, c))
            if c - 1 >= 0:
                ecuacion.append((f, c - 1))
            if f - 1 >= 0:
                ecuacion.append((f - 1, c))

        sistema_ecuaciones.append(ecuacion)
        valores_finales.append(matriz[f])

    valores_finales = np.array(valores_finales).flatten()
    return escalarMatriz(sistema_ecuaciones, valores_finales)

def escalarMatriz(sistema_ecuaciones, valores_finales):
    
    return [1] * len(valores_finales) 

def mostrarSolucion(solucion):
    ventana_solucion = tk.Toplevel()
    ventana_solucion.title("Solución")
    texto_solucion = tk.Label(ventana_solucion, text=str(solucion))
    texto_solucion.pack(pady=5)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Input Matrix Size")

tamano_matriz = tk.Entry(root)
tamano_matriz.pack(pady=10)

btn_obtener = tk.Button(root, text="Obtener tamaño de la matriz", command=obtenerTamanoMatriz)
btn_obtener.pack()

root.mainloop()
