import sqlite3

def create_employee():
    #to-do insert new employee into employees table

    employee_id = str(input('\nEnter the employee ID: '))
    role = str(input('Enter the employee role: '))
    name = str(input('Enter the employee name: '))
    age = int(input("What's the age of %s: " % (name)))
    wage = float(input("Enter employee's wage: "))

    try:
        db_connection = sqlite3.connect("database.db")
        cursor = db_connection.cursor()
        cursor.execute('INSERT INTO employees(matricula, role, name, age, wage) VALUES(?, ? , ?, ?, ?)', (employee_id, role, name, age, wage))
        db_connection.commit()
        db_connection.close()
        print('\nEmployee sucessfully registered!')
    except:
        print('\nOh no!, something went wrong with the database.')