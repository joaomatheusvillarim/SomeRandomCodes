from datetime import datetime, timedelta
import time

brasil = ["acre", "amazonas", "roraima", "rondonia", "tocantins", "para", "amapa", "rio grande do norte", "paraiba", \
    "pernambuco", "alagoas", "sergipe", "bahia", "ceara", "piaui", "maranhao", "mato grosso", "mato grosso do sul", "goias", \
    "distrito federal", "sao paulo", "rio de janeiro", "minas gerais", "espirito santo", "santa catarina", "parana", "rio grande do sul"]
start_time, acertos = datetime.now(), []
timea, timeb, timec, timed = start_time.day, start_time.hour, start_time.minute, start_time.second

x = input("Bem vindo ao jogo 27 estados do Brasil (embora sejam 26 e um distrito federal haha)\n" +
    "Quando o jogo começar, digite o nome de cada estado sem utilizar acentos gráficos\n" +
    "Caso queira desistir, basta digitar 'eu desisto'\n" + "Boa sorte! Aperte ENTER para começar!")
for n in range(5, 0, -1): #5 seconds countdown
    time.sleep(1)
    print(n)
print("\n"*60) #clear screen

while True: #game
    guess = input().lower() #attempt
    if guess in brasil:
        if guess in acertos: #already listed
            print("Você já listou esse estado!")
        else: #correct
            acertos.append(guess)
            print("{}/27".format(len(acertos)))
    elif guess=="eu desisto": #user gives up
        print("Você esqueceu de: {} \nTotal: {} estado(s)".format(list(set(brasil).difference(set(acertos))), 27-len(acertos)))
        break
    else: #not a state
        print("{} não é um estado".format(guess))
    if len(acertos)==27: #list is complete
        end_time = datetime.now() #user stats
        timediff = end_time - timedelta(days=timea, hours=timeb, minutes=timec, seconds=timed) 
        name = input("Parabéns! Seu tempo foi de {}\nPor favor insira seu nome: ". format(timediff.strftime("%X")))
        try: #try to read file w previous user stats
            f = open("27statesbestscore.txt")
            bestname, besttime = f.read().split(", ")
            a, b, c = map(int, besttime.split(":"))
            besttime = datetime(hour=a, minute=b, second=c, year=start_time.year, month=start_time.month, day=start_time.day)
            if timediff <= besttime:
                f = open("27statesbestscore.txt", "w")
                f.write("{}, {}".format(name, timediff.strftime("%X")))
                bestname, besttime = name, timediff
        except FileNotFoundError:
            f = open("27statesbestscore.txt", "w")
            f.write("{}, {}".format(name, timediff.strftime("%X")))
            bestname, besttime = name, timediff
        print("Melhor tempo de {} por {}".format(besttime.strftime("%X"), bestname))
        break
