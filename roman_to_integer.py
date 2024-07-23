def romantoInt(s:str):
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    N = len(s)
    output = 0
    i = N -1

    while i>=0:
        if i < N-1 and lookup[s[i]] < lookup[s[i+1]]:
            output -= lookup[s[i]]
        else:
            output += lookup[s[i]]
        i-=1
    return output

# Test cases
print(romantoInt("III"))    # Output: 3
print(romantoInt("IV"))     # Output: 4
print(romantoInt("IX"))     # Output: 9
print(romantoInt("LVIII"))  # Output: 58
print(romantoInt("MCMXCIV"))# Output: 1994
