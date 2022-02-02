
def load_words():
    # Load word list from text file and sort words into 3 lists by word length
    global words_easy, words_medium, words_hard

    textfile = open("hangman/words.txt", "r")
    WORDS = textfile.read().splitlines()
    textfile.close()

    words_easy = []
    words_medium = []
    words_hard = []

    for i in WORDS:

        if len(i) == 4 | len(i) == 5:
            words_easy.append(i)
        if len(i) == 6 | len(i) == 7:
            words_medium.append(i)
        if len(i) >= 8:
            words_hard.append(i)

def clearConsole():
    # Clear command line interface, enable cleaner interaction
    import os
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def wordtolist(word):
    # Convert word to a python list
    global result, answer
    result = [] # Starts populated with the word to guess
    answer = [] # Stores the blank spaces that get populated with correct guess
    for i in word:
        result.append(i)
        answer.append("_")

def random_select(lookup):
    # Selects a random word from passed list
    from random import randint
    return lookup[randint(1,len(lookup))]

def letterguess():
    # Input letter guess, has to be single letter
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            return guess

def checkletter_multiple(letter):
    # Takes guessed letter and checks if present in word
    # If word present add letter to answer list
    global result, answer
    i=0
    while True:
        try:
          pos = result.index(letter) #returns position of guessed letter in word
          result[pos] = ''
          answer[pos] = letter
          i=i+1
        except: # Error occurs if letter not present in list
          if i < 1:
            letter_not.append(letter) # Add failed guessed letter to list
            score() # Update score
          break

def check_complete():
    # Check if guessed word is complete
    global word, answer
    a = ''.join(answer)
    if word == a:
      print('Complete!')
      return 1
    else:
      return 0

def score():
    # Drop a life
    global lives
    lives = lives - 1

def level():
    # Select a skill level to play at
    # Selects one of the word word lists to play with 
    global words_easy, words_medium, words_hard
    while True:
        try:
            choice = int(input("Level 1, 2 or 3?: "))
            if choice == 1:
                return words_easy
            if choice == 2:
                return words_medium
            if choice == 3:
                return words_hard
            else:
                return words_easy      
        except:
            print("error - select number.")

def reset_game():
    # Reset the game
    global letter_not, lives, word, result, answer
    clearConsole()
    word = random_select(level()) #Randomly select the word based on chosen skill level
    clearConsole()
    letter_not = [] # Clear failed letter guess list
    lives = 10 # Reset Lives
    wordtolist(word) # Convert word to list 
    print(' '.join(answer) + "\n")


def main():
    global letter_not, lives, word, result, answer
    load_words() 
    reset_game()
    while True:
        checkletter_multiple(letterguess())
        clearConsole()
        print(' '.join(answer) + "\n")
        nh = ', '.join(letter_not)
        print(f'Letters Used: {nh}')
        print(f'Lives: {lives}' + "\n")  
        if lives == 0:
            print('Game Over!')
            print(f'Word was: {word}')
            if input("Hit <Enter> to play again, type 'q' to quit: ") == "q":
                break
            else:
                reset_game() 
        if check_complete() == 1:
            if input("Hit <Enter> to play again, type 'q' to quit: ") == "q":
                break
            else:
                reset_game() 

if __name__ == "__main__":
    main()