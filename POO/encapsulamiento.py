class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo 

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"✅ Depósito exitoso: ${monto}")
        else:
            print("❌ Monto inválido.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"✅ Retiro exitoso: ${monto}")
        else:
            print("❌ Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.__saldo}")

# Uso de la clase
cuenta1 = CuentaBancaria("Pedro", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.mostrar_saldo()
