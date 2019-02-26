#!/usr/local/bin/python3

import pandas as pd
import numpy as np

my_dict = {
     'name' : ["a", "b", "c", "d", "e","f", "g"],
     'age' : [20,27, 35, 55, 18, 21, 35],
     'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]
}

# print (len(my_dict['name']))
#df = pd.DataFrame(my_dict, index = [x for x in range(1, len(my_dict['name']), 1)])
# df = pd.DataFrame(my_dict, index = [1, 2, 3, 4, 5, 6, 7])

df = pd.DataFrame(my_dict)
# df.set_index("name")
# print (df.set_index("name"))
print (df.set_index(["name", "age"]))

# print (df.dtypes)
# print (df.head()) # Prints 1st 5 rows
# print (df.tail()) # Prints last 5 rows

# print (df.head(2)) # Prints 1st 2 rows
# print (df.tail(1)) # Prints last row


# np_arr = np.array([10,20,30,40,50,60,70])
# df1 = pd.DataFrame(my_dict, index=np_arr)
#
# print (df1)