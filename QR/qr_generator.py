import qrcode
from PIL import Image

# Datos del QR
data = "https://github.com/SebastianMartinezLesmes"
logo_path = "../simulate_hacking/glitch skull.png"  # Tu imagen subida
output_path = "qr.png"

# Crear QR con alta corrección de errores
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta tolerancia
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Imagen base del QR con color verde neón y fondo negro
qr_img = qr.make_image(fill_color="#39FF14", back_color="black").convert("RGB")

# Cargar el logo
logo = Image.open(logo_path)

# Redimensionar logo al 40% del QR
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.4)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Pegar el logo centrado
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Guardar el QR final
qr_img.save(output_path)

print("✅ QR con logo verde neón generado correctamente:", output_path)
