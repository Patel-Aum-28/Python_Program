# Python Program to Find Sum of Natural Numbers Using Recursion
import sys
sys.setrecursionlimit(2005)

interval = int(input("Enter the interval number until you want sum(Maximum 2000):- "))

def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n-1)

result = sum(interval)
print(f"Sum of number until {interval} is:- {result}")