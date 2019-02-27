# Exercise 10
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 3 October 2017
# Mr. Veera

print ('Enter your birthdate:')
byear = int(input('Year:'))
bmonth = int(input('Month:'))
bday = int(input('Day:'))

print ("Enter today's date:")
tyear = int(input('Year:'))
tmonth = int(input('Month:'))
tday = int(input('Day:'))

totalyears = tyear - byear
totalmonths = tmonth - bmonth
totaldays = tday - bday
daycalculator = (totalyears*365) + (totalmonths*30) + totaldays

sleep = daycalculator*8

print ('You have been alive for %i days.' %(daycalculator))
print ('You have slept %i hours.' %(sleep))
