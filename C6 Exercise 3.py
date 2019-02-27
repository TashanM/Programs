# Exercise 3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 30 October 2017
# Mr. Veera

investment = 2500
investment_rate = 0.075
final_amount = 5000
t = 1

while ((investment*(1 + investment_rate)**t) <= final_amount):
    t+=1

print ('It will take %i year(s) to get $5000.' %(t))
