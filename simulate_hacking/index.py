import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import getpass

# ---------- VENTANA PRINCIPAL (CARGA) ----------

def bloquear_cierre():
    pass  # Ignora el botón "X"

mensajes_falsos = [
    "[✓] Iniciando conexión al host remoto...",
    "[✓] Inyectando payload...",
    "[✓] Desactivando firewall...",
    "[✓] Escaneando red...",
    "[✓] Copiando datos a servidor remoto...",
    "[✓] Eliminando rastros...",
    "[✓] Instalando backdoor...",
    "[✓] Finalizando operación..."
]

def cargar():
    progreso["value"] = 0
    ventana.update_idletasks()

    for i in range(101):
        progreso["value"] = i
        porcentaje.set(f"Instalando virus... {i}%")
        ventana.update_idletasks()

        if i % 13 == 0 and mensajes_falsos:
            consola.insert(tk.END, mensajes_falsos.pop(0) + "\n")
            consola.see(tk.END)

        time.sleep(0.08)

    porcentaje.set("¡Instalación completada!")
    consola.insert(tk.END, "[✓] Proceso finalizado exitosamente.\n")
    ventana.update_idletasks()
    ventana.after(3000, mostrar_segunda_ventana)

# ---------- SEGUNDA VENTANA (IMAGEN + MENSAJE) ----------

def mostrar_segunda_ventana():
    ventana.destroy()  # Cierra la ventana principal

    usuario = getpass.getuser()

    segunda = tk.Tk()
    segunda.title("Advertencia final")
    segunda.geometry("800x600")  # Ventana más grande
    segunda.configure(bg="black")
    segunda.resizable(False, False)

    try:
        img = Image.open("glitch skull.png")
        img = img.resize((300, 300))  # Imagen más grande
        imagen = ImageTk.PhotoImage(img)
        label_img = tk.Label(segunda, image=imagen, bg="black")
        label_img.image = imagen  # Mantener referencia
        label_img.pack(pady=30)
    except Exception as e:
        print("Error cargando imagen:", e)

    texto = tk.Label(
        segunda,
        text=f"Ahora te tengo, {usuario}...",
        fg="lime",
        bg="black",
        font=("Courier New", 24, "bold")  # Texto más grande
    )
    texto.pack(pady=10)

    segunda.after(6000, segunda.destroy)  # Cierra después de 6s
    segunda.mainloop()

# ---------- INICIAR VENTANA DE CARGA ----------

ventana = tk.Tk()
ventana.title("terminal.exe")
ventana.geometry("600x300")
ventana.configure(bg="black")
ventana.resizable(False, False)

# Cambiar icono de ventana
try:
    ventana.iconbitmap("glitch-skull.ico")
except Exception as e:
    print("No se pudo cargar el icono:", e)

ventana.protocol("WM_DELETE_WINDOW", bloquear_cierre)

# Estilo hacker
fuente_terminal = ("Courier New", 12)
estilo_barra = ttk.Style()
estilo_barra.theme_use('clam')
estilo_barra.configure("green.Horizontal.TProgressbar",
                       troughcolor='black',
                       background='lime',
                       bordercolor='black',
                       lightcolor='lime',
                       darkcolor='green')

# Título
porcentaje = tk.StringVar()
porcentaje.set("Instalando virus... 0%")
label = tk.Label(ventana, textvariable=porcentaje, font=("Courier New", 14, "bold"),
                 fg="lime", bg="black")
label.pack(pady=(10, 0))

# Barra de carga
progreso = ttk.Progressbar(ventana, orient="horizontal", length=500,
                           mode="determinate", style="green.Horizontal.TProgressbar")
progreso.pack(pady=(5, 10))

# Consola hacker
consola = tk.Text(ventana, height=10, bg="black", fg="lime",
                  insertbackground="lime", font=fuente_terminal, borderwidth=0)
consola.pack(padx=10, pady=(0, 10), fill="both", expand=True)
consola.insert(tk.END, "[*] Ejecutando terminal...\n")

ventana.after(500, cargar)
ventana.mainloop()
