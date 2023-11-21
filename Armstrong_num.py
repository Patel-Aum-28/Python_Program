#Python Program to Check Armstrong Number

num = int(input("Enter a number :- "))

length = len(str(num))

digits = []
for i in str(num):
    digits.append(int(i))

sum = 0

for j in range(length):
    sum = (digits[j]**length) + sum

if sum == num:
    print(f"{num} is an Armstrong Number!")
else:
    print(f"{num} is not an Armstrong number!")