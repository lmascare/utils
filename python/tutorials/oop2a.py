#!/usr/bin/env python3

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last 
        self.pay   = pay
        self.email = first + '.' + last + '@kellynoah.com'

    def fullname(self):
        return '{} {} {} '.format(self.first,self.last,self.email)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee('Corey','Shaffer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
