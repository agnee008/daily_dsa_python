def longestCommonSubsequence(text1: str, text2:str):
    """
    Compute the length of the longest common subsequence (LCS) between two strings.

    The longest common subsequence of two strings is the longest subsequence present in both of them.
    A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

    Args:
    text1 (str): The first string to compare.
    text2 (str): The second string to compare.

    Returns:
    int: The length of the longest common subsequence between `text1` and `text2`.

    Example:
    >>> longestCommonSubsequence("abcde", "ace")
    3
    >>> longestCommonSubsequence("abc", "abc")
    3
    >>> longestCommonSubsequence("abc", "def")
    0
    """
    dp = [[0 for j in range(len(text2) +1)] for i in range(len(text1) +1)]

    for i in range(len(text1) - 1,-1,-1):
        for j in range(len(text2) -1,-1,-1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp[0][0]


text1 = "abcde"
text2 = "ace"
result = longestCommonSubsequence(text1, text2)
print(f"The length of the longest common subsequence is: {result}")