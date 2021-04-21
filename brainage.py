import random

times = int(input())
for x in range(0, times):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(1, 4)
    if c == 1:
        print("%d + %d" %(a, b))
        x = float(input())
        if x == a + b:
            pass
        else:
            print("Wrong.")
    if c == 2:
        print("%d - %d" %(a, b))
        x = float(input())
        if x == a - b:
            pass
        else:
            print("Wrong.")
    if c == 3:
        print("%d * %d" %(a, b))
        x = float(input())
        if x == a * b:
            pass
        else:
            print("Wrong.")
    if c == 4:
        print("%d / %d" %(a, b))
        x = float(input())
        if x == a / b:
            pass
        else:
            print("Wrong.")