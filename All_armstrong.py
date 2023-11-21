#Python Program to Find Armstrong Number in an Interval

interval = int(input("Enter last interval value :- "))

print(f"List of Armstrong Numbers from 1 to {interval}!")

for last in range(1, interval + 1):
    length = len(str(last))

    digits = []
    for i in str(last):
        digits.append(int(i))

    sum = 0

    for j in range(length):
        sum = (digits[j]**length) + sum

    if sum == last:
        print(f"{last}")
