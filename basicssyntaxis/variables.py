a = 12
b = 4.6
name = "Steven"

is_active= True

print (a,b,name, is_active)

print (type(a))
print (type(name))
print (type(is_active))

device='router'
id=101

print(f'Device: {device} and ID: {id}')

# Operaciones aritmeticas

numeroa =2
numerob =3

result= numeroa+numerob

print('La suma es: {result}')

print ("El resultado de la suma es: ", numeroa+numerob)
print ("El resultado de la resta es: ", numeroa-numerob)
print ("El resultado de la multiplicacion es: ", numeroa*numerob)
print ("El resultado de la multiplicacion es: ", numeroa**numerob)
print ("El resultado de la division es: ", numeroa/numerob)
print ("El resultado de la division es: ", numeroa//numerob)

# String

print ("String")
name= "steven cedeno"
print (name.upper())
print (name.capitalize())

name2= name.upper()
print(name2)

print(name2.lower())
language= 'PYTHON'
print(language[0])
print(language[-1])
print(language[-2])
print(len(language))  

# list
print ("# LIST")
devices=['router','switch','cable',56, True,False]
print(len(devices))

# extraer datos

print(devices[0])
print(devices[-1])


devices.append('Server')
print(devices)


#list

names=list()
names.append('steven')
names.append('Camilo')
names.append('Marcos')
names.append('Julian')

print(names)
print('OK')

names[1]= 'Mario'
print(names)

print(names.pop())
print(names)

# list of ten nunmer

numbers = list(range(10))

print(numbers)
selectednumbers=numbers[2:4]

print(selectednumbers)

print(numbers[:-1])

print(numbers[:3])

numbers[2:3]=[100,100]
print (numbers)

# TUPLES
print('TUPLES')
containertuple=(10,20)
containerlist=list(containertuple)
print(type(containertuple))
print(containertuple[0])

#Dictionary
print('Dictionary')

animals=dict()
animals={'dog':'nice','cat':'pretty','monkey':'black','turtle':'small'}

print(animals['cat'])
animals['cat']='purple'
print(animals)

print('Turtle'in animals)

del animals ['monkey']
print(animals)

animals['serpiente']='ugly'
animals['mouse']='liny'
animals['donkey']='big'

for item  in animals:
    feature=animals[item]
    print('%item has %feature'(item,feature))

print(animals)






print('OK!!!')