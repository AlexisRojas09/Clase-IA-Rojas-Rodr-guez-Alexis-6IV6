"""
Código anterior:
import tkinter as tk
from tkinter import messagebox

intentos = 0

def validar_numero(numero_str):
    if not numero_str.strip():
        return False, "El número no puede estar vacío."
    try:
        numero = int(numero_str)
    except ValueError:
        return False, "Ingrese un número entero válido."

    if numero >= 10:
        return False, "El número debe ser menor que 10."

    return True, ""


def registro_numero():
    global intentos
    intentos += 1

    numero_str = entry_numero.get()
    valido, mensaje = validar_numero(numero_str)

    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        lbl_resultado.config(text="")
        entry_numero.delete(0, tk.END)
        entry_numero.focus()
        return

    numero = int(numero_str)
    lbl_resultado.config(text=f"Número correcto ingresado: {numero}")
    lbl_msg.config(text=f"Intentos realizados: {intentos}", fg="green")

    entry_numero.delete(0, tk.END)
    entry_numero.focus()


root = tk.Tk()
root.title("Validación de número menor que 10")

tk.Label(root, text="Ingrese un número entero:").grid(row=0, column=0, padx=10, pady=5)
entry_numero = tk.Entry(root)
entry_numero.grid(row=0, column=1, padx=10, pady=5)

btn_validar = tk.Button(root, text="Validar", command=registro_numero)
btn_validar.grid(row=1, column=0, columnspan=2, pady=10)

lbl_resultado = tk.Label(root, text="", fg="green")
lbl_resultado.grid(row=2, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red")
lbl_msg.grid(row=3, column=0, columnspan=2)

root.bind("<Return>", lambda e: registro_numero())
entry_numero.focus()

root.mainloop()
"""

import tkinter as tk
from tkinter import messagebox

intentos = 0

def validar_numero(numero_str):
    if not numero_str.strip():
        return False, "El número no puede estar vacío."
    try:
        numero = int(numero_str)
    except ValueError:
        return False, "Ingrese un número entero válido."

    if not (0 < numero < 20):
        return False, "El número debe estar dentro del rango (0,20), es decir, mayor que 0 y menor que 20."

    return True, ""


def registro_numero():
    global intentos
    intentos += 1

    numero_str = entry_numero.get()
    valido, mensaje = validar_numero(numero_str)

    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        lbl_resultado.config(text="")
        entry_numero.delete(0, tk.END)
        entry_numero.focus()
        return

    numero = int(numero_str)
    lbl_resultado.config(text=f"Número correcto ingresado: {numero}")
    lbl_msg.config(text=f"Intentos realizados: {intentos}", fg="green")

    entry_numero.delete(0, tk.END)
    entry_numero.focus()


root = tk.Tk()
root.title("Validación de número dentro de un rango")
root.configure(bg='lightblue')

tk.Label(root, text="Ingrese un número entero:", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_numero = tk.Entry(root, font=('Arial', 12))
entry_numero.grid(row=0, column=1, padx=10, pady=5)

btn_validar = tk.Button(root, text="Validar", command=registro_numero, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_validar.grid(row=1, column=0, columnspan=2, pady=10)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=2, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=3, column=0, columnspan=2)

root.bind("<Return>", lambda e: registro_numero())
entry_numero.focus()

root.mainloop()