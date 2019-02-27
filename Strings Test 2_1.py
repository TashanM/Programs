# Strings Test 2_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 27 November 2017
# Mr. Veera

lower = int(input('Enter lower limit of range: '))
upper = int(input('Enter upper limit of range: '))

count = 0
rsa = 0

for num in range (lower, upper+1):
    for divisor in range (1, num+1):
        if (num % divisor == 0):
            count+=1

    if (count == 4):
        rsa+=1

    count = 0
print ('The number of RSA numbers between %i and %i is %i' %(lower, upper, rsa))
