def runLengthEncoding(s: list[str]):
    # Initialize hash with keys as unique characters from s and values as 0
    hash = {char: 0 for char in s}

    # Use a variable to keep track of the count of the current character
    current_char = s[0]
    current_count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            hash[current_char] = current_count
            current_char = s[i]
            current_count = 1
    
    # Update the count for the last character sequence
    hash[current_char] = current_count

    return hash

# Example usage
s = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'd']
result = runLengthEncoding(s)
print(result)  # Output: {'a': 3, 'b': 2, 'c': 3, 'd': 2}

"""
***********
"""

def runLengthEncoding(s: list[str]) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            result.append(f"{current_count}{current_char}")
            current_char = s[i]
            current_count = 1

    # Append the last sequence
    result.append(f"{current_count}{current_char}")

    return ''.join(result)

# Example usage
s = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'd']
print(runLengthEncoding(s))  # Output: "3a2b3c2d"
