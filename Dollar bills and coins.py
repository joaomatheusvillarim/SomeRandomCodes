#uri 1021

valor = int(float(input()) * 100)
notas = valor//100
moedas = valor%100

valores_das_notas = (100, 50, 20, 10, 5, 2)
numero_de_notas = []
valores_das_moedas = (50, 25, 10, 5)
numero_de_moedas = []

for x in valores_das_notas:
    numero = notas//x
    notas -= numero*x
    numero_de_notas.append(numero)

for x in valores_das_moedas:
    numero = moedas//x
    moedas -= numero*x
    numero_de_moedas.append(numero)

numero_de_moedas.insert(0, notas)
numero_de_moedas.append(moedas)
valores_das_moedas = (100, 50, 25, 10, 5, 1)

print("NOTAS:")
for i in range(6):
    x, y = numero_de_notas[i], valores_das_notas[i]
    print("{} nota(s) de R$ {}.00".format(x, y))

print("MOEDAS:")
for i in range(6):
    x, y = numero_de_moedas[i], valores_das_moedas[i]
    print("{x} moeda(s) de R$ {y:.2f}".format(x = x, y = y/100))