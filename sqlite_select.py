import sqlite3
connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

sql = 'select * from employees where name like "A%" order by id desc'

cursor.execute(sql)

for row in cursor.fetchall():
    print(row)

# ty = cursor.fetchone()
# print("only single line", ty)

# id = input('Enter an ID:')

sql = 'SELECT * FROM employees WHERE id=?'

# cursor.execute(sql, (id,))

record = (10, 'Leonardo Amaro', 'Marketing', '+411111', 'la@x.it')
sql = 'INSERT INTO employees VALUES(?, ?, ?, ?, ?)'
cursor.execute(sql, record)


connection.close()