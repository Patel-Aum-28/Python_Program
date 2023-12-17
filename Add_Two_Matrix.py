# Python Program to Add Two Matrices

def options():
    print("Select Option:")
    print("1. Addition of two 2x2 matrix")
    print("2. Addition of two 3x3 matrix")
    print("3. Addition of two 4x4 matrix")
    
    choice = int(input("\nEnter Your Choice:- "))
    
    if choice == 1 or choice == 2 or choice == 3:
        return choice
    else:
        print("Invalid input!")

def input_matrix(order, name):
    matrix = []
    if name == "a":
        print(f"Enter Matrix A: ")
        for i in range(order):
            row = []
            for j in range(order):
                element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                row.append(element)
            matrix.append(row)
        return matrix
    elif name == "b":
        print(f"Enter Matrix B: ")
        for i in range(order):
            row = []
            for j in range(order):
                element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                row.append(element)
            matrix.append(row)
        return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

choice = options()

if choice == 1:
    order = 2
elif choice == 2:
    order = 3
elif choice == 3:
    order = 4

nameA = "a"
nameB = "b"

matrix_a = input_matrix(order, nameA)
matrix_b = input_matrix(order, nameB)

print("Matrix A:")
print_matrix(matrix_a)

print("Matrix B:")
print_matrix(matrix_b)

result_matrix = add_matrices(matrix_a, matrix_b)

print("Resultant Matrix:")
print_matrix(result_matrix)
