import tkinter as tk
from tkinter import messagebox

trabajadores = []

def calcular_aumento(sueldo):
    if sueldo < 4000:
        return sueldo * 1.15
    elif sueldo <= 7000:
        return sueldo * 1.10
    else:
        return sueldo * 1.08

def validar_datos(trabajador, sueldo_str):
    if not trabajador.strip():
        return False, "El nombre del trabajador no puede estar vacío."
    try:
        sueldo = float(sueldo_str)
        if sueldo <= 0:
            return False, "El sueldo debe ser un número positivo."
    except ValueError:
        return False, "El sueldo debe ser un número válido."
    return True, ""

def procesar_trabajador():
    trabajador = entry_trabajador.get()
    sueldo_str = entry_sueldo.get()
    
    valido, mensaje = validar_datos(trabajador, sueldo_str)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        return
    
    sueldo = float(sueldo_str)
    nuevo_sueldo = calcular_aumento(sueldo)
    
    trabajadores.append({
        'nombre': trabajador,
        'sueldo_original': sueldo,
        'nuevo_sueldo': nuevo_sueldo
    })
    
    lbl_resultado.config(text=f"Nuevo sueldo de {trabajador}: ${nuevo_sueldo:.2f}")
    lbl_msg.config(text="", fg="red")
    
    entry_trabajador.delete(0, tk.END)
    entry_sueldo.delete(0, tk.END)
    entry_trabajador.focus()

def mostrar_historial():
    if not trabajadores:
        messagebox.showinfo("Historial", "No hay trabajadores registrados.")
        return
    
    historial = "Historial de trabajadores:\n\n"
    for t in trabajadores:
        historial += f"Nombre: {t['nombre']}\nSueldo Original: ${t['sueldo_original']:.2f}\nNuevo Sueldo: ${t['nuevo_sueldo']:.2f}\n\n"
    
    ventana_historial = tk.Toplevel(root)
    ventana_historial.title("Historial de Trabajadores")
    ventana_historial.configure(bg='lightblue')
    tk.Label(ventana_historial, text=historial, justify=tk.LEFT, bg='lightblue', font=('Arial', 12)).pack(padx=10, pady=10)


root = tk.Tk()
root.title("Sistema de Aumento de Sueldos")
root.configure(bg='lightblue')

tk.Label(root, text="Nombre del Trabajador", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_trabajador = tk.Entry(root, font=('Arial', 12))
entry_trabajador.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sueldo Básico", bg='lightblue', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
entry_sueldo = tk.Entry(root, font=('Arial', 12))
entry_sueldo.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calcular Aumento", command=procesar_trabajador, bg='lightgreen', font=('Arial', 10, 'bold')).grid(row=2, column=0, columnspan=2, pady=10)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Mostrar Historial", command=mostrar_historial, bg='lightgreen', font=('Arial', 10, 'bold')).grid(row=4, column=0, columnspan=2, pady=10)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=5, column=0, columnspan=2)

root.bind("<Return>", lambda e: procesar_trabajador())
entry_trabajador.focus()

root.mainloop()