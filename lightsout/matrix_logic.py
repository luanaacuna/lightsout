import numpy as np
from tkinter import messagebox
def procesarMatriz(matriz_entries, size, mostrarSolucion_callback):
    matriz = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):
            matriz[i, j] = int(matriz_entries[i][j].get())

    solucion = solucionarLightsOut(matriz)

    if solucion is not None:
        mostrarSolucion_callback(solucion, size)
    else:
        messagebox.showinfo("Resultado", "El sistema no tiene solución")

def solucionarLightsOut(matriz):
    size = matriz.shape[0]
    cantidad_elementos = size * size

    sistema_ecuaciones = np.zeros((cantidad_elementos, cantidad_elementos), dtype=int)
    valores_finales = matriz.flatten()

    for i in range(size):
        for j in range(size):
            indice = i * size + j
            sistema_ecuaciones[indice, indice] = 1
            if i > 0:
                sistema_ecuaciones[indice, (i - 1) * size + j] = 1
            if i < size - 1:
                sistema_ecuaciones[indice, (i + 1) * size + j] = 1
            if j > 0:
                sistema_ecuaciones[indice, i * size + (j - 1)] = 1
            if j < size - 1:
                sistema_ecuaciones[indice, i * size + (j + 1)] = 1

    augmented_matrix = np.concatenate((sistema_ecuaciones, valores_finales.reshape(-1, 1)), axis=1) % 2
    solucion = gauss_jordan_mod2(augmented_matrix)
    
    return solucion if solucion is not None else None

def gauss_jordan_mod2(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        if matrix[i, i] == 0:
            for j in range(i + 1, rows):
                if matrix[j, i] == 1:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
            else:
                continue
        matrix[i] = matrix[i] % 2
        for j in range(rows):
            if j != i and matrix[j, i] == 1:
                matrix[j] = (matrix[j] + matrix[i]) % 2
    for i in range(rows):
        if matrix[i, :-1].sum() == 0 and matrix[i, -1] == 1:
            return None
    return matrix[:, -1] % 2
