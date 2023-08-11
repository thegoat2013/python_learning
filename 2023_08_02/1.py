'''
Exercise 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.

'''

def tax (salary):
    tax=0
    if salary <= 10000:
        tax=0
    elif salary > 10000:    
        salary=salary-10000
        tax=salary*0.1
    elif salary > 20000:
        salary=salary-20000
        tax=salary*0.2
    elif salary > 300000:
        salary=salary-30000
        tax=salary*0.3        
        tax=10000*0.1 + tax
    print(tax)    
    
    
    
tax(21000)

