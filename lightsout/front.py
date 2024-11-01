import tkinter as tk

from matrix_logic import procesarMatriz

def obtenerTamanoMatriz(tamano_matriz_entry):
    size = int(tamano_matriz_entry.get())
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
    btn_process = tk.Button(
        ventana_matriz,
        text="Procesar",
        command=lambda: procesarMatriz(matriz_entries, size, mostrarSolucion)
    )
    btn_process.grid(row=size, columnspan=size)

def mostrarSolucion(solucion, size):
    ventana_solucion = tk.Toplevel()
    ventana_solucion.title("Solución")

    for i in range(size):
        for j in range(size):
            valor = solucion[i * size + j]
            color = "green" if valor == 1 else "red"  # Verde para 1, rojo para 0
            label = tk.Label(ventana_solucion, text=str(valor), bg=color, width=3, height=2)
            label.grid(row=i, column=j, padx=2, pady=2)
