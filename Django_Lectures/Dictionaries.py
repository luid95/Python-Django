#Dictionaries
my_stuff = {"key1": "value1", 'key2': 'value2'}
print(my_stuff['key2'])

dicc = {"key1": 123, 'key2': 'value2', "key3": {'123':[1,2,'grabMe']}}
print(dicc)
print(dicc ['key3']['123'][2])
print(dicc ['key3']['123'][2].upper())

#Example 2
stuff = {'lunch': 'pizza', 'bfast': 'egss'}
print(stuff['lunch'])
stuff['lunch'] = 'burger'
stuff['dinner'] = 'pasta'
print(stuff)
