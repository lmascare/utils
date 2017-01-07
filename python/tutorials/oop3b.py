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

emp_1 = Employee('Corey','Shaffer',50000)
emp_2 = Employee('Test','User',60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email, new_emp_1.pay)
