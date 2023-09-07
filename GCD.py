import math

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Calculate the GCD
gcd = math.gcd(num1, num2)

# Display the GCD
print(f"The greatest common divisor of {num1} and {num2} is {gcd}")
