# Title:	401k Life 
# Author:	Mark Larkin
# Language:	Python
# Version:	1.0
# Created:	3/31/18
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
print('\n401k Life')
print('\nThis calculator gives you an estimate of how long your 401k will last you in retirement.\n')

# Get input from user and store in variables
rage = int(input('Expected retirement age: '))
balance = float(input('Estimated 401k balance at retirement: '))
rate = float(input('Expected annual return rate (example: 6.5): '))
nwithdraw = float(input('Desired monthly amount needed (after tax) in retirement: '))

# Calculate gross annual distribution based on net monthly amount input 
ctr = int(rage)
gwithdraw = float((nwithdraw / .65) * 12)

# Loop through calculations for every year between current age and retirement age
while (balance > gwithdraw):
    balance = ((balance - gwithdraw) * (1 + (rate/100)))
    ctr = ctr + 1
    

# Display results
#print('--------------------------------------------------\n')
print('\nThe gross annual withdrawal would be ${:,.2f}\n'.format(gwithdraw))
print('At age ' + str(ctr) + ' your 401k balance = ${:,.2f}\n'.format(balance))

