import tkinter as tk
from tkinter import messagebox

numeros = []
suma_acumulada = 0

def validar_numero(numero_str):
    if not numero_str.strip():
        return False, "El número no puede estar vacío."
    try:
        numero = int(numero_str)
    except ValueError:
        return False, "Ingrese un número entero válido."
    return True, ""


def agregar_numero():
    global suma_acumulada
    
    numero_str = entry_numero.get()

    valido, mensaje = validar_numero(numero_str)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        entry_numero.delete(0, tk.END)
        entry_numero.focus()
        return

    numero = int(numero_str)

    if numero == 0:
        finalizar_proceso()
        return

    numeros.append(numero)
    suma_acumulada += numero

    lbl_lista.config(text=f"Números ingresados: {', '.join(map(str, numeros))}", fg="blue")
    lbl_suma.config(text=f"Suma acumulada: {suma_acumulada}", fg="green")
    lbl_msg.config(text="", fg="red")

    entry_numero.delete(0, tk.END)
    entry_numero.focus()


def finalizar_proceso():
    if not numeros:
        messagebox.showinfo("Resultado", "No se ingresaron números.")
        return

    resultado = (f"RESUMEN FINAL:\n\n"
                f"Números ingresados: {', '.join(map(str, numeros))}\n"
                f"Cantidad de números: {len(numeros)}\n"
                f"Suma total: {suma_acumulada}")

    messagebox.showinfo("Proceso Finalizado", resultado)
    
    # Reiniciar variables
    global numeros, suma_acumulada
    numeros = []
    suma_acumulada = 0
    
    lbl_lista.config(text="")
    lbl_suma.config(text="")
    lbl_msg.config(text="Ingrese números (0 para finalizar)", fg="green")
    entry_numero.delete(0, tk.END)
    entry_numero.focus()


root = tk.Tk()
root.title("Sistema de suma acumulativa")
root.configure(bg='lightblue')

tk.Label(root, text="Ingrese números (0 para finalizar):", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_numero = tk.Entry(root, font=('Arial', 12))
entry_numero.grid(row=0, column=1, padx=10, pady=5)

btn_agregar = tk.Button(root, text="Agregar número", command=agregar_numero, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_agregar.grid(row=1, column=0, columnspan=2, pady=10)

btn_finalizar = tk.Button(root, text="Finalizar (Ingresa 0)", command=finalizar_proceso, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_finalizar.grid(row=2, column=0, columnspan=2, pady=5)

lbl_lista = tk.Label(root, text="", fg="blue", bg='lightblue', font=('Arial', 12), wraplength=300, justify=tk.LEFT)
lbl_lista.grid(row=3, column=0, columnspan=2, padx=10)

lbl_suma = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_suma.grid(row=4, column=0, columnspan=2, pady=10)

lbl_msg = tk.Label(root, text="Ingrese números (0 para finalizar)", fg="green", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=5, column=0, columnspan=2)

root.bind("<Return>", lambda e: agregar_numero())
entry_numero.focus()

root.mainloop()
