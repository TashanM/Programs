# Exercise 1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 30 November 2017
# Mr. Veera

def addRoof():
    print ('%4s%s' %('/', '\\'))
    print ('%3s%2s%s' %('/', '', '\\'))
    print ('%2s%4s%s' %('/', '', '\\'))
    print ('/______\\')

def addBase():
    print (':%7s' %(':'))
    print (':%7s' %(':'))
    print (':______:')

def addWalk():
    print ('%5s' %('**'))
    print ('%14s' %('***********'))

addRoof()
addBase()
addWalk()
