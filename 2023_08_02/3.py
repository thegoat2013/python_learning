'''
check if a number is a prime number
'''
def prime_composite (number):
    for num in range(2,number//2-1):
        if number%num==0:
            return False
    return number > 1
x=(prime_composite (48))
print(x)
    