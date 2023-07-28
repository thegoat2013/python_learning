'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
'''
import re
z=("Emma is good developer. Emma is a writer", "Emma")
def countSubString(whole_string, sub_string):
    #write code here
    