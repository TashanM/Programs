# SurfsUp_3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 11 October 2017
# Mr. Veera

wave_height = float(input('Enter the height of the waves in feet:'))

userwaverounded = int(wave_height*10)

if (userwaverounded >= 60):
   print('Great Day for Surfing!')
elif (userwaverounded >= 30):
   print('Go Body Boarding!')
elif (userwaverounded >= 0):
   print ('Go for a swim!')
else:
   print ('Whoa! What kind of surf is that?')

