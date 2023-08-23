'''
Exercise 2: Merge two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
dict3={}
for key, value in dict1.items():
    dict3[key] = value
for key, value in dict2.items():
    dict3[key] = value
print(dict3)    