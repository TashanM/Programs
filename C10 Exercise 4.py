# Exercise 4
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 15 January 2017
# Mr. Veera

number = []

to5 = ''
to10 = ''
to15 = ''
to20 = ''
to25 = ''
to30 = ''
to35 = ''
to40 = ''
to45 = ''
to50 = ''

nums = int(input('Enter a number between 1 and 50: '))

while (nums != -1):
    number.append(nums)
    nums = int(input('Enter a number between 1 and 50: '))

average = sum(number) / len(number)
maximum = max(number)
mmrange = max(number) - min(number)

for histogram in number:
    if (histogram >= 1 and histogram <= 5):
        to5+='*'
        
    if (histogram >= 6 and histogram <= 10):
        to10+='*'
        
    if (histogram >= 11 and histogram <= 15):
        to15+='*'
        
    if (histogram >= 16 and histogram <= 20):
        to20+='*'
        
    if (histogram >= 21 and histogram <= 25):
        to25+='*'
        
    if (histogram >= 26 and histogram <= 30):
        to30+='*'
        
    if (histogram >= 31 and histogram <= 35):
        to35+='*'
        
    if (histogram >= 36 and histogram <= 40):
        to40+='*'
        
    if (histogram >= 41 and histogram <= 45):
        to45+='*'
        
    if (histogram >= 46 and histogram <= 50):
        to50+='*'

print ()
print ('Average: %i' %(average))
print ('Maximum: %i' %(maximum))
print ('Range: %i' %(mmrange))
print ()
print (' 1 -  5 :  %s' %(to5))
print (' 6 - 10 :  %s' %(to10))
print ('11 - 15 :  %s' %(to15))
print ('16 - 20 :  %s' %(to20))
print ('21 - 25 :  %s' %(to25))
print ('26 - 30 :  %s' %(to30))
print ('31 - 35 :  %s' %(to35))
print ('36 - 40 :  %s' %(to40))
print ('41 - 45 :  %s' %(to45))
print ('46 - 50 :  %s' %(to50))
