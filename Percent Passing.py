# Percent Passing
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 25 October 2017
# Mr. Veera

numberofscores = int(input('Enter the number of total scores:'))

scorenum = 0
scorecount = 0
scoreover = 0

while (scorenum < numberofscores):
    scorecount+=1
    score = int(input('Enter the grade number %i:' %(scorecount)))

    if (score > 70):
        scoreover+=1
    scorenum+=1

if (scorenum == numberofscores):
    scorepercent = (scoreover / scorecount)*100

    print ('%.2f%% of people got over 70%%.' %(scorepercent))
