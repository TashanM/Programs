# Exercise 13
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 October 2017
# Mr. Veera

print ('Enter the amount spent last month on the following items:')
print (' ')
food = float(input('Food: $'))
clothing = float(input('Clothing: $'))
entertainment = float(input('Entertainment: $'))
rent = float(input('Rent: $'))

total = food + clothing + entertainment + rent

foodpercent = (food/total)*100
clothingpercent = (clothing/total)*100
entertainmentpercent = (entertainment/total)*100
rentpercent = (rent/total)*100

print (' ')
print ('%-12s%15s%-3s' %('Category', ' ', 'Budget'))
print ('%-12s%15s%-3s%%' %('Food', ' ', '%.2f' %(foodpercent)))
print ('%-12s%15s%-3s%%' %('Clothing', ' ', '%.2f' %(clothingpercent)))
print ('%-12s%14s%-3s%%' %('Entertainment', ' ', '%.2f' %(entertainmentpercent)))
print ('%-12s%15s%-3s%%' %('Rent', ' ', '%.2f' %(rentpercent)))
