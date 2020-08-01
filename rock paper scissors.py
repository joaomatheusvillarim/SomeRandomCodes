#rock paper scissors
import random

lista = ["rock", "paper", "scissors"]
while True:
    print("Pick one: \n" + str(lista))
    x = input()
    print("You chose", x)
    try:
        x = lista.index(x)
    except:
        if x == "break":
            break
    y = random.randint(0, 2)
    print("I chose", lista[y])
    if x == y:
        print("It's a tie")
    if x == y+1:
        print("Player wins")
    if x == y-1:
        print("Computer wins")
