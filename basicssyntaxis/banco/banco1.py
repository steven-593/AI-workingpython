balance = 1000
transactions = []

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
            if amount <= 0:
                print("Error: La cantidad debe ser positiva.")
            else:
                balance += amount
                transactions.append(f"Depósito: +{amount}")
                print(f"Depósito exitoso. Saldo actual: {balance}")
        except ValueError:
            print("Error: Entrada inválida. Debe ser un número.")
    
    elif choice == '2':
        try:
            amount = float(input("Cantidad a retirar: "))
            if amount <= 0:
                print("Error: La cantidad debe ser positiva.")
            elif amount > balance:
                print("Error: Fondos insuficientes.")
            else:
                balance -= amount
                transactions.append(f"Retiro: -{amount}")
                print(f"Retiro exitoso. Saldo actual: {balance}")
        except ValueError:
            print("Error: Entrada inválida. Debe ser un número.")
    
    elif choice == '3':
        print(f"Saldo actual: {balance}")
    
    elif choice == '4':
        if not transactions:
            print("No hay transacciones.")
        else:
            print("Historial de transacciones:")
            for trans in transactions:
                print(trans)
    
    elif choice == '5':
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")