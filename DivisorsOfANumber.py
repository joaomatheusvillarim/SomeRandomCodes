#print the divisors of a number

listanum, primo, txt, listanum2 = list(map(int, input().split())), 1, ["is", "isn't"], []

def divisores(num):
    listadiv = []
    for n in range(1, num+1):
        if num%n==0:
            listadiv.append(n)
    return listadiv

def mdc(*numbers):
    lista, mdc = [], 0
    for x in numbers:
        lista.append(divisores(x))
    for x in lista[0]:
        present = []
        for y in range(1, len(lista)):
            present.append(True) if x in lista[y] else present.append(False)
        if all(present) and x>mdc:
            mdc = x
    return mdc

def mmc(*numbers):
    lista = []
    for x in numbers:
        lista.append(x)
    a = lista[0]
    for x in range(1, len(lista)):
        b = mdc(a, lista[x])
        b *= (a/b) * (lista[x]/b)
        a = b


for num in range(len(listanum)):
    print("The divisors of {} are: {}".format(listanum[num], listanum2[num]))
    if len(listanum2[num])<=2: primo = 0
    print("{} {} a prime number.".format(listanum[num], txt[primo]))