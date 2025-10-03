class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        print(f"Cuenta creada para {titular}")
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado con éxito")
        else:
            print("No puedes depositar una cantidad negativa o cero")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado con éxito")
        else:
            print("Fondos insuficientes")

    def ver_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")
        return self.saldo


# Programa principal
nombre = input("Ingrese el nombre del titular: ")
saldo_inicial = int(input("Ingrese el saldo inicial: "))

cuenta = CuentaBancaria(nombre, saldo_inicial)

while True:
    print("\n--- Menú ---")
    print("1 > Depositar")
    print("2 > Retirar")
    print("3 > Ver saldo")
    print("4 > Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = int(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(monto)
    elif opcion == "2":
        monto = int(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "3":
        cuenta.ver_saldo()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")