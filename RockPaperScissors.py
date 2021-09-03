import random

start = input("Welcome to Rock, Paper, Scissors!\nType 'break' to leave\nPress ENTER to start.\n")
lista, play = ["rock", "paper", "scissors"], True
while play:
    user = input("Pick one:\n{}\n".format(lista))
    if user == "break":
        play = False
    else:
        x, y = lista.index(user), random.randint(0, 2)
        print("\n"*50 + "You chose: {}\nI chose: {}".format(user, lista[y]))
        if lista[x] == lista[y]: print("It's a tie")
        if lista[x-1] == lista[y]: print("Player wins")
        if lista[x] == lista[y-1]: print("Computer wins")