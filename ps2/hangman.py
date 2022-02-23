# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
# import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed = ''.join(sorted(letters_guessed))
    print(letters_guessed)
    secret_word = ''.join(sorted(set(secret_word)))
    print(secret_word)
    if (secret_word == letters_guessed):
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # create a list with '_' of same length as the secret_word
    # guessed_word = [char for char in len(secret_word) * '_ ']
    guessed_word = list(len(secret_word) * '_')

    for char in letters_guessed:
        # to get all indexes of a character in string
        res = [i for i in range(len(secret_word)) if secret_word.startswith(char, i)]
        for index in res:
            guessed_word[index] = char
        # print(guessed_word)
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets = [i for i in 'abcdefghijklmnopqrstmuvwxyz']
    for char in alphabets:
        if char in letters_guessed:
            alphabets.remove(char)
    return ''.join(alphabets)


def get_input(all_guessed_letters, available_letters, warnings, guesses_remaining):
    '''
    returns the input letter
    '''

    guess_letter = input("Please guess a letter: ").lower()
    while len(guess_letter) > 1 or guess_letter in all_guessed_letters or not guess_letter.isalpha():

        if (guesses_remaining == 0):
            return ('', warnings, guesses_remaining)

        if guess_letter == '*':
            break

        warnings -= 1
        message = "You have " + str(warnings) + " warnings left.\n"
        if warnings <= 0:
            message = "You have exhausted your warning limit!!! you lost a guess, guesses remaining: " + str(
                guesses_remaining) + "\n"
            guesses_remaining -= 1

        print("\n" + 30 * "-", "\n\nAvailable letters:", available_letters)
        guess_letter = input(message + "Please enter a single letter from 'Available letters':  ").lower()

    return (guess_letter, warnings, guesses_remaining)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 6
    correct_guesses = []
    all_guessed_letters = []
    warnings = 3
    # guessed_word = ''
    vowels = 'aeiou'
    unique_char_secret_word = len(set(secret_word))
    guessed_word_no_spaces = ''

    print(secret_word)
    print("\nWelcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.\n")

    while guesses_remaining > 0:

        # verify if the word is already guessed
        if guessed_word_no_spaces == secret_word:
            if is_word_guessed(secret_word, correct_guesses):
                print(50 * "*", '\n!!!!!!!!!!YAYYY!!!!!!!!!!\nCongratulations, you have WON! \nYour Score is:', guesses_remaining * unique_char_secret_word)
                break

        # print the guesses remaining and available alphabets
        available_letters = get_available_letters(all_guessed_letters)
        print("\n" + 30 * "-", "\n\nYou have", guesses_remaining, " guesses left\nAvailable letters:",
              available_letters)
        # get input
        (guess_letter, warnings, guesses_remaining) = get_input(all_guessed_letters, available_letters, warnings, guesses_remaining)

        if guesses_remaining == 0:
            print(50 * "*", "\nGAME OVER, please try again\nThe Secret Word is", secret_word)
            return

        if guess_letter == '*':
            show_possible_matches(guessed_word_no_spaces)
            continue

        # update the letter to guessed letters
        all_guessed_letters.append(guess_letter)
        guessed_word = ' '.join(get_guessed_word(secret_word, all_guessed_letters))
        guessed_word_no_spaces = guessed_word.replace(' ','')

        if guess_letter in secret_word:
            # print("Correct guess :)\nRemaining guesses: ", guesses_remaining)
            correct_guesses.append(guess_letter)
            print("Good guess: ",guessed_word )
        else:
            guesses_remaining -= 1 if guess_letter in vowels else 1
            print("Oops! That letter is not in my word: ", guessed_word)
            # print("Incorrect guess :( \nRemaining guesses: ",guesses_remaining)

    if (guesses_remaining == 0):
        print(50 * "*", "\nGAME OVER, please try again\nThe Secret Word is", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, my_word_length):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    for i in range(my_word_length):
        if my_word[i] == '_' or my_word[i] == other_word[i]:
            continue
        else:
            return
    return other_word


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    all_matched_word = []
    my_word_length = len(my_word)
    for word in wordlist:
        if len(word) == my_word_length:
            match = match_with_gaps(my_word, word, my_word_length)
            if match != None:
                all_matched_word.append(match)
    print(', '.join(all_matched_word))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    # show_possible_matches('t__t')
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
