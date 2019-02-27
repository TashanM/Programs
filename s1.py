n = input()
one = [1, 2]
two = [3, 4]
g = [one, two]

for t in n:
    if (t == 'H'):
        s = g[0]
        g[0] = g[1]
        g[1] = s
    if (t == 'V'):
        s = g[0][0]
        s2 = g[1][0]
        g[0][0] = g[0][1]
        g[1][0] = g[1][1]
        g[0][1] = s
        g[1][1] = s2

print (g[0][0], g[0][1])
print (g[1][0], g[1][1])
