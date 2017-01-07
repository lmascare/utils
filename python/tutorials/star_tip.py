#!/usr/bin/env python3

record = ('Dave', 'dave@example.com', '732-555-1212', '908-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

records = [
        ('foo',1,2),
        ('bar','hello'),
        ('foo',3,4),
        ]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

