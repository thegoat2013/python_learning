'''
Write a Python program to check if value 200 exists in the following dictionary.

Given:
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
'''
Expected output:
200 present in a dict
'''
for value in sample_dict.values():
    if value==200:
        print("200 exists")
        break