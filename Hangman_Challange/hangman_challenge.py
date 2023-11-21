import time
import random

def starter():
    print("Welcome to Hangman Challenge!")

    print("Loading.", end="", flush=True)
    time.sleep(1)

    for _ in range(30):
        print(".", end="", flush=True)
        time.sleep(1)

def open_file(file_name):
    with open(file_name, mode="r") as file:
        data = file.read()
        words = data.split("\n")



path = input("Enter path of wordlist: ")
open_file(path)
