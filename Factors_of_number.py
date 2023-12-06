#Python Program to Find the Factors of a Number
num = int(input("Enter the Number: "))

print(f"The factors of {num} are: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i)
