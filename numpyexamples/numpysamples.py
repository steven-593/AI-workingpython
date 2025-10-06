import numpy as np # type: ignore

# a=np.array([1,2,3,4])
# print(type(a))
# print(a.shape)
# print(a[2])
# a[0]=100
# a[1]+=1000
# a[2]-=1000
# print(a)
# arreglo en 2 dimensiones
b = np.array([[1,2,3,4],[5,6,7,8]]) 
print(type(b))
print(b.shape)  
print(b)

print(b[1,1])

b[1,2]+=100

print(b)



a=np.zeros((4,5))
print(a)
print(a.shape)



b=np.ones((3,4))
print(b)

c=np.eye(4)
print(c)


d=np.full((5,5),8)
print(d)


e = np.random.random((3,3))
print(e)



print('-------------------------------------------------------------------------------------------------------')

# crear una matriz aleatoria de 3 x 4 de numeros enteros 

f = np.random.randint(0, 10, size=(3,4))

print(f)


f = np.random.choice([1,10],size=(3,4))
print(f)


g = np.random.randint(1, 10, (3,4))
print(g)

submatrixg = g[0:2, 1:3]
print("Submatriz:\n", submatrixg)


h = np.random.randint(11, 100, (5,4))
print("Matriz original (h):\n", h)

sub1 = h[0:2,0:2]     # filas 0 y 1, todas las columnas
sub2 = h[1:3,1:3]     # filas 2 a 4, todas las columnas
print("Submatriz 1:\n", sub1)
print("Submatriz 2:\n", sub2)

print('---------------------------------------------------------------------------------------')
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)

filter=(a>2)
print(filter)
print(a[filter])

print('---------------------------------------------------------------------------------')
# 1. Crear un arreglo 7x7 con valores fijos del 0 al 100
arr = np.array([
    [10, 20, 30, 40, 50, 60, 70],
    [5, 15, 25, 35, 45, 55, 65],
    [0, 12, 24, 36, 48, 60, 72],
    [3, 13, 23, 33, 43, 53, 63],
    [7, 17, 27, 37, 47, 57, 67],
    [9, 19, 29, 39, 49, 59, 69],
    [2, 14, 26, 38, 50, 62, 74]
])
print("Matriz original:\n", arr)
print("Forma:", arr.shape)
# 2. Crear la máscara para valores entre 40 y 60
mask = (arr >= 40) & (arr <= 60)
print("\nMáscara booleana:\n", mask)
# 3. Aplicar la máscara para obtener los valores filtrados
filtrados = arr[mask]
print("\nValores filtrados (entre 40 y 60):\n", filtrados)


print('--------------------------------------------------------------------------------------------------')

x=np.array([[1,2],[3,4]])
y=np.array([[10,23],[20,40]])
print(x)
print(y)
print(x.shape)
print(y.shape)

print(x+y)
print(np.add(x,y))



print(x*y)


print(np.dot(x,y))

h = np.random.randint(11, 100,(3,4))
print(h)

print(np.sum(h,axis=0))

print(np.sum(h,axis=1))

print(np.sum(g))

print('----------------------------------------------------------------------------------------')
x=np.array([[1,2],[3,4]])
y=np.array([[10,23],[20,40]])

print(x)
print(x.T)

print('----------------------------------------------------------------------------------------')
horizantal= np.concatenate((x,y), axis=1)
print('Concatenacion Horizontal:')
print(horizantal)
print(horizantal.shape)
print('----------------------------------------------------------------------------------------')
Vertical= np.concatenate((x,y), axis=0)
print('Concatenacion Horizontal:')
print(Vertical)
print(Vertical.shape)

print('----------------------------------------------------------------------------------------')
c=np.concatenate((x,y),axis=0)
print(c.shape)
