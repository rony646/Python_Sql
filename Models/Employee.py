class Employee:
    def __init__(self, matricula, role, name, age, wage):
        self.matricula = matricula
        self.role = role
        self.name = name
        self.age = age
        self.wage = wage

    def get_employee_info(self):
        print('Name: %s\nRole: %s\nAge: %d\nWage: %d' % (self.name, self.role, self.age, self.wage))

