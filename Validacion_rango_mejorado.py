import tkinter as tk
from tkinter import messagebox

intentos = 0
intentos_incorrectos = 0
lista_intentos = []

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
    global intentos, intentos_incorrectos
    intentos += 1

    numero_str = entry_numero.get()
    lista_intentos.append(numero_str)

    valido, mensaje = validar_numero(numero_str)

    if not valido:
        intentos_incorrectos += 1
        lbl_msg.config(text=mensaje, fg="red")
        lbl_resultado.config(text="")
        entry_numero.delete(0, tk.END)
        entry_numero.focus()
        return

    numero = int(numero_str)
    lbl_resultado.config(text=f"Número correcto ingresado: {numero}")
    lbl_msg.config(text=f"Intentos totales: {intentos} | Incorrectos: {intentos_incorrectos}", fg="green")

    entry_numero.delete(0, tk.END)
    entry_numero.focus()


def mostrar_historial():
    if not lista_intentos:
        messagebox.showinfo("Historial", "No hay intentos registrados.")
        return

    historial = "Historial de intentos:\n\n"
    for i, intento in enumerate(lista_intentos, 1):
        valido, _ = validar_numero(intento)
        status = "Correcto" if valido else "Incorrecto"
        historial += f"Intento {i}: '{intento}' - {status}\n"

    historial += f"\nTotal intentos: {intentos}\nIntentos incorrectos: {intentos_incorrectos}"

    ventana_historial = tk.Toplevel(root)
    ventana_historial.title("Historial de Intentos")
    ventana_historial.configure(bg='lightblue')
    tk.Label(ventana_historial, text=historial, justify=tk.LEFT, bg='lightblue', font=('Arial', 12)).pack(padx=10, pady=10)


root = tk.Tk()
root.title("Validación de número dentro de un rango")
root.configure(bg='lightblue')

tk.Label(root, text="Ingrese un número entero:", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_numero = tk.Entry(root, font=('Arial', 12))
entry_numero.grid(row=0, column=1, padx=10, pady=5)

btn_validar = tk.Button(root, text="Validar", command=registro_numero, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_validar.grid(row=1, column=0, columnspan=2, pady=10)

btn_historial = tk.Button(root, text="Mostrar Historial", command=mostrar_historial, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_historial.grid(row=2, column=0, columnspan=2, pady=5)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=3, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=4, column=0, columnspan=2)

root.bind("<Return>", lambda e: registro_numero())
entry_numero.focus()

root.mainloop()