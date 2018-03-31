import os
os.system("clear")
print('\n401k Growth Calculator\n')

age = int(input('Current age: '))
sal = float(input('Current salary: '))

pers = int(input('401k contribution percent (ex. 6): '))
match = int(input('Company match percent (ex. 6): '))
amount = float(input('Current balance: '))
rate = float(input('Expected return rate: '))
yrs = int(60 - age)
crate = float(pers + match)/100
contrib = float(sal * crate)
ctr = age

print('\n')

for i in range(0, yrs):
    #print '\n', yrs, 'years until age 59'
    total = (amount * pow(1 + (rate/100), i))
    print('Salary at age ' + str(ctr) + ' = ${:,.2f}'.format(sal))
    print('Contrib at age ' + str(ctr) + ' = ${:,.2f}'.format(contrib))
    print('401k balance at age ' + str(ctr) + ' = ${:,.2f}\n'.format(total))
    sal = sal * 1.03
    contrib = float(sal * crate)
    amount = amount + contrib
    ctr = ctr + 1
