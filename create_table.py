import sqlite3

def create_table():
    # Creating the employees table

    try:
        db_connection = sqlite3.connect("database.db")

        cursor = db_connection.cursor()

        sql_create = 'create table employees'\
                    '(matricula varchar(8) primary key, '\
                    'role TEXT, ' \
                    'name TEXT, '\
                    'age INTEGER, ' \
                    'wage float)'
        cursor.execute(sql_create)

        db_connection.commit()
        db_connection.close()

        print('Table was created sucessfully!')
    except:
        print('Error when creating employees table')