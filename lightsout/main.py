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
    size = matriz.shape[0]
    cantidad_elementos = size * size

    # Construir el sistema de ecuaciones en módulo 2
    sistema_ecuaciones = np.zeros((cantidad_elementos, cantidad_elementos), dtype=int)
    valores_finales = matriz.flatten()

    # Llenar la matriz del sistema de ecuaciones
    for i in range(size):
        for j in range(size):
            indice = i * size + j
            # El propio botón
            sistema_ecuaciones[indice, indice] = 1
            # Vecinos
            if i > 0:  # Celda de arriba
                sistema_ecuaciones[indice, (i - 1) * size + j] = 1
            if i < size - 1:  # Celda de abajo
                sistema_ecuaciones[indice, (i + 1) * size + j] = 1
            if j > 0:  # Celda izquierda
                sistema_ecuaciones[indice, i * size + (j - 1)] = 1
            if j < size - 1:  # Celda derecha
                sistema_ecuaciones[indice, i * size + (j + 1)] = 1


    # Aplicar eliminación de Gauss-Jordan en módulo 2
    augmented_matrix = np.concatenate((sistema_ecuaciones, valores_finales.reshape(-1, 1)), axis=1) % 2
    solucion = gauss_jordan_mod2(augmented_matrix)
    
    if solucion is None:
        return None  # No hay solución
    return solucion

def gauss_jordan_mod2(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        if matrix[i, i] == 0:
            # Intentar encontrar una fila con un 1 en la misma columna para intercambiar
            for j in range(i + 1, rows):
                if matrix[j, i] == 1:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
            else:
                # No se encontró fila para intercambiar, continuar al siguiente pivote
                continue
        # Hacer el pivote igual a 1
        matrix[i] = matrix[i] % 2  # Mantener todo en módulo 2
        # Eliminar el 1 en otras filas de la columna actual
        for j in range(rows):
            if j != i and matrix[j, i] == 1:
                matrix[j] = (matrix[j] + matrix[i]) % 2
    # Revisar si existe una solución única
    for i in range(rows):
        if matrix[i, :-1].sum() == 0 and matrix[i, -1] == 1:
            return None  # No hay solución
    # Extraer solución
    return matrix[:, -1] % 2

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

