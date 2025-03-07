# This is one more Fibonacci example.

def print_fibonacci(length):
    """Print Fibonacci series."""
    if length <= 0:
        print("Length must be a positive integer.")
        return
    
    # Initial vathe first two numbers in the sequence
    first, second = 0, 1

    # Print the initial Fibonacci number
    print(first, second, end=" ")

    # Generate and print the remaiing sequence
    for _ in range(length - 2):
        next_number = first + second
        print(next_number, end=" ")
        first, second = second, next_number
        
if __name__ == '__main__':
    print('Fibonacci Series: ')
    print_fibonacci(13)
