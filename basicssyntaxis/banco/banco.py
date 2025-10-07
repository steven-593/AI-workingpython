class Account:
    def __init__(self, initial_balance=1000):
        """Clase base para una cuenta bancaria"""
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        """Deposita dinero en la cuenta"""
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.balance += amount
        self.transactions.append(f"Depósito: +{amount}")
        return self.balance

    def withdraw(self, amount):
        """Retira dinero de la cuenta si hay fondos suficientes"""
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes.")
        self.balance -= amount
        self.transactions.append(f"Retiro: -{amount}")
        return self.balance

    def get_balance(self):
        """Devuelve el saldo actual"""
        return self.balance

    def get_transactions(self):
        """Devuelve el historial de transacciones"""
        return self.transactions


class SavingsAccount(Account):
    def __init__(self, initial_balance=1000, interest_rate=0.05):
        """Cuenta de ahorros que aplica interés"""
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calcula y aplica el interés al saldo"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interés aplicado: +{interest:.2f}")
        return self.balance


# -----------------------------
# Programa principal con menú
# -----------------------------

# Crea una cuenta de ahorros con saldo inicial de 1000 y 5% de interés
account = SavingsAccount()

print("=== Bienvenido al Sistema Bancario ===")

while True:
    print("\n--- Menú ---")
    print("1 > Depositar")
    print("2 > Retirar")
    print("3 > Ver saldo")
    print("4 > Ver transacciones")
    print("5 > Aplicar interés")
    print("6 > Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            monto = float(input("Cantidad a depositar: "))
            nuevo_saldo = account.deposit(monto)
            print(f"Depósito realizado. Saldo actual: {nuevo_saldo:.2f}")

        elif opcion == "2":
            monto = float(input("Cantidad a retirar: "))
            nuevo_saldo = account.withdraw(monto)
            print(f"Retiro realizado. Saldo actual: {nuevo_saldo:.2f}")

        elif opcion == "3":
            print(f"💰 Saldo actual: {account.get_balance():.2f}")

        elif opcion == "4":
            print("Historial de transacciones:")
            if not account.get_transactions():
                print("No hay transacciones aún.")
            else:
                for t in account.get_transactions():
                    print("-", t)

        elif opcion == "5":
            nuevo_saldo = account.apply_interest()
            print(f"Interés aplicado. Saldo actual: {nuevo_saldo:.2f}")

        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

    except ValueError as e:
        print("Error:", e)
