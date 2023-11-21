#Python Program to Find the Factorial of a Number

num = int(input("Enter a number to find Factorial:- "))

if num == 0:
    print(f"Factorial of {num} is 1!")
elif num < 0:
    print("Enter only positive number!")
else:
    sum = 1
    for n in range(1, num+1):
        sum = n * sum
    print(f"Factorial of {num} is {sum}!")