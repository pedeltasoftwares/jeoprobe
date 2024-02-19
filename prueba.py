import tkinter as tk
from tkinter import messagebox
import uuid

# Función para obtener la dirección MAC
def obtener_mac_address():
    mac_address = uuid.getnode()
    return ':'.join(('%012X' % mac_address)[i:i+2] for i in range(0, 12, 2))

# Función para verificar la dirección MAC y mostrar la interfaz si está autorizada
def verificar_mac_y_mostrar_interfaz():
    mac_address_autorizada = "E0:D0:45:87:91:F9"
    mac_address_actual = obtener_mac_address()
    if mac_address_actual == mac_address_autorizada:
        # Si la dirección MAC coincide, mostrar la interfaz
        mostrar_interfaz()
    else:
        # Si la dirección MAC no coincide, mostrar un mensaje de error y salir del programa
        messagebox.showerror("Error", "La dirección MAC no está autorizada.")

# Función para mostrar la interfaz
def mostrar_interfaz():
    root = tk.Tk()
    root.title("Interfaz Autorizada")
    # Aquí puedes agregar los elementos de tu interfaz gráfica
    root.mainloop()

# Verificar la dirección MAC y mostrar la interfaz si está autorizada
verificar_mac_y_mostrar_interfaz()
