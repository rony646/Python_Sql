import sqlite3

db_connection = sqlite3.connect("database.db")

cursor = db_connection.cursor()


def create_table():
    # Creating the employees table
    sql_create = 'create table employees'\
                '(matricula varchar(8) primary key, '\
                'role TEXT, ' \
                'name TEXT, '\
                'age INTEGER, ' \
                'wage float)'
    cursor.execute(sql_create)


create_table()

db_connection.commit()
db_connection.close()
