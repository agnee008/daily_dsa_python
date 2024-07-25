def getSum(a, b):
    while b != 0:
        # Calculate the sum without carry
        sum_without_carry = a ^ b
        
        # Calculate the carry
        carry = (a & b) << 1
        
        # Update a and b
        a = sum_without_carry
        b = carry
    
    return a

# Example usage
print(getSum(1, 2))  # Output: 3
print(getSum(-2, 3)) # Output: 1
