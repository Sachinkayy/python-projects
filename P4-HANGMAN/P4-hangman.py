import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) #choosing a random word
    while '-' in word or ' ' in word:  #choosing a random word but without hypen or space
        word= random.choice(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters = set(word) #consists the words of the chosen word
    all_alphabets = set(string.ascii_uppercase) #consists all alphabets in uppercase
    used_letters = set()

    lives = 6

    #getting user input
    while lives>0 and len(word_letters) >0:
        print('You have',lives,"lives left and you have used these letters: ",' '.join(used_letters))

        #what current word is (W-RD)
        word_list= [letter if letter in used_letters else "-" for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter =input('Guess a letter: , or press qq to Quit ').upper()
        if user_letter in all_alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives -=1 #take away one life
                print('\nYour letter,',user_letter,'is not in the word.')

        elif user_letter in used_letters:
            print("\n You have already used that that letter. Guess another letter")
        
        elif user_letter =="QQ":
            break

        else:
            print('\nThat is not a valid letter.')

    #get here when lives ==0 or len(word_letters) == 0
    if lives ==0:
        print('GAME OVER, the word is ',word)
    
    elif user_letter =="QQ":
        print("SEE YOU SOON!")
    else:
        print("YAY!! YOU GUESSED THE WORD ", word,"!!")

if __name__  =="__main__":
    hangman()


