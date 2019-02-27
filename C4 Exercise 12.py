# Exercise 12
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 4 October 2017
# Mr. Veera

print ('Enter the number of time spent on each of the following project tasks:')
print (' ')
designing = int(input('Designing:'))
coding = int(input('Coding:'))
debugging = int(input('Debugging:'))
testing = int(input('Testing:'))

total = designing + coding + debugging + testing

designingpercent = (designing/total)*100
codingpercent = (coding/total)*100
debuggingpercent = (debugging/total)*100
testingpercent = (testing/total)*100

print (' ')
print ('%-12s%15s%-3s' %('Task', ' ', '% Time'))
print ('%-12s%15s%-3s%%' %('Designing', ' ', '%.2f' %(designingpercent)))
print ('%-12s%15s%-3s%%' %('Coding', ' ', '%.2f' %(codingpercent)))
print ('%-12s%15s%-3s%%' %('Debugging', ' ', '%.2f' %(debuggingpercent)))
print ('%-12s%15s%-3s%%' %('Testing', ' ', '%.2f' %(testingpercent)))
