import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
sql = """
    INSERT INTO employees(id, name, department, phone, email) VALUES (1, "John Smith", "IT", "+55555", "js@x.com");
    INSERT INTO employees VALUES(2, "Anne Barker", "Accounting", "0.40404040", "a@x.com");
    INSERT INTO employees VALUES(3, "Antony Romano", "Sales", "+1494944", "ar@x.com");

"""
cursor.executescript(sql)

connection.commit()
connection.close()