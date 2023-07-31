'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
def patterns (rows):
    rows=rows+1
    iterate=1
    while iterate<rows:
        print(str(iterate) * iterate)
        iterate=iterate+1
    
            
patterns(10)                