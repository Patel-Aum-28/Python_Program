#Python Program to Display Fibonacci Sequence Using Recursion

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\nEnter 'q' to quit the program!")
    interval = input("Enter the interval: ")

    if interval.lower() == 'q':
        print("Quitting the program.")
        break
    else:
        try:
            interval = int(interval)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q'.")
            continue

        if interval <= 0:
            print(f"The Fibonacci series up to {interval} is: \nTerm({interval}): 0")
        else:
            print(f"The Fibonacci series up to {interval} is:")
            for i in range(interval+1):
                result = fibonacci(i)
                print(f"Term({i}): {result}")
