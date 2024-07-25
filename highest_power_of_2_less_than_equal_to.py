def highestPowerOf2(n: int) -> int:
    # Initialize power to 1 (2^0)
    power = 1
    
    # Double the power until it exceeds n
    while power * 2 <= n:
        power *= 2
    
    return power

# Example usage
print(highestPowerOf2(10))  # Output: 8
print(highestPowerOf2(19))  # Output: 16
print(highestPowerOf2(32))  # Output: 32
