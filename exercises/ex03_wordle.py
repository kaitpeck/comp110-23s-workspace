"""EX03 -- Wordle"""

__author__ = "730314385"

def contains_char(secret_word: str, guess_char: str) -> bool:
    """searching to see if guess_char is found in secret_word"""
    assert len(guess_char) == 1
    secret_idx: int = 0 

    while secret_idx < len(secret_word):
        if secret_word[secret_idx] == guess_char:
            secret_idx = secret_idx + 1
            return True
        else: 
            secret_idx = secret_idx + 1
    else: 
        return False

def emojified(guess_word: str, secret_word: str) -> str:
    """emoji to code if letters in guess match letters in secret"""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_idx: int = 0
    check: str = ""
    secret_length: int = len(secret_word)
    
    while guess_idx < secret_length:
        secret_idx: int = 0
        if guess_word[guess_idx] == secret_word[guess_idx]:
            check = check + GREEN_BOX  # this letter is in the correct space
        else: 
            cond: bool = False
            while cond is False and guess_idx < secret_length and secret_idx < secret_length:
                if guess_word[guess_idx] == secret_word[secret_idx]:
                    cond = True
                    check = check + YELLOW_BOX  # this letter is in the incorrect space, but is somewhere else in the word
                    secret_idx = secret_idx + 1
                else:
                    secret_idx = secret_idx + 1
            if cond is False and secret_idx == secret_length:
                check = check + WHITE_BOX  # this letter is not in the word at all
        guess_idx = guess_idx + 1
    return(check)  # tells you how accurate your characters are to the secret word

def input_guess(exp_length: int) -> str:
    """prompts guesses until they provide a guess of expected length"""
    playing: bool = True
    guess_word: str = str(input(f"Enter a {exp_length} character word: "))
    while playing:
        if len(guess_word) == exp_length:
            playing = False
        elif len(guess_word) != exp_length:
            guess_word: str = str(input(f"That wasn't {exp_length} chars! Try again: "))
    return guess_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_length: int = len(secret_word)
    
    attempt: int = 1
    playing: bool = True

    while attempt <= 6 and playing:
        print(f"=== Turn {attempt}/6 ===") 
        guess_word: str = input_guess(secret_length)
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {attempt} turns!")
            playing = False
        else:
            attempt = attempt +1
    if attempt > 6 and playing: 
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
