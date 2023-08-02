'''
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

Given:
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]




def add_lists(firstlist, secondlist):
    newlist = []
    for num in firstlist:
        if num % 2==1:
            newlist.append(num)
    for numb in secondlist:
        if numb % 2==0:
            newlist.append(numb)
    print(newlist)
add_lists(list1, list2)    
            
                     