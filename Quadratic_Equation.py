#Python Program to Solve Quadratic Equation

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

d = ((b**2)-(4*a*c))

root1 = ((-b) + (d**(1/2))) / (a*2)
root2 = ((-b) - (d**(1/2))) / (a*2)

print(f'Root1 : {root1}')
print(f'Root2 : {root2}')