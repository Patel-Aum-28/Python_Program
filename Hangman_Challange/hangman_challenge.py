import time
import random

def starter():
    print("Welcome to Hangman Challenge!")

    print("Loading.", end="", flush=True)
    time.sleep(1)

    for _ in range(25):
        print(".", end="", flush=True)
        time.sleep(1)

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
    
    return list_of_letters, list_of_dash


path = input("Enter path of wordlist: ")
main_word = openfile_randomword(path)
list_of_letters, list_of_dash = empty_list(main_word)

print(list_of_letters)
print(list_of_dash)