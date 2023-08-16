'''
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:
'''
str1 = "PYnative29@#8496"
'''
Expected Outcome:


Sum is: 38 and Average is  6.333333333333333
'''
total=0
for num in range(0,len(str1)):
    if isinstance(num, int):
        total=total+num
    else:
        continue
print(total)       