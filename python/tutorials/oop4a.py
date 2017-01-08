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
    pass

dev_1 = Developer('Corey','Shafer',50000)
dev_2 = Developer('Test','User',60000)

print(dev_1.email)
print(dev_2.pay)

# print(help(Developer))

