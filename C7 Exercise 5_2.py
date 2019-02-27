# Exercise 5_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 December 2017
# Mr. Veera

def getDollarAmount(quarters, dimes, nickels, pennies):
    quarteramount = quarters*0.25
    dimeamount = dimes*0.1
    nickelamount = nickels*0.05
    pennyamount = pennies*0.01

    total = quarteramount + dimeamount + nickelamount + pennyamount

    return total

print ('Enter your total coins:')
print ()
quarters = int(input('Quarters: '))
dimes = int(input('Dimes: '))
nickels = int(input('Nickels: '))
pennies = int(input('Pennies: '))
print ()

amount = getDollarAmount(quarters, dimes, nickels, pennies)

print ('Total: $%.2f' %(amount))
