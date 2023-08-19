'''
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:
'''
g = "PYnative29@#8496"
'''
Expected Outcome:


Sum is: 38 and Average is  6.333333333333333
'''
total=0
divisor=0
for index  in range(0,len(g)):
    char =(g[index])
    if char.isnumeric():
        total=total+int(char) 
        divisor=divisor+1
print(total)
average=total/divisor
print(average)