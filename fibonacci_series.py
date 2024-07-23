def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): The position in the Fibonacci sequence to calculate.

    Returns:
    int: The nth Fibonacci number. If n < 1, returns 1.
    """
    if n < 1:
        return 1
    
    prev = 0
    counter = 1
    current = 1

    while counter < n:
        next = prev + current
        counter += 1
        prev = current
        current = next
    return current


def fibonacci_series(n: int):
    """
    Print the first n Fibonacci numbers.

    Args:
    n (int): The number of Fibonacci numbers to print.

    Returns:
    None
    """
    if n < 1:
        return
    
    # Initialize the first two Fibonacci numbers
    prev = 0
    current = 1
    
    # Print the first Fibonacci number
    print(prev, end=" ")

    if n == 1:
        return

    # Print the second Fibonacci number
    print(current, end=" ")

    # Generate and print the rest of the Fibonacci series
    for _ in range(2, n):
        next_val = prev + current
        print(next_val, end=" ")
        prev = current
        current = next_val


if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print(f"The first {n} Fibonacci numbers are:")
    fibonacci_series(n)
