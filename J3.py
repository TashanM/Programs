s = input()
count = 0
n = []

for a in s:
    if (a == 'l' or a == 'o' or a == 'v' or a == 'e'):
        n.append(a)

for num1 in range (len(s)):
    if (s[num1] == 'l'):
        for num2 in range (num1+1, len(s)):
            if (s[num2] == 'o'):
                for num3 in range (num2+1, len(s)):
                    if (s[num3] == 'v'):
                        for num4 in range (num3+1, len(s)):
                            if (s[num4] == 'e'):
                                count+=1

print (count)
