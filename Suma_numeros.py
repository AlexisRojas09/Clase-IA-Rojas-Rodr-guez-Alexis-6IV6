import tkinter as tk
from tkinter import messagebox

def validar_numero(numero_str):
    if not numero_str.strip():
        return False, "El número no puede estar vacío."
    try:
        numero = int(numero_str)
        if numero <= 0:
            return False, "El número debe ser un entero positivo."
    except ValueError:
        return False, "Ingrese un número entero válido."
    return True, ""


def calcular_suma_numeros(n):
    """
    Calcula la suma de los primeros n números enteros positivos.
    Retorna la suma y la secuencia como string.
    """
    suma = n * (n + 1) // 2
    secuencia = " + ".join(str(i) for i in range(1, n + 1))
    return suma, secuencia


def calcular():
    numero_str = entry_numero.get()

    valido, mensaje = validar_numero(numero_str)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        lbl_secuencia.config(text="")
        lbl_resultado.config(text="")
        entry_numero.delete(0, tk.END)
        entry_numero.focus()
        return

    numero = int(numero_str)
    suma, secuencia = calcular_suma_numeros(numero)

    lbl_secuencia.config(text=f"Secuencia: {secuencia}", fg="blue")
    lbl_resultado.config(text=f"Suma total: {suma}", fg="green")
    lbl_msg.config(text="", fg="red")

    entry_numero.delete(0, tk.END)
    entry_numero.focus()


root = tk.Tk()
root.title("Cálculo de suma de números enteros")
root.configure(bg='lightblue')

tk.Label(root, text="Ingrese un número n:", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_numero = tk.Entry(root, font=('Arial', 12))
entry_numero.grid(row=0, column=1, padx=10, pady=5)

btn_calcular = tk.Button(root, text="Calcular", command=calcular, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_calcular.grid(row=1, column=0, columnspan=2, pady=10)

lbl_secuencia = tk.Label(root, text="", fg="blue", bg='lightblue', font=('Arial', 12))
lbl_secuencia.grid(row=2, column=0, columnspan=2)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=3, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=4, column=0, columnspan=2)

root.bind("<Return>", lambda e: calcular())
entry_numero.focus()

root.mainloop()
