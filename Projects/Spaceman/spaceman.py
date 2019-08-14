import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def get_available_letters(letters_guessed):
    '''
    A function that is used to get the letters that have not been guessed yet.

    Args:
        letters_guessed (list of strings): list of letters that have been guessed so far

    Retunrs: 
        string: letters that represent what letters have not yet been guessed.
    '''

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #TODO: Loop through the letters of the alphabet and build a string of letters that are not in letters_guessed

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''


    letters_guessed = []
    allowed_num_incorrect_guesses = 7
    num_incorrect_guesses_so_far = 0

     #TODO: print a welcome message and some game instructions

    while  num_incorrect_guesses_so_far <= allowed_num_incorrect_guesses:

        #TODO: get a guess from the player and if one letter add to the letters guessed so far
        #TODO: check if the guess is more than one letter and reprompt if it is until one letter is entered. Hint: use a loop and conditionals to do this

        #TODO: If the guessed letter is in the secret word show the player they guessed correctly
        #TODO: If the guessed letter is not in the secret word, show the player the guess was incorrect and add to number of incorrect guesses the player has made so far. 
        #TODO: If the guessed letter is not in the secret word, sheck if the player has run out of incorrect guesses to end the game
        #TODO: If the guessed letter is not in the secret word, show the number of incorrect guesses left

        #TODO: show the guessed word so far

        #TODO: show the letters that have not been guessed yet

        #TODO: check if the game has been won, if so exit the loop and show a message

        break #TODO: REMOVE THIS LINE





#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())