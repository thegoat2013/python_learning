'''
Exercise 6: Delete a list of keys from a dictionary
Given:
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
'''
# Keys to remove
keys = ["name", "salary"]
Expected output:

{'city': 'New york', 'age': 25}
'''
keys=[]
for key in sample_dict.keys():
    if key=="name" or key=="salary":
        keys.append(key)
for key in keys:
    sample_dict.pop(key)
print(sample_dict)