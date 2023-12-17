# Python Program to Find Factorial of Number Using Recursion

num = int(input("Enter a number to find Factorial:- "))

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

if num < 0:
    print("Please enter positive number.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is:- 1")
else:
    result = factorial(num)
    print(f"Factorial of {num} is:- {result}")