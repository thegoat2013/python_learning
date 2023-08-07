'''
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
def pattern (start):
    for num in range(start, 0,-1):
        result=''        
        for numb in range(num, 0,-1):
            result=result+' ' + str(numb)
        print(result)
pattern(5)        
           
    
    