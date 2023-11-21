#Python Program to Find HCF or GCD

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

if num1 < num2:
    x = num1
elif num2 < num1:
    x = num2

for i in range(1, x+1):
    if (num1 % i == 0) and (num2 % i == 0):
        result = i

print(f"GCD or HCF number is :- {result}")