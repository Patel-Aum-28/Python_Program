#Python Program to Print all Prime Numbers in an Interval

ran = int(input("Input the range (Greater than 2):- "))

for num in range(2, ran):
    for devide in range(2, num):
        if num % devide == 0:
            break
    else:
        print(num)