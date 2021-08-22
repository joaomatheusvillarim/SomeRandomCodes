#the 50 states of USA

from datetime import datetime
from datetime import timedelta
import time

usa = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", \
    "illionois", "indiana", "idaho", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachussetts", "michigan", \
    "minnesotta", "missouri", "mississippi", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico", "new york", \
    "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", \
    "texas", "tennessee", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"]
start_time, acertos = datetime.now(), []
timea, timeb, timec, timed = start_time.day, start_time.hour, start_time.minute, start_time.second

x = input("Welcome to the game 50 States of the United States of America!\n" +
    "If you want to give, just type 'i give up'\n" +
    "Good luck! Press ENTER to start the game!")
for n in range(5, 0, -1):
    time.sleep(1)
    print(n)
print("\n"*60)

while True:
    guess = input().lower()
    if guess in usa:
        if guess in acertos:
            print("You've already said that state!")
        else:
            acertos.append(guess)
            print("{}/50".format(len(acertos)))
    elif guess=="i give up":
        print("You forgot about: {} \nTotal: {} state(s)".format(list(set(usa).difference(set(acertos))), 50-len(acertos)))
        break
    else:
        print("{} isn't a state".format(guess))
    if len(acertos)==50:       
        end_time = datetime.now()
        timediff = end_time - timedelta(days=timea, hours=timeb, minutes=timec, seconds=timed) 
        print("Congrats! Your time was {}". format(timediff.strftime("%X")))
        break