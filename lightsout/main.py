import tkinter as tk
from front import obtenerTamanoMatriz

# Configuración de la ventana principal
root = tk.Tk()
root.title("Input Matrix Size")

tamano_matriz = tk.Entry(root)
tamano_matriz.pack(pady=10)

btn_obtener = tk.Button(root, text="Obtener tamaño de la matriz", command=lambda: obtenerTamanoMatriz(tamano_matriz))
btn_obtener.pack()

root.mainloop()