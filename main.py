from create_table import create_table
from create_employee import create_employee
from fetch_all_employees import fetch_all_employees
from Models import Employee

print('*' * 25)
print(' Employees System ')
print('*' * 25)

def show_options():
    print('\nChoose an option: \n')
    print('1 - Regiser a new employee')
    print('2 - Show all employees registered')

def main():
    user_option = None

    show_options()
    user_option = int(input('\nType an option: '))
    
    if user_option == 1:
        create_employee()
    elif user_option == 2:
        fetch_all_employees()
    else:
        user_option = int(input('Type an option: '))

if __name__ == '__main__':
    main()