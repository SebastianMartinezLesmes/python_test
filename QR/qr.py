import qrcode

# Datos del QR
data = "https://github.com/SebastianMartinezLesmes"
output_path = "qr.png"

# Crear QR con alta corrección de errores
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Crear imagen del QR con color verde neón sobre fondo negro
qr_img = qr.make_image(fill_color="#39FF14", back_color="black").convert("RGB")

# Guardar el QR final
qr_img.save(output_path)

print("✅ QR verde neón generado correctamente:", output_path)
