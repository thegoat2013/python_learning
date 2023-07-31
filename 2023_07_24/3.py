'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
'''

z=("Emma is good developer. Emma is a writer")
def countSubString(whole_string, sub_string):
    #write code here
    count=0
    index=0
    last=len(sub_string)
    for num in whole_string:
        x=whole_string[index:index + last]
        index=index+1
        if x == sub_string:
            count=count+1
            
    print(count)
countSubString(z, "Emma")     
    
    
        
        
        
       
            