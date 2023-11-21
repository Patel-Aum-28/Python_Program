#Python Program to Print all Prime Numbers in an Interval

interval = int(input("Input the range (Greater than 2):- "))

for num in range(2, interval):
    for divide in range(2, num):
        if num % divide == 0:
            break
    else:
        print(num)