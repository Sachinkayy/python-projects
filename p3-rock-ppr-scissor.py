import random

def play():
    computer = random.choice(['r','p','s' ])
    x = f" your Opponent chose {computer}, It's a "
    stop = 0
    while stop ==0:
        user = input('Your choice please.. r for ROCK, p for PAPER\
s for scissor or q to Quit -- ')

        if user == 'q':
            return "SEE YOU SOON"
            
        if user ==computer:
            print(x,"tie")
            # return x,"tie"
            continue

        if iswin(user,computer):
            print(x,'win')
            continue
            return x,"win"

        print(x,'loose')
        continue
        # return x,"loose"

def iswin(player,opponent):
    if (player=='r' and opponent=='s' or player=='p' and opponent=='r'\
         or player=='s' and opponent=='p'):
         return True
print(play())