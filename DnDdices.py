import random
while True:
    try:
        print(random.randint(1, int(input("How many sides? (Ex.: 6, for regular dice)\n"))))
    except ValueError:
        break