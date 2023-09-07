def generate_fibonacci(n):
    fibonacci_sequence = []
    
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    
    # Generate the Fibonacci sequence up to n
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        fibonacci_result = generate_fibonacci(n)
        print(f"Fibonacci sequence up to {n}: {fibonacci_result}")
