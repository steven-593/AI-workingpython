# Dictionary
print('Dictionary1')

mydictionary = dict()
mydictionary['humans'] = 2
mydictionary['mouse'] = 4
mydictionary['spider'] = 8

for animal in mydictionary:
    data = mydictionary[animal]
    print(f'the {animal} has {data} legs')
# # LOOPS
#     counter=0
#     while counter<10:
#         print(counter)
#         counter+=1
# name=input('Enter your name: ')
# print(f'Hello, {name}' )

print('-----------------------------------------------------------------------------------------------------------')

myList=list()
for i in range(100):
    if i%2==0:
        myList.append(i)
print(myList)

print('-----------------------------------------------------------------------------')
myList=[ i for i in range(10) if i%2==0]
print(myList)

print('ok....')

print ('---------------------------------------------------------------------------------')
myList=[i*i for i in range(100)]
print(myList)

# funciones 

def greetings():
    return f'Hello my friend'

tmp=greetings()
print(tmp)

# crear una lista con numeros con 10 elementos en la lista guardar numeros que consideremos del 1 al 20  crear una metodo que detecte el numero mAXIMO 


number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newnumber = [12,34,56,76,45,34,29,58,23,45,90,91,95,42,77,99,14,7,5,2]

for num in number:
    k = 0
    for new_num in newnumber:
        if num > new_num:
            k += 1
    
    # Si num es mayor que TODOS los elementos de newnumber
    if k == len(newnumber):
        print(num)


def greeting2(name='Camilo'):
    print(f'Hello, {name}')
    return
greeting2()


print("----------------------------------------------------------------------------------------------------------------")
print('CALCULADORA DE PRUEBA')
print('=====================')
# Bucle que repite la calculadora
while True:
    print('\n--- NUEVA OPERACIÓN ---')
    # Pedir el primer número
    numero1 = float(input('Ingresa el primer número: '))
    # Pedir la operación
    print('\n¿Qué operación quieres hacer?')
    print('1 = Suma')
    print('2 = Resta')
    print('3 = Multiplicación')
    print('4 = División')
    operacion = input('\nElige una operación (1, 2, 3 o 4): ')
    # Pedir el segundo número
    numero2 = float(input('Ingresa el segundo número: '))
    # Hacer el cálculo según la operación elegida
    if operacion == '1':
        resultado = numero1 + numero2
        print(f'\nResultado: {numero1} + {numero2} = {resultado}')
    elif operacion == '2':
        resultado = numero1 - numero2
        print(f'\nResultado: {numero1} - {numero2} = {resultado}')
    elif operacion == '3':
        resultado = numero1 * numero2
        print(f'\nResultado: {numero1} × {numero2} = {resultado}')
    elif operacion == '4':
        if numero2 == 0:
            print('\nError: No se puede dividir por cero')
        else:
            resultado = numero1 / numero2
            print(f'\nResultado: {numero1} ÷ {numero2} = {resultado}')
    else:
        print('\nOperación no válida')
    # Preguntar si quiere hacer otra operación
    continuar = input('\n¿Quieres hacer otra operación? (s/n): ')
    if continuar.lower() != 's':
        print('\n¡Gracias por usar la calculadora!')
        break

