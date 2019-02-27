# Exercise 16
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 9 October 2017
# Mr. Veera

awbrey = int(input('Enter the votes of Awbrey:'))
martinez = int(input('Enter the votes of Martinez:'))

total = awbrey + martinez
awbreypercent = (awbrey/total)*100
martinezpercent = (martinez/total)*100

print (' ')
print ('%-12s%10s%13s' %('Candidate', 'Votes', 'Percentage'))
print ('%-12s%10s%10s%%' %('Awbrey', awbrey, '%.2f' %(awbreypercent)))
print ('%-12s%10s%10s%%' %('Martinez', martinez, '%.2f' %(martinezpercent)))
print (' ')
print ('TOTAL VOTES: %i' %(total))
