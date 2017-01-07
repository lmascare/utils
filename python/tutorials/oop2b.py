#!/usr/bin/env python3

class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last 
        self.pay   = pay
        self.email = first + '.' + last + '@kellynoah.com'

    def fullname(self):
        return '{} {} {} '.format(self.first,self.last,self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey','Shaffer',50000)
emp_2 = Employee('Test','User',60000)

emp_1.raise_amount = 1.05
emp_2.raise_amount = 1.07

print(emp_1.pay, emp_1.raise_amount, Employee.raise_amount)
print(emp_1.__dict__)

#print(Employee.__dict__)

print(emp_2.pay, emp_2.raise_amount, Employee.raise_amount)
print(emp_2.__dict__)
