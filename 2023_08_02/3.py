'''
check if a number is a prime number
'''
def prime_composite (number):
    for num in range(2,number//2+1):
        if number%num==0:
            return False
    return number > 1
#x=(prime_composite (48))
#print(x)
def add_prime (source):
    output=0
    for num in range(1,source+1):
        z=(prime_composite (num))
        if z==True:
            output=num+output
        pass
    return output
a=(add_prime (10))
print(a)
