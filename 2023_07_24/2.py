'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
def patterns (rows):
    count=1
    times=1
    numb=1
    for num in range(0,rows):
        print(str(numb) * count)
        count=count+1
        numb=numb+1
    
            
patterns(5)                