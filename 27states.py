#the 27 states of brazil

from datetime import datetime
from datetime import timedelta
import time

brasil = ["acre", "amazonas", "roraima", "rondonia", "tocantins", "para", "amapa", "rio grande do norte", "paraiba", \
    "pernambuco", "alagoas", "sergipe", "bahia", "ceara", "piaui", "maranhao", "mato grosso", "mato grosso do sul", "goias", \
    "distrito federal", "sao paulo", "rio de janeiro", "minas gerais", "espirito santo", "santa catarina", "parana", "rio grande do sul"]
start_time, acertos = datetime.now(), []
timea, timeb, timec, timed = start_time.day, start_time.hour, start_time.minute, start_time.second

x = input("Bem vindo ao jogo 27 estados do Brasil (embora sejam 26 e um distrito federal haha)\n" +
    "Quando o jogo começar, digite o nome de cada estado sem utilizar acentos gráficos\n" +
    "Caso queira desistir, basta digitar 'eu desisto'\n" +
    "Boa sorte! Aperte ENTER para começar!")
for n in range(5, 0, -1):
    time.sleep(1)
    print(n)
print("\n"*60)

while True:
    guess = input().lower()
    if guess in brasil:
        if guess in acertos:
            print("Você já listou esse estado!")
        else:
            acertos.append(guess)
            print("{}/27".format(len(acertos)))
    elif guess=="eu desisto":
        print("Você esqueceu de: {} \nTotal: {} estado(s)".format(list(set(brasil).difference(set(acertos))), 27-len(acertos)))
        break
    else:
        print("{} não é um estado".format(guess))
    if len(acertos)==27:       
        end_time = datetime.now()
        timediff = end_time - timedelta(days=timea, hours=timeb, minutes=timec, seconds=timed) 
        print("Parabéns! Seu tempo foi de {}". format(timediff.strftime("%X")))
        break