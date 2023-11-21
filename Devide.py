#How many number are available that can divide provided number

num = int(input('Enter the number (1 to 1,00,00,000) :- '))

print('List of number that can divide'+ str(num) + ' :- ')

for i in range(10000000):
    if num == i:
        break
    
    if i == 0:
        continue
    elif num % i == 0:
        print(i)
    elif num % i != 0:
        continue