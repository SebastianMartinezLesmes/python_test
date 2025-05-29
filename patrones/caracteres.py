import re

texto = "Mi correo es usuario123@gmail.com y mi número es 555-1234."
patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

coincidencias = re.findall(patron, texto)
print(coincidencias)
