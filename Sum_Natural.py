#Python Program to Find the Sum of Natural Numbers

num = int(input("Enter the interval number until you want sum:- "))
sum = 0
for i in range(1, num+1):
    sum = i + sum

print(sum)