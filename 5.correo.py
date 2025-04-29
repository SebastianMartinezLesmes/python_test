import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración
remitente = "tucorreo@gmail.com"
clave = "tu_contraseña_o_token"
destinatario = "destinatario@gmail.com"
asunto = "Correo desde Python"
mensaje = "¡Hola! Este correo fue enviado desde un script Python. 😊"

# Crear mensaje
msg = MIMEMultipart()
msg['From'] = remitente
msg['To'] = destinatario
msg['Subject'] = asunto
msg.attach(MIMEText(mensaje, 'plain'))

# Enviar
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, clave)
    servidor.send_message(msg)
    servidor.quit()
    print("✅ ¡Correo enviado con éxito!")
except Exception as e:
    print("❌ Error al enviar el correo:", e)
