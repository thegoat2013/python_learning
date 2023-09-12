def number(source):
    output=0
    for num in range(1,source):
        for digit in range(1,num):
            if num%digit==0:
                pass
            output=output+num
    print(output)
number (10)
