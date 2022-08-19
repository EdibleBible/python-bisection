from random import randint
a = 774
lower = 0
upper = 99
list = []
for x in range(100):
    list.append(int(randint(0, 1000)))
list.sort()
exit = 0
prev = ""
if (list[99] == a):
    exit = 1
while (exit == 0):
    y = (lower+upper)//2
    x = list[y]
    if (prev == x):
        exit = 2
    prev = x
    if (x == a):
        exit = 1
    if (x > a):
        upper = y
    elif (x < a):
        lower = y
if (exit == 1):
    print("number " + str(a) + " is present in the array with the index of " + str(((upper+lower)//2)))
if (exit == 2):
    print("number " + str(a) + " isn't present in the array")