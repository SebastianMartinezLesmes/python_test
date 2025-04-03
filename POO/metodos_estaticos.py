class Producto:
    total_productos = 0 
    lista_productos = [] 

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.total_productos += 1
        Producto.lista_productos.append(self) 

    @classmethod
    def cantidad_productos(cls):
        return f"Total de productos creados: {cls.total_productos}"

    @classmethod
    def agregar_producto(cls):
        nombre = input("¿Cómo se llama el producto? ").strip()
        while True:
            try:
                precio = float(input("¿Cuánto vale el producto? ").strip())
                break 
            except ValueError:
                print("❌ Por favor, ingrese un valor numérico válido.")
        
        cls(nombre, precio) 

    @classmethod
    def mostrar_productos(cls):
        print("\n📦 Lista de Productos:")
        for p in cls.lista_productos:
            print(f"- {p.nombre}: ${p.precio:.2f}")
        print("\n" + cls.cantidad_productos()) 

while True:
    pregunta = input("¿Quieres agregar un producto? (si/no): ").strip().lower()
    
    if pregunta in ["si", "s"]:
        Producto.agregar_producto()
    elif pregunta in ["no", "n"]:
        break  
    else:
        print("⚠️ Respuesta no válida. Responde con 'si' o 'no'.")

# Mostrar resultados
Producto.mostrar_productos()
