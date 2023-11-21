#Print FizzBuzz of the given interval.
#If num is divisible by 3 than print Fizz, if divisible by 5 than print Buzz and if divisible by both than print FizzBuzz.

interval = int(input("Enter range:- "))

for num in range(interval):
    if ((num%3)==0) and ((num%5)==0):
        print("FizzBuzz")
    elif (num%3)==0:
        print("Fizz")
    elif (num%5)==0:
        print("Buzz")
    else:
        print(num)
