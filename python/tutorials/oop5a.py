#!/usr/bin/env python3

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last 
        self.pay   = pay

        self.email = first + '.' + last + '@kellynoah.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {} {} '.format(self.first,self.last,self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
       cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# Mon = 0, Sun = 6. So workday is between 0 - 4
    @staticmethod
    def is_workday(day):
        if day.weekday() > 4:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('    -->', emp.fullname())

dev_1 = Developer('Corey','Shafer',50000, 'Python')
dev_2 = Developer('Test','User',60000, 'Java')

dev_1.apply_raise()
dev_2.apply_raise()

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(dev_1.email, dev_1.prog_lang, dev_1.pay)
print(dev_2.email, dev_2.prog_lang, dev_2.pay)

print(mgr_1.fullname())
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print("\n")
print(issubclass(Developer, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
