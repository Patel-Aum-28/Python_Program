#Python Program to Check Prime Number

num = int(input("Enter the number you want to check: "))

if num == 1:
    print(f"{num} is not a prime number!")
else:
    temp = 0
    for i in range(2, num):
        if (num % i) == 0:
            temp = 1
            break
    
    if temp == 1:
        print(f'{num} is not a prime number!')
    else:
        print(f'{num} is a prime number!')