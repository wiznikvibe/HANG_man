#Import libraries and python modules
import random
import hangman_words
from hangman_arts import logo, stages


# Initialize end_of_game as False
end_of_game = False

#Randomly choose the word from the word_list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6


print(logo)


#Create blanks list of the same length that of the choosen word
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've have already guessed the {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
      print(f"You have guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
      if lives == 0:
            end_of_game = True
            print(("You Lose"))
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(stages[lives])