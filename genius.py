import random
import time
cores = ["verde", "vermelho", "amarelo", "azul"]
sequencia = []
play = True
while play==True:
    print("\n"*100)
    x = random.randint(0, 3)
    sequencia.append(cores[x])
    for cor in sequencia:
        print(cor)
        time.sleep((2))
    print("\n"*100)
    for x in range(len(sequencia)):
        guess = input()
        if guess == sequencia[x]:
            pass
        else:
            print("Wrong")
            play = False