# Exercise 5_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 4 December 2017
# Mr. Veera

def getDollarAmount(quarters, dimes, nickels, pennies):
    quarteramount = quarters*0.25
    dimeamount = dimes*0.1
    nickelamount = nickels*0.05
    pennyamount = pennies*0.01

    total = quarteramount + dimeamount + nickelamount + pennyamount

    print ('Total: $%.2f' %(total))

print ('Enter your total coins:')
print ()
quarters = int(input('Quarters: '))
dimes = int(input('Dimes: '))
nickels = int(input('Nickels: '))
pennies = int(input('Pennies: '))
print ()

getDollarAmount(quarters, dimes, nickels, pennies)
