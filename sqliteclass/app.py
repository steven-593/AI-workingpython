import sqlite3
# Creacion y conexion a la base de datos SQLITE

conn=sqlite3.connect('studentuleam.db')

cursor=conn.execute('''CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,
                     name TEXT,
                     age INTEGER)''')
print('STUDENTS DATABASE WAS CREATED SUCCEDDFULLY OR ALREADY CREATED')

conn.commit()


studentsList=[('Marcos',24),('Mario',35), ('Steven',24)]

for name, age in studentsList:
    print(name)
    print(age)
    cursor.execute('INSERT INTO students (name,age) VALUES (?,?)',(name,age))
    conn.commit()
    print('Everthings is working')


cursor.execute('SELECT * FROM students ')

for row in cursor.fetchall():
    print(f'Id: {row[0]},Name: {row[1]}, Age:{row[2]}')

conn.commit()
conn.close()