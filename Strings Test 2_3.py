# Strings Test 2_3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 28 November 2017
# Mr. Veera

lower = int(input('Enter lower limit of range: '))
upper = int(input('Enter upper limit of range: '))

count = 0
rsa = 0
divisor = 1

for num in range (lower, upper+1):
    while (divisor <= num):
        if (num % divisor == 0):
            count+=1
            
        divisor+=1
        
    if (count == 4):
        rsa+=1

    count = 0
    divisor = 1

print ('The number of RSA numbers between %i and %i is %i' %(lower, upper, rsa))
