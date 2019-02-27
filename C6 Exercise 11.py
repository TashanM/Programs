# Exercise 11
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 November 2017
# Mr. Veera

hour = int(input('Enter the starting hour: '))
time_of_day = input('Enter am or pm: ')
elapsed = int(input('Enter the number of elapsed hours: '))

time = hour + elapsed

if (time > 24):
    while (time > 12):
        time = time - 12
        if (time_of_day == 'am'):
            time_of_day = 'pm'
        else:
            time_of_day = 'am'
    print ('The time is: %i:00 %s' %(time, time_of_day))
    
elif (time > 12):
    time = time - 12
    if (time_of_day == 'am'):
        time_of_day = 'pm'
    else:
        time_of_day = 'am'
    print ('The time is: %i:00 %s' %(time, time_of_day))

else:
    print ('The time is: %i:00 %s' %(time, time_of_day))



##hour = int(input('Enter the starting hour: '))
##time_of_day = input('Enter am or pm: ')
##elapsed = int(input('Enter the number of elapsed hours: '))
##
##if (time_of_day == 'pm'):
##    hour+=12
##
##ampm = time_of_day
##time = hour + elapsed
##
##while (time > 24):
##    time-=12
##    
##    if (ampm == 'am'):
##        ampm = 'pm'
##    else:
##        ampm = 'am'
##
##time-=12
##
##if (elapsed == 12 and time_of_day == 'am'):
##    ampm = 'pm'
##
##print ('The time is: %i:00 %s' %(time, ampm))
