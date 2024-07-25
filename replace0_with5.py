def replace0with5(n: int) -> int:
    # Convert the integer to a string
    str_n = str(n)
    # Replace all '0' with '5'
    replaced_str_n = str_n.replace('0', '5')
    # Convert the string back to an integer
    return int(replaced_str_n)

# Example usage
print(replace0with5(102))  # Output: 152
print(replace0with5(1020))  # Output: 1525
