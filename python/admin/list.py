#!/usr/bin/python

list1 = ['1', '2', '3', '5', '7']

list2 = ['2', '4', '6', '8']

s = set(list2)

diff1 = [x for x in list1 if x not in s]
print diff1

diff2 = list(set(list2) - set(list1))

print diff2


