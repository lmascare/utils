#!/usr/bin/python
#
tel = {'jack': 4098, 'sape': 4139}

print(tel['jack'])
print(tel.keys())

for telno in tel:
    print(tel[telno])

for name,tel_no in tel.items():
    print name, "-->", tel_no
