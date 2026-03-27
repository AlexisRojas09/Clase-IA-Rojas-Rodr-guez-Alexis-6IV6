import tkinter as tk
from tkinter import messagebox

Compras = []

def registro_compras():
    Nombre_cliente = entry_nombre.get()
    Mes = entry_mes.get()
    Importe_compra = entry_importe.get()

    valido, mensaje = validar_datos(Nombre_cliente, Mes, Importe_compra)
    if not valido:
        lbl_msg.config(text=mensaje, fg="red")
        return

    Importe_compra = float(Importe_compra)
    porcentaje_descuento = descuento_compra(Mes)
    importe_final = Importe_compra * (1 - porcentaje_descuento)

    compra = {
        'nombre': Nombre_cliente,
        'mes': Mes,
        'importe': Importe_compra,
        'descuento': porcentaje_descuento,
        'importe_final': importe_final
    }
    Compras.append(compra)

    lbl_resultado.config(text=(f"Compra registrada: {Nombre_cliente}. Importe: $ {Importe_compra:.2f} MXN, "
                               f"Descuento: {porcentaje_descuento*100:.0f}%, "
                               f"Total a pagar: $ {importe_final:.2f} MXN"))
    lbl_msg.config(text="", fg="red")
    entry_nombre.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_importe.delete(0, tk.END)
    entry_nombre.focus()

def validar_datos(Nombre_cliente, Mes, Importe_compra):
    meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

    if not Nombre_cliente.strip():
        return False, "El nombre del cliente no puede estar vacío."
    if not Mes.strip():
        return False, "El mes de la compra no puede estar vacío."

    mes_limpio = Mes.strip().lower()
    if mes_limpio not in meses_validos:
        return False, "El mes ingresado no es válido. Debe ser un mes del año (enero-diciembre)."

    try:
        Importe_compra = float(Importe_compra)
        if Importe_compra <= 0:
            return False, "El importe debe ser un número positivo."
    except ValueError:
        return False, "El importe debe ser un número válido."
    return True, ""

def descuento_compra(mes):
    mes_limpio = mes.strip().lower()
    if mes_limpio == "octubre":
        return 0.15
    elif mes_limpio == "diciembre":
        return 0.20
    elif mes_limpio == "julio":
        return 0.10
    else:
        return 0.0

def total_vendido():
    return sum(c['importe_final'] for c in Compras)


def mostrar_historial():
    if not Compras:
        messagebox.showinfo("Historial", "No hay compras registradas.")
        return

    historial = "Historial de compras:\n\n"
    for c in Compras:
        historial += (f"Cliente: {c['nombre']} | Mes: {c['mes']} | Importe: $ {c['importe']:.2f} "
                     f"| Desc: {c['descuento']*100:.0f}% | Total: $ {c['importe_final']:.2f}\n")

    historial += f"\nTotal vendido: $ {total_vendido():.2f} MXN"

    ventana_historial = tk.Toplevel(root)
    ventana_historial.title("Historial y Recaudo")
    ventana_historial.configure(bg='lightblue')
    tk.Label(ventana_historial, text=historial, justify=tk.LEFT, bg='lightblue', font=('Arial', 12)).pack(padx=10, pady=10)


root = tk.Tk()
root.title("Sistema de Descuentos en Tienda")
root.configure(bg='lightblue')

tk.Label(root, text="Nombre del Cliente", bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root, font=('Arial', 12))
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Mes de la Compra", bg='lightblue', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
entry_mes = tk.Entry(root, font=('Arial', 12))
entry_mes.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Importe de Compra", bg='lightblue', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=5)
entry_importe = tk.Entry(root, font=('Arial', 12))
entry_importe.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Registrar Compra", command=registro_compras, bg='lightgreen', font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)

btn_historial = tk.Button(root, text="Mostrar Historial", command=mostrar_historial, bg='lightgreen', font=('Arial', 10, 'bold'))
btn_historial.grid(row=4, column=0, columnspan=2, pady=5)

lbl_resultado = tk.Label(root, text="", fg="green", bg='lightblue', font=('Arial', 12))
lbl_resultado.grid(row=5, column=0, columnspan=2)

lbl_msg = tk.Label(root, text="", fg="red", bg='lightblue', font=('Arial', 12))
lbl_msg.grid(row=6, column=0, columnspan=2)

root.bind("<Return>", lambda e: registro_compras())
entry_nombre.focus()

root.mainloop()