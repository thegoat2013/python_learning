'''
Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
def star (count):
    for num in range(0,count-1):
        print("*" *num )    
    for num in range(count-1,0,-1):
        print("*" *num )        
star(5)
    
    