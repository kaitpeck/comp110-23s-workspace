"""one shot wordle"""

__author__ = "730314385"

secret_word: str = "python"
playing: bool = True
secret_length: int = len(secret_word)

guess: str = str(input(f"What is your {secret_length}-letter guess? "))
guess_length: int = len(guess)

# checking to see if word length is correct or if you guessed the word right on the first try
while playing:
    if (len(guess) != secret_length):
        guess = str(input(f"That was not {secret_length} letters! Try again: "))
    else:
        if len(guess) == secret_length and guess != secret_word:
            print("Not quite. Play again soon!")
            playing = False
        else: 
            if len(guess) == secret_length and guess == secret_word:
                print("Woo! You got it!")
                playing = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
w: str = ""
s: str = 0

# checking to see if the individual characters are right
while i < secret_length:
    if guess[i] == secret_word[i]:
        w = w + GREEN_BOX #this letter is in the correct space
    else: 
        available: str = False
        while available == False and i < secret_length and s < secret_length:
            if guess[i] == secret_word[s]:
                available = True
                w = w + YELLOW_BOX #this letter is in the incorrect space, but is somewhere else in the word
            else:
                s = s + 1
        if available == False and s == secret_length:
            w = w + WHITE_BOX #this letter is not in the word at all
    i = i + 1
print(w) #tells you how accurate your characters are to the secret word