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
count=1
for num in range(0,5):
    print("*" * count)
    count=count+1
count=count-2    
for num in range(0,4):
    print("*" * count)
    count=count-1

    
    