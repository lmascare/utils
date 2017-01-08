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

dev_1 = Developer('Corey','Shafer',50000, 'Python')
dev_2 = Developer('Test','User',60000, 'Java')

dev_1.apply_raise()
dev_2.apply_raise()
print(dev_1.email, dev_1.prog_lang, dev_1.pay)
print(dev_2.email, dev_2.prog_lang, dev_2.pay)

