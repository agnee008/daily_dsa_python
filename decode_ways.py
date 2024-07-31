def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1) #dp is a list of size n + 1 initialized to 0. This list will store the number of ways to decode the substring up to each position.
    dp[0] = 1 #dp[0] is set to 1 because there is one way to decode an empty string.
    dp[1] = 1 # dp[1] is set to 1 because there is one way to decode a string of length 1, provided the character is between '1' and '9'.

    for i in range(2, n + 1):
        one_digit = int(s[i - 1:i]) #one_digit extracts the digit at position i-1 as an integer.
        two_digits = int(s[i - 2:i]) # two_digit extracts the two digits ending at position i as an integer.
        
        if 1 <= one_digit <= 9: # If one_digit is between 1 and 9, it means the current single digit can be decoded as a valid letter ('A' to 'I'), so the number of ways to decode up to i is incremented by the number of ways to decode up to i-1.
            dp[i] += dp[i - 1] 
        
        if 10 <= two_digits <= 26: #If two_digit is between 10 and 26, it means the current two digits can be decoded as a valid letter ('J' to 'Z'), so the number of ways to decode up to i is incremented by the number of ways to decode up to i-2
            dp[i] += dp[i - 2]

    return dp[n]

# Example usage:
print(numDecodings("226"))  # Output: 3
print(numDecodings("12"))   # Output: 2
print(numDecodings("0"))    # Output: 0
