import random
dict = {"fullform of CPU? ":"central processing unit","fullform of PSU? ":"power supply", \
"fullform of RAM? " : "random access memory","fullform of ROM? ":"read only memory", \
"fullform of GPU? ":"graphics processing unit"}
score = 0
run=0
consent = input("Do you wanna play a guessing game? ENTER y to continue \n")

while True:
    if consent.lower() == "y":
        while run < 5:
            question = random.choice(list(dict.keys()))
            answer = (input(question)).lower()

            if answer == dict[question]:
                print("right answer")
                score +=1
                run +=1
            
            elif score == 5:
                print(f"Woohoo, You won the game!! Your accuracy is {(score/5)*100}%")

            elif answer != dict[question]:
                print(f"GAME OVER!! :( Your accuracy is {(score/5)*100}% \n")
                break
        consent = input("do you wish to play again? press y if YES \n")
        continue
    else:
        print("see you next time :)")
        break




    
  

