"""
Python Maps also called ChainMap is a type of data structure to manage
multiple dictionaries together as one unit.
Creating a ChainMap
We create two dictionaries and club them using the ChainMap method from
the collections library. Then we print the keys and values of the result of
the combination of the dictionaries. If there are duplicate keys, then only the
value from the first key is preserved.
"""

import collections
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

# Club both the dictionary using ChainMap
res = collections.ChainMap(dict1, dict2)

# Create a single dictionary
print(res.maps, "\n")
print('Keys:\t\t{}'.format(list(res.keys())))
print('Values:\t\t{}'.format(list(res.values())))
# Or
# Print all values from res
for key, value in res.items():
    print('Key: {}\tValue: {}'.format(key, value))

# Updating Map
dict2['day4'] = 'Sat'
print(res.maps, "\n")
