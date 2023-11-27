#Python Program to Print the Fibonacci sequence

interval = int(input("Input the range:- "))

a = 0
b = 1
count = 0

if interval <= 0:
    print (f"The fibonacci series until {interval} is: \nTerm({interval}): 0")
elif interval == 1 or interval == 2:
    print (f"The fibonacci series until {interval} is: \nTerm({interval}): 1")
else:
    print (f"The fibonacci series until {interval} is: ")
    while count <= interval:
        print(f"Term({count}): {a}")
        c = a + b
        
        a = b
        b = c
        count += 1