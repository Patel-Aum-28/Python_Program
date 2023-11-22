import time
import random

def starter():
    print("Welcome to Hangman Challenge!")

    print("Loading.", end="", flush=True)
    time.sleep(1)

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)

def openfile_randomword(file_name):
    with open(file_name, mode="r") as file:
        data = file.read()
        words = data.split("\n")
    main_word = random.choice(words)
    return main_word

def empty_list(main_word):
    list_of_letters = []
    list_of_dash = list_of_letters.copy()
    length_word = len(main_word)
    
    for i in main_word:
        list_of_letters.append(i)
        list_of_dash.append("_")
    
    return list_of_letters, list_of_dash, length_word

def check_word(user_input, length_word, list_of_letters, list_of_dash):
    if user_input == "":
        print("\nPlease enter something!")
    elif len(user_input) != 1 or user_input.isalpha()==False:
        print("\nInvalid input. Please enter a single character(A to Z).")
    else:
        for position in range(length_word):
            letter = list_of_letters[position]
            if letter == user_input:
                list_of_dash[position] = letter

        if "_" not in list_of_dash:
            print("\nCongratulations! You guessed the word.")
            print(f"\nCorrect word is:- {list_of_letters}")
            return False
        
    return True, list_of_dash

path = input("Enter path of wordlist: ")
main_word = openfile_randomword(path)
print("\n")
starter()
list_of_letters, list_of_dash, length_word = empty_list(main_word)

flag = True
while flag:
    user_input = input("\nGuess the character:- ").lower()
    result = check_word(user_input, length_word, list_of_letters, list_of_dash)
    
    if isinstance(result, bool):
        flag = result
    else:
        flag, dash = result
        print(dash)