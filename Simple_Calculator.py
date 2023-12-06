#Python Program to Make a Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def input_num():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    return num1, num2

def main():
    while True:
        print("\n\nTo quite the program input 'q' in the operator input.")
        operation = input("Enter operation (+, -, *, /, **): ")
        
        if operation == '+':
            num1, num2 = input_num()
            result = add(num1, num2)
        elif operation == '-':
            num1, num2 = input_num()
            result = subtract(num1, num2)
        elif operation == '*':
            num1, num2 = input_num()
            result = multiply(num1, num2)
        elif operation == '/':
            num1, num2 = input_num()
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = divide(num1, num2)
        elif operation == '**':
            num1 = int(input("Enter the number: "))
            num2 = int(input("Enter power of number you want: "))
            result = power(num1, num2)
        elif operation == 'q':
            break
        else:
            print("Error: Invalid operation. Please enter a valid operation (+, -, *, /, **).")
            return

        print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
