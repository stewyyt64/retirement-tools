# Title:	401k Distribution Calculator
# Author:	Mark Larkin
# Language:	Python
# Version:	1.0
# Created:	3/30/18
# Description:
# 	This program provides 401k-related calculations based on the user's input of:
#	Current Age
#	Retirement Age
#	Salary
#	Contribution rate (and match)
#	Current 401k balance
#	Expected return rate

# Clear screen and display header text
import os
os.system("clear")
print('\n401k Distribution Calculator')
print('\nThe calculator gives you an estimate of your break-even annual and monthly distribution.')
print('(The break-even distribution is the amount you could withdraw annually in perpetuity.)')
print('\nNote: calculations assumes a 2.5% annual salary increase\n')

# Get input from user and store in variables
age = int(input('Current age: '))
rage = int(input('Expected retirement age: '))
sal = float(input('Current annual salary: '))
pers = int(input('Personal 401k contribution percent (1 - 15): '))
match = int(input('Company match percent (typically between 3 - 6): '))
balance = float(input('Current 401k balance: '))
rate = float(input('Expected annual return rate (example: 6.5): '))

# Calculate years, total contribution rate, and contribution amount
if match > pers:
	new_match = pers
	crate = float(pers + new_match)/100
else:
	crate = float(pers + match)/100

yrs = int(rage - age)
contrib = float(sal * crate)
ctr = int(age)

# Loop through calculations for every year between current age and retirement age
for i in range(0, yrs):
    sal = sal * 1.025
    contrib = float(sal * crate)
    balance = balance + contrib
    total = (balance * (1 + (rate/100)))
    balance = total
    ctr = ctr + 1

# Display results
print('--------------------------------------------------\n')
print('You have',yrs, 'years until age',rage)
print('\nSalary at age ' + str(ctr) + ' = ${:,.2f}'.format(sal))
print('401k balance at age ' + str(ctr) + ' = ${:,.2f}\n'.format(total))
distro = float(total * (rate/100))
ndistro = float(distro * .65)
ndistromonth = float(ndistro / 12)
print('Annual PRE-TAX distribution at ' + str(rate) + '% = ${:,.2f}\n'.format(distro))
print('Annual AFTER-TAX distribution = ${:,.2f}\n'.format(ndistro))
print('Monthly AFTER-TAX distribution = ${:,.2f}\n'.format(ndistromonth))
