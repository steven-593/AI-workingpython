class Account:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.balance += amount
        self.transactions.append(f"Depósito: +{amount}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes.")
        self.balance -= amount
        self.transactions.append(f"Retiro: -{amount}")
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions

account = Account()

while True:
    print("\nMenú:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Mostrar transacciones")
    print("5. Salir")
    
    choice = input("Elige una opción: ")
    
    if choice == '1':
        try:
            amount = float(input("Cantidad a depositar: "))
            new_balance = account.deposit(amount)
            print(f"Depósito exitoso. Saldo actual: {new_balance}")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif choice == '2':
        try:
            amount = float(input("Cantidad a retirar: "))
            new_balance = account.withdraw(amount)
            print(f"Retiro exitoso. Saldo actual: {new_balance}")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif choice == '3':
        print(f"Saldo actual: {account.get_balance()}")
    
    elif choice == '4':
        trans = account.get_transactions()
        if not trans:
            print("No hay transacciones.")
        else:
            print("Historial de transacciones:")
            for t in trans:
                print(t)
    
    elif choice == '5':
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")