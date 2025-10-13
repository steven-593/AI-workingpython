import pandas as pd

print('Bienvenido a la primer clase de Pnadas')


serData=pd.Series(data=[10,20,30,40],index=['Carlos', 'Juan', 'Marcos', 'Pablo'])
print(serData)
print(serData.index)
print(serData['Marcos'])
print('Juanita' in serData)

serDate1=serData*2
print(serDate1)

serDate1=serData**2
print(serDate1)

print('------------------------Estructura de datos en 2 dimensiones-------------------------------')

dictionary = {
    'one': pd.Series(data=[1, 2, 3, 4, 5], index=['Carlos', 'Juan', 'Marcos', 'Pablo', 'Luis']),
    'two': pd.Series(data=[6, 7, 8, 9, 10], index=['Carlos', 'Juan', 'Marcos', 'Pablo', 'Luis'])
}

df = pd.DataFrame(dictionary)
print(df)
print(df.index)
print(df.columns)

df['three']=df['one']*df['two']
print(df)

df['filter']=df['three']>45

print(df)

del df['filter']
print(df)


df.insert(1,'copy of one',df ['one'])

print(df)

print('-------------import ssv files -----------------------------------')

movies=pd.read_csv('movies.csv')
# print(movies.head(3))
print(movies.columns)
print(movies.shape)

print('-------------import ssv files -----------------------------------')

ratings=pd.read_csv('ratings.csv')
# print(movies.head(3))
print(ratings.columns)
print(ratings.shape)

print('-------------import ssv files -----------------------------------')

links=pd.read_csv('links.csv')
# print(movies.head(3))
print(links.columns)
print(links.shape)

print('-------------import ssv files -----------------------------------')

tags=pd.read_csv('tags.csv')
# print(movies.head(3))
print(tags.columns)
print(tags.shape)

print(tags.tail(2))
del ratings['timestamp']
del tags['timestamp']

print('Variables de tags:')
print(tags.columns)

print('Variables de ratings:')
print(ratings.columns)
print('----------------------')
print(tags.iloc[0])

print(tags.iloc[[0,22,500]])
print(tags.index)

print('*************************************************************')
print(ratings.head(5))
print('----------------------------------------------')
print(ratings['rating'].describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())

print('*************************************************************')
print(ratings['rating'])
is_highly_rated = ratings['rating'] >= 4
print(ratings[is_highly_rated].head(4))
print(ratings.shape)
print(ratings[is_highly_rated].shape)

print('*************************************************************')
print(movies.columns)
print(movies.head(2))

is_amination=movies['genres'].str.contains('Amination')
print(movies.shape)
print(movies[is_amination].shape)

print('Movies')
print(movies.columns)
print('ratings')
print(ratings.columns)

# relacionar las bases de datos movies y ratings  filtrar 
#las peliculas que sean mayor a 4 pero que sean de animacion

print('Movies')
print(movies.columns)
print('Ratings')
print(ratings.columns)

# 1. Filtrar películas de animación
is_animation = movies['genres'].str.contains('Animation', case=False, na=False)
animation_movies = movies[is_animation]

# 2. Filtrar ratings mayores a 4
high_ratings = ratings[ratings['rating'] > 4]

# 3. Relacionar las dos bases usando movieId
animation_high_rated = pd.merge(animation_movies, high_ratings, on='movieId')

# 4. Mostrar el resultado
print('Películas de animación con rating > 4:')
print(animation_high_rated[['title', 'genres', 'rating']].head())

# Opcional: ver cuántas cumplen la condición
print('Número de películas:', animation_high_rated.shape[0])