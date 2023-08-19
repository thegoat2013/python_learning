'''
Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Given:

# number of terms
n = 5
Expected output:
24690
'''
def terms (number, terms):
    term_number=number
    total=number
    for num in range(1,terms):
        term_number=term_number*10+number
        total=total+term_number
        
        
    print(total)
terms(2,2)    
        
    