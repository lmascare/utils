#!/usr/bin/env python3

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last):
        self.first = first
        self.last  = last 

        self.email = first + '.' + last + '@kellynoah.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
