# Exercise 2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 30 November 2017
# Mr. Veera

def inchescentimeters():
    centimeters = num*2.54
    print ('%.1f inches equals %.1f centimeters.' %(num, centimeters))

def feetcentimeters():
    centimeters = num*30
    print ('%.1f feet equals %.1f centimeters.' %(num, centimeters))

def yardsmeters():
    meters = num*0.91
    print ('%.1f yards equals %.1f meters.' %(num, meters))

def mileskilometers():
    kilometers = num*1.6
    print ('%.1f miles equals %.1f kilometers.' %(num, kilometers))

def centimetersinches():
    inches = num/2.54
    print ('%.1f centimeters equals %.1f inches.' %(num, inches))

def centimetersfeet():
    feet = num/30
    print ('%.1f centimeters equals %.1f feet.' %(num, feet))

def metersyards():
    yards = num/0.91
    print ('%.1f meters equals %.1f yards.' %(num, inches))

def kilometersmiles():
    miles = num/1.6
    print ('%.1f kilometers equals %.1f miles.' %(num, inches))

num = float(input('Enter a number: '))

print ()
print ('Convert:')
print ('1. Inches to Centimeters %15s' %('5. Centimeters to Inches'))
print ('2. Inches to Centimeters %15s' %('6. Centimeters to Inches'))
print ('3. Inches to Centimeters %15s' %('7. Centimeters to Inches'))
print ('4. Inches to Centimeters %15s' %('8. Centimeters to Inches'))
print ()

choice = int(input('Enter your choice: '))
print ()

if (choice == 1):
    inchescentimeters()
elif (choice == 2):
    feetcentimeters()

elif (choice == 3):
    yardsmeters()

elif (choice == 4):
    mileskilometers()

elif (choice == 5):
    centimetersinches()

elif (choice == 6):
    centimetersfeet()

elif (choice == 7):
    metersyards()

else:
    kilometersmiles()
