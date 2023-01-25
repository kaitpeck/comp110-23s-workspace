"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730314385"


five_char_word: str = input("Enter a 5-character word: ")
if (len(five_char_word) != 5):
    print("Error: Word must contain 5 characters") 
    exit()
else:
    single_char: str = input("Enter a single character: ")
    if (len(single_char) != 1):
        print("Error: Character must be a single character.")
        exit()
    else: 
        print("Searching for " + single_char + " in " + five_char_word)

        if (five_char_word[0] == single_char):
            print(single_char + " found at index 0")
            instances: int = 1
        else: 
            instances: int = 0

        if (five_char_word[1] == single_char):
            print(single_char + " found at index 1")
            instances = instances + 1
        else: 
            instances = instances + 0

        if (five_char_word[2] == single_char):
            print(single_char + " found at index 2")
            instances = instances + 1
        else: 
            instances = instances + 0

        if (five_char_word[3] == single_char):
            print(single_char + " found at index 3")
            instances = instances + 1
        else: 
            instances = instances + 0

        if (five_char_word[4] == single_char):
            print(single_char + " found at index 4")
            instances = instances + 1
        else: 
            instances = instances + 0

        if (instances == 0):
            print("No instances of " + single_char + " found in " + five_char_word)
        else:
            if (instances == 1):
                print(str(instances) + " instance of " + single_char + " found in " + five_char_word)
            else: 
                if (instances > 1):
                    print(str(instances) + " instances of " + single_char + " found in " + five_char_word)