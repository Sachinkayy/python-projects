
class Game():
    import random
    choices = ["r","p","s"]

    def __init__(self):
        self.player_name =input("Please enter your name after-- \n") 
        print(f"Hi {self.player_name}, hope you are ready for the big gammmme!! \n\n\n")

    def playy(self):
        while True:
            computer_choice =  Game.random.choice(Game.choices)
            player_choice = (input("Please choose from R,P,S for Rock,Paper,Scissor or Q to QUIT-- \n\n")).lower().strip()
            
            if player_choice == 'q':
                print("SEE YOU NEXT TIME \n")
                break

            elif player_choice == computer_choice:
                print(f"Its a TIE, you both chose {player_choice} \n")
                continue

            elif player_choice =="r" and computer_choice=="s" or player_choice=="p" and computer_choice=="r" or player_choice =="s" and computer_choice =="p":
                print(f"You Won, opponent chose {computer_choice} \n")
                continue

            else:
                print(f"You lost, opponent chose {computer_choice} \n")
                continue
    
p=Game()
p.playy()




