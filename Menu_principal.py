import tkinter as tk
from tkinter import messagebox
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ejercicios = [
    ("1. Aumento de sueldos", "Aumento_sueldos.py"),
    ("2. Pago en parque", "Pago_Parque.py"),
    ("3. Descuentos tienda", "Descuentos_tienda.py"),
    ("4. Validación número < 10", "Validacion_Numero.py"),
    ("5. Validación rango", "Validacion_rango.py"),
    ("6. Registro de intentos", "Validacion_rango_mejorado.py"),
    ("7. Suma de números", "Suma_numeros.py"),
    ("8. Suma acumulativa", "Suma_acumulativa.py"),
    ("9. Suma hasta límite", "Suma_limite.py"),
    ("10. Pago trabajadores", "Pago_trabajadores.py"),
]

def abrir_ejercicio(archivo):
    ruta_archivo = os.path.join(directorio_actual, archivo)
    if not os.path.exists(ruta_archivo):
        messagebox.showerror("Error", f"No se encontró {archivo}")
        return
    os.system(f'start python "{ruta_archivo}"')

root = tk.Tk()
root.title("Menú Principal")
root.configure(bg='lightblue')

tk.Label(root, text="Ejercicios de Programación", bg='lightblue', font=("Arial", 14, "bold")).pack(pady=10)

for titulo, archivo in ejercicios:
    btn = tk.Button(root, text=titulo, command=lambda f=archivo: abrir_ejercicio(f), bg='lightgreen', font=('Arial', 10, 'bold'), width=35, height=1)
    btn.pack(pady=5)

btn_salir = tk.Button(root, text="Salir", command=root.quit, bg='red', font=('Arial', 10, 'bold'), width=35, height=1)
btn_salir.pack(pady=10)

root.mainloop()
