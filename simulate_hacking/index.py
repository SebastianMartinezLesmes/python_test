import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import getpass
import random

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

advertencias_falsas = [
    "[!] Atención: actividad sospechosa detectada...",
    "[!] Tu cámara ha sido activada.",
    "[!] Extrayendo contraseñas de Chrome...",
    "[!] Monitoreando pulsaciones de teclado.",
    "[!] Borrando archivos innecesarios...",
    "[!] Localización GPS detectada.",
    "[!] Analizando conversaciones recientes...",
    "[!] Transmitiendo feed en vivo...",
    "[!] Enviando credenciales al servidor...",
    "[!] Conexión interceptada por un tercero.",
]

def escribir_mensaje(mensaje):
    for char in mensaje:
        consola.insert(tk.END, char)
        consola.update_idletasks()
        time.sleep(0.01)
    consola.insert(tk.END, "\n")
    consola.see(tk.END)

def cargar():
    progreso["value"] = 0
    ventana.update_idletasks()

    for i in range(101):
        progreso["value"] = i
        porcentaje.set(f"Instalando virus... {i}%")
        ventana.update_idletasks()

        # Mostrar mensajes falsos y advertencias
        if i % 13 == 0:
            if mensajes_falsos:
                escribir_mensaje(mensajes_falsos.pop(0))

            if random.random() < 0.5 and advertencias_falsas:
                escribir_mensaje(random.choice(advertencias_falsas))

        time.sleep(0.08)

    porcentaje.set("¡Instalación completada!")
    escribir_mensaje("[✓] Proceso finalizado exitosamente.")
    ventana.update_idletasks()
    ventana.after(3000, mostrar_segunda_ventana)

# ---------- SEGUNDA VENTANA (IMAGEN + MENSAJE + GLITCH) ----------

def glitch_text(label, colores=["lime", "green", "red", "white"]):
    def cambiar_color():
        color = random.choice(colores)
        label.config(fg=color)
        label.after(100, cambiar_color)
    cambiar_color()

def mostrar_segunda_ventana():
    ventana.destroy()

    usuario = getpass.getuser()

    segunda = tk.Tk()
    segunda.title("Advertencia final")
    segunda.geometry("800x600")
    segunda.configure(bg="black")
    segunda.resizable(False, False)

    try:
        img = Image.open("glitch skull.png")
        img = img.resize((300, 300))
        imagen = ImageTk.PhotoImage(img)
        label_img = tk.Label(segunda, image=imagen, bg="black")
        label_img.image = imagen
        label_img.pack(pady=30)
    except Exception as e:
        print("Error cargando imagen:", e)

    texto = tk.Label(
        segunda,
        text=f"Ahora te tengo, {usuario}...",
        fg="lime",
        bg="black",
        font=("Courier New", 24, "bold")
    )
    texto.pack(pady=10)

    glitch_text(texto)

    segunda.after(6000, segunda.destroy)
    segunda.mainloop()


# ---------- INICIAR VENTANA DE CARGA ----------

ventana = tk.Tk()
ventana.title("terminal.exe")
ventana.geometry("600x300")
ventana.configure(bg="black")
ventana.resizable(False, False)

try:
    ventana.iconbitmap("glitch-skull.ico")
except Exception as e:
    print("No se pudo cargar el icono:", e)

ventana.protocol("WM_DELETE_WINDOW", bloquear_cierre)

fuente_terminal = ("Courier New", 12)
estilo_barra = ttk.Style()
estilo_barra.theme_use('clam')
estilo_barra.configure("green.Horizontal.TProgressbar",
                       troughcolor='black',
                       background='lime',
                       bordercolor='black',
                       lightcolor='lime',
                       darkcolor='green')

porcentaje = tk.StringVar()
porcentaje.set("Instalando virus... 0%")
label = tk.Label(ventana, textvariable=porcentaje, font=("Courier New", 14, "bold"),
                 fg="lime", bg="black")
label.pack(pady=(10, 0))

progreso = ttk.Progressbar(ventana, orient="horizontal", length=500,
                           mode="determinate", style="green.Horizontal.TProgressbar")
progreso.pack(pady=(5, 10))

consola = tk.Text(ventana, height=10, bg="black", fg="lime",
                  insertbackground="lime", font=fuente_terminal, borderwidth=0)
consola.pack(padx=10, pady=(0, 10), fill="both", expand=True)
escribir_mensaje("[*] Ejecutando terminal...")

ventana.after(500, cargar)
ventana.mainloop()
