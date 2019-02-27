# Time Converter
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 29 November 2017
# Mr. Veera

def hours_to_minutes():
    hours = int(input('Enter the number of hours: '))
    minutes = hours*60
    print ('%i hours is %i minutes' %(hours, minutes))

def days_to_hours():
    days = int(input('Enter the number of days: '))
    hours = days*24
    print ('%i days is %i hours' %(days, hours))

def minutes_to_hours():
    minutes = int(input('Enter the number of minutes: '))
    hours = minutes/60
    print ('%i minutes is %.2f hours' %(hours))

def hours_to_days():
    hours = int(input('Enter the number of hours: '))
    days = hours/24
    print ('%i hours is %.2f days' %(days))
    
method = int(input('Enter:\n1 for Hours to Minutes\n2 for Days to Hours\n3 for Minutes to Hours\n4 for Hours to Days\nChoose:'))
print ()

if (method == 1):
    hours_to_minutes()
    
elif (method == 2):
    days_to_hours()
    
elif (method == 3):
    minutes_to_hours()

else:
    hours_to_days()
