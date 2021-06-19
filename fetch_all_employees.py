import sqlite3

def fetch_all_employees():
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        print('-' * 25)
        print('Employee ID: %s\n' % (row[0]))
        print('Role: %s\n' % (row[1]))
        print('Name: %s\n' % (row[2]))
        print('Age: %d\n' % (row[3]))
        print('Wage: %dR$\n' % (row[4]))
    db_connection.close()