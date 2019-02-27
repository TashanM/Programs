# 2D Lists 1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 7 Febuary 2019
# Mr. Veera

produce = ['kale', 'spinach', 'sprouts']
fruit = ['olives', 'tomatoes', 'avocado']
cart = [produce, fruit]
new = []

for num in range (len(cart)-1, -1, -1):
    for num1 in range (len(cart[num])):
        new.append(cart[num][num1])

print (new)
       
