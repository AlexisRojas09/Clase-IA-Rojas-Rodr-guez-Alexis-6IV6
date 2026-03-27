import tkinter as tk
from tkinter import messagebox

visitantes = []

def registro_visitantes():
    Nombre = entry_nombre.get()
    Edad = entry_edad.get()
    Cantidad_juegos = entry_juegos.get()

    valido, mensaje = validar_datos(Nombre, Edad, Cantidad_juegos)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        return
    
    Edad = int(Edad)
    Cantidad_juegos = int(Cantidad_juegos)
    
    costo = calcular_costo(Edad, Cantidad_juegos)

    visitantes.append({
        'nombre': Nombre,
        'edad': Edad,
        'cantidad_juegos': Cantidad_juegos,
        'costo': costo
    })

    lbl_resultado.config(text=f"Visitante registrado: {Nombre}. Costo total: S/ {costo:.2f}")
    lbl_msg.config(text="", fg="red")

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_juegos.delete(0, tk.END)
    entry_nombre.focus()

def validar_datos(Nombre, Edad, Cantidad_juegos):
    if not Nombre.strip():
        return False, "El nombre del visitante no puede estar vacío."
    try:
        Edad = int(Edad)
        if Edad <= 0:
            return False, "La edad debe ser un número positivo."
    except ValueError:
        return False, "La edad debe ser un número válido."
    try:
        Cantidad_juegos = int(Cantidad_juegos)
        if Cantidad_juegos < 0:
            return False, "La cantidad de juegos debe ser un número no negativo."
    except ValueError:
        return False, "La cantidad de juegos debe ser un número válido."
    return True, ""

def calcular_costo(edad, cantidad_juegos):
    costo_base = cantidad_juegos * 50
    
    if edad < 10:
        descuento = 0.25
    elif 10 <= edad <= 17:
        descuento = 0.10
    else:
        descuento = 0.0
    costo_final = costo_base * (1 - descuento)
    return costo_final


def total_recaudado():
    return sum(v['costo'] for v in visitantes)


def mostrar_historial():
    if not visitantes:
        messagebox.showinfo("Historial", "No hay visitantes registrados.")
        return

    historial = "Historial de visitantes:\n\n"
    for v in visitantes:
        historial += (f"Nombre: {v['nombre']} | Edad: {v['edad']} | Juegos: {v['cantidad_juegos']} "
                     f"| Pago: $ {v['costo']:.2f}\n")

    historial += f"\nTotal recaudado: $ {total_recaudado():.2f}"

    ventana_historial = tk.Toplevel(root)
    ventana_historial.title("Historial y Recaudo")
    ventana_historial.configure(bg='lightblue')
    tk.Label(ventana_historial, text=historial, justify=tk.LEFT, bg='lightblue', font=('Arial', 12)).pack(padx=10, pady=10)


root = tk.Tk()
root.title("Sistema de Registro de Visitantes en Parque")
root.configure(bg='lightblue')

tk.Label(root, text="Nombre del Visitante", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root, font=('Arial', 12))
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Edad", bg='lightblue', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(root, font=('Arial', 12))
entry_edad.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Cantidad de Juegos", bg='lightblue', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=5)
entry_juegos = tk.Entry(root, font=('Arial', 12))
entry_juegos.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Registrar Visitante", command=registro_visitantes, bg='lightgreen', font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)

btn_historial = tk.Button(root, text="Mostrar Historial", command=mostrar_historial, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_historial.grid(row=4, column=0, columnspan=2, pady=5)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=5, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=6, column=0, columnspan=2)

root.bind("<Return>", lambda e: registro_visitantes())
entry_nombre.focus()

root.mainloop()