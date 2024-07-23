def longestPalindromicSubsequence(s: str) -> str:
    """
    Find the longest palindromic substring within a given string.

    A palindromic substring is a substring that reads the same forward and backward.

    Args:
    s (str): The input string to search for the longest palindromic substring.

    Returns:
    str: The longest palindromic substring within `s`.

    Example:
    >>> longestPalindromicSubsequence("babad")
    'bab'  # or 'aba', both are correct
    >>> longestPalindromicSubsequence("cbbd")
    'bb'
    """
    res = ""
    resLen = 0

    for i in range(len(s)):
        # Check for odd-length palindromes
        l, r = i, i  # noqa: E741
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1  # noqa: E741
            r += 1

        # Check for even-length palindromes
        l, r = i, i + 1  # noqa: E741
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1  # noqa: E741
            r += 1

    return res

# Example usage
s = "babad"
print(f"The longest palindromic substring is: {longestPalindromicSubsequence(s)}")
