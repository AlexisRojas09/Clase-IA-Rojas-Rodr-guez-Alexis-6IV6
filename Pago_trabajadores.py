import tkinter as tk
from tkinter import messagebox

trabajadores = []

def validar_datos(nombre, horas_normales_str, pago_hora_str, horas_extras_str, hijos_str):
    if not nombre.strip():
        return False, "El nombre del trabajador no puede estar vacío."
    
    try:
        horas_normales = float(horas_normales_str)
        if horas_normales < 0:
            return False, "Las horas normales deben ser un número no negativo."
    except ValueError:
        return False, "Las horas normales deben ser un número válido."
    
    try:
        pago_hora = float(pago_hora_str)
        if pago_hora <= 0:
            return False, "El pago por hora debe ser un número positivo."
    except ValueError:
        return False, "El pago por hora debe ser un número válido."
    
    try:
        horas_extras = float(horas_extras_str)
        if horas_extras < 0:
            return False, "Las horas extras deben ser un número no negativo."
    except ValueError:
        return False, "Las horas extras deben ser un número válido."
    
    try:
        hijos = int(hijos_str)
        if hijos < 0:
            return False, "El número de hijos debe ser un número no negativo."
    except ValueError:
        return False, "El número de hijos debe ser un número entero válido."
    
    return True, ""


def calcular_pago_trabajador(horas_normales, pago_hora, horas_extras, hijos):
    """
    Calcula el pago total de un trabajador.
    Retorna pago_horas_normales, pago_horas_extras, bonificacion_hijos, pago_total.
    """
    pago_horas_normales = horas_normales * pago_hora
    pago_horas_extras = horas_extras * (pago_hora * 1.5)
    bonificacion_hijos = hijos * 0.5
    pago_total = pago_horas_normales + pago_horas_extras + bonificacion_hijos
    
    return pago_horas_normales, pago_horas_extras, bonificacion_hijos, pago_total


def registrar_trabajador():
    nombre = entry_nombre.get()
    horas_normales_str = entry_horas_normales.get()
    pago_hora_str = entry_pago_hora.get()
    horas_extras_str = entry_horas_extras.get()
    hijos_str = entry_hijos.get()

    valido, mensaje = validar_datos(nombre, horas_normales_str, pago_hora_str, horas_extras_str, hijos_str)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        return

    horas_normales = float(horas_normales_str)
    pago_hora = float(pago_hora_str)
    horas_extras = float(horas_extras_str)
    hijos = int(hijos_str)

    pago_horas_normales, pago_horas_extras, bonificacion_hijos, pago_total = calcular_pago_trabajador(
        horas_normales, pago_hora, horas_extras, hijos
    )

    trabajadores.append({
        'nombre': nombre,
        'horas_normales': horas_normales,
        'pago_hora': pago_hora,
        'horas_extras': horas_extras,
        'hijos': hijos,
        'pago_horas_normales': pago_horas_normales,
        'pago_horas_extras': pago_horas_extras,
        'bonificacion_hijos': bonificacion_hijos,
        'pago_total': pago_total
    })

    lbl_resultado.config(
        text=(f"Trabajador registrado: {nombre}\n"
              f"Pago horas normales: ${pago_horas_normales:.2f}\n"
              f"Pago horas extras: ${pago_horas_extras:.2f}\n"
              f"Bonificación por hijos: ${bonificacion_hijos:.2f}\n"
              f"Pago total: ${pago_total:.2f}"),
        fg="green"
    )
    lbl_msg.config(text="", fg="red")

    entry_nombre.delete(0, tk.END)
    entry_horas_normales.delete(0, tk.END)
    entry_pago_hora.delete(0, tk.END)
    entry_horas_extras.delete(0, tk.END)
    entry_hijos.delete(0, tk.END)
    entry_nombre.focus()


def mostrar_reporte():
    if not trabajadores:
        messagebox.showinfo("Reporte", "No hay trabajadores registrados.")
        return

    reporte = "REPORTE DE PAGOS DE TRABAJADORES\n" + "="*60 + "\n\n"
    
    total_pagado = 0
    for t in trabajadores:
        reporte += (f"Nombre: {t['nombre']}\n"
                   f"Horas normales: {t['horas_normales']:.1f} x ${t['pago_hora']:.2f} = ${t['pago_horas_normales']:.2f}\n"
                   f"Horas extras: {t['horas_extras']:.1f} x ${t['pago_hora'] * 1.5:.2f} = ${t['pago_horas_extras']:.2f}\n"
                   f"Bonificación ({t['hijos']} hijo/s): ${t['bonificacion_hijos']:.2f}\n"
                   f"Pago total: ${t['pago_total']:.2f}\n\n")
        total_pagado += t['pago_total']

    reporte += "="*60 + "\n"
    reporte += f"Cantidad de trabajadores: {len(trabajadores)}\n"
    reporte += f"Total pagado: ${total_pagado:.2f}"

    ventana_reporte = tk.Toplevel(root)
    ventana_reporte.title("Reporte de Pagos")
    ventana_reporte.configure(bg='lightblue')
    tk.Label(ventana_reporte, text=reporte, justify=tk.LEFT, bg='lightblue', font=('Courier', 9)).pack(padx=10, pady=10)


root = tk.Tk()
root.title("Sistema de pago de trabajadores")
root.configure(bg='lightblue')

tk.Label(root, text="Nombre del Trabajador", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root, font=('Arial', 12))
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Horas Normales", bg='lightblue', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
entry_horas_normales = tk.Entry(root, font=('Arial', 12))
entry_horas_normales.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Pago por Hora Normal", bg='lightblue', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=5)
entry_pago_hora = tk.Entry(root, font=('Arial', 12))
entry_pago_hora.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Horas Extras", bg='lightblue', font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=5)
entry_horas_extras = tk.Entry(root, font=('Arial', 12))
entry_horas_extras.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Número de Hijos", bg='lightblue', font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=5)
entry_hijos = tk.Entry(root, font=('Arial', 12))
entry_hijos.grid(row=4, column=1, padx=10, pady=5)

btn_registrar = tk.Button(root, text="Registrar Trabajador", command=registrar_trabajador, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_registrar.grid(row=5, column=0, columnspan=2, pady=10)

btn_reporte = tk.Button(root, text="Mostrar Reporte de Pagos", command=mostrar_reporte, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_reporte.grid(row=6, column=0, columnspan=2, pady=5)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12), justify=tk.LEFT)
lbl_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=8, column=0, columnspan=2)

root.bind("<Return>", lambda e: registrar_trabajador())
entry_nombre.focus()

root.mainloop()
