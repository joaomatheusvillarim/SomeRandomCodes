#that challenge

#receives input
x = str(input())

for k in range(1, int(x)+1):
    digits = []
    willprint = 0
    #creates a list with its digits
    for y in str(k):
        digits.append(int(y))

    #analyzes the difference between digits
    for y in range(0, (len(digits)-1)):
        difference = digits[y+1] - digits[y]
        if (difference > 1) or (difference < -1):
            willprint = False
            break
        else:
            willprint = True
    if willprint == True:
        string = "".join(str(x) for x in digits)
        print(string)
