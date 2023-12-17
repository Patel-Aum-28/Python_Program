#Python Program to Find the Sum of Natural Numbers

interval = int(input("Enter the interval number until you want sum:- "))
sum = 0
for i in range(1, interval+1):
    sum = i + sum

print(sum)