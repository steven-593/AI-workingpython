
# while True:

#     number= int(input('Enter a number, please. \n'))
#     if number % 2==0:
#         print(f'The number {number} entered is even')
#     else:
#         print(f'The number {number} entered is odd')

# userDefault='admin'
# passworDefault=1234
# user=input(f'Enter the user of the account. \n')
# pasword=input('enter the password of the account')

# if user == userDefault and pasword==passworDefault:
#     print('You are allowed to come to the system')
# else:
#     print('You are bot user of the system....')

# crear una lista de numeros que realice la suma de todos los numeros 

# repository=list()
# ramdonNumber = int(input('Enter a number please '))
# sum=0
# for i in range (ramdonNumber):
#     repository.append(i)
# for i in repository:
#     sum=sum+i

# print(f'the total sum is {sum}')

# realizar un ejercico de un sistema bancario en donde el usuario pueda agregar dinero y pueda visualizar el dinero y realizar retiro
print('--------------------------------------------------')
# balance = 1000
# while True:
#     print("\nMenu:")
#     print("1 > Deposit")
#     print("2 > Withdraw")
#     print("3 > Check balance")
#     print("4 > Exit")
#     try:
#         choice = int(input("Enter your choice: "))
#     except ValueError:
#         print("Please enter a valid number.")
#         continue
#     if choice == 1:
#         try:
#             money = int(input("Enter the amount to deposit: "))
#             balance += money
#             print(f"Deposited ${money}. New balance: ${balance}")
#         except ValueError:
#             print("Invalid amount. Please enter a number.")
#     elif choice == 2:
#         try:
#             money = int(input("Enter the amount to withdraw: "))
#             if balance >= money:
#                 balance -= money
#                 print(f"Please take your money. Remaining balance: ${balance}")
#             else:
#                 print("Insufficient funds.")
#         except ValueError:
#             print("Invalid amount. Please enter a number.")
#     elif choice == 3:
#         print(f"Your current balance is: ${balance}")
#     elif choice == 4:
#         print("Thank you for using our service. Goodbye!")
#         break
#     else:
#         print("Your choice is not allowed. Try again.")


# class Students:
#     def __init__(self, name,course='AI'):
#         print('the student has been registered...')
#         self.name=name
#         self.course=course
#     def dateStudents(self):
#         print(f'Name: {self.name} and Course: {self.course}')
#         return

# stedent1=Students('Steven')
# student2=Students('Marta', 'Distributed systems')

# stedent1.dateStudents()
# student2.dateStudents()

# class Students:
#     def __init__(self, name,course='AI'):
#         print('the student has been registered...')
#         self.name=name
#         self.course=course
#     def dateStudents(self, status='No active'):
#         print(f'Name: {self.name} and Course: {self.course}')
#         return

# stedent1=Students('Steven')
# student2=Students('Marta', 'Distributed systems')

# stedent1.dateStudents('No active')
# student2.dateStudents('Active')

print('--------------------------------------------------')
balance = 1000
while True:
    print("\nMenu:")
    print("1 > Deposit")
    print("2 > Withdraw")
    print("3 > Check balance")
    print("4 > Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        try:
            money = int(input("Enter the amount to deposit: "))
            balance += money
            print(f"Deposited ${money}. New balance: ${balance}")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == 2:
        try:
            money = int(input("Enter the amount to withdraw: "))
            if balance >= money:
                balance -= money
                print(f"Please take your money. Remaining balance: ${balance}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == 3:
        print(f"Your current balance is: ${balance}")
    elif choice == 4:
        print("Thank you for using our service. Goodbye!")
        break
    else:
        print("Your choice is not allowed. Try again.")


