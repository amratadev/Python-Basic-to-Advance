a = 10
b = 2

print("Div=", a/b)      # True Division → always float → 5.0
print("Div=", a//b)     # Floor Division → 5

print("Mul=", 5*2)      # Multiplication → 10
print("Square of 2 is=", 2**2)   # 2^2 → 4
print("Cube of 2 is=", 2**3)     # 2^3 → 8
print("3 raised power 4=", 3**4) # 3^4 → 81

"""
PEMDAS (Operator Precedence in Python)
P = Parentheses ()
E = Exponent **
M = Multiplication *
D = Division /
F = Floor Division //
Mod = Modulus %
A = Addition +
S = Subtraction -
L-> R 
"""

expression = 5 + 2*3 - 1 + 10/5#5+6-1+2.0->11-1+2.0->10+2.0->12.0
print(expression)  

# Calculate BMI
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

print("BMI =", (weight / (height**2)))#Body Mass Index.

print("BMI =", round(weight / (height**2), 2))#round(number, ndigits)