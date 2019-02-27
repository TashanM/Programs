# Strings Test 2_5
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 28 November 2017
# Mr. Veera

text = input('Enter text: ')

position = 0
happyc = 0
sadc = 0

while (position <= len(text)):
    happy = text.find(':-)', position)
    sad = text.find(':-(', position)
    if (happy != 0):
        happyc+=1
    elif(sad != 0):
        sadc+=1

    happy = 0
    sad = 0
    position+=1

if (happyc == 0 and sadc == 0):
    print ('None')
elif (happyc == sadc):
    print ('Unsure')
elif (happyc > sadc):
    print ('Happy')
else:
    print ('Sad')

print (happyc)
print (sadc)
