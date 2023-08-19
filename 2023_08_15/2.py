'''
Exercise 11: Reverse a given string
Given:
'''
test = "PYnative"
'''
Expected Output:

evitanYP
'''
def reverse(source):
    output=''
    for index in range(len(source)-1,-1,-1):
        output=output+(source[index])
    print(output)
reverse(test)        