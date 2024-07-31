def longestCommonSubsequence(text1: str, text2: str) -> str:
    """
    Compute the longest common subsequence (LCS) between two strings.

    The longest common subsequence of two strings is the longest subsequence present in both of them.
    A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

    Args:
    text1 (str): The first string to compare.
    text2 (str): The second string to compare.

    Returns:
    str: The longest common subsequence between `text1` and `text2`.

    Example:
    >>> longestCommonSubsequence("abcde", "ace")
    'ace'
    >>> longestCommonSubsequence("abc", "abc")
    'abc'
    >>> longestCommonSubsequence("abc", "def")
    ''
    """
    m, n = len(text1), len(text2)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = text1[i] + dp[i + 1][j + 1]
            else:
                if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i][j + 1]

    return dp[0][0]

text1 = "abcde"
text2 = "ace"
result = longestCommonSubsequence(text1, text2)
print(f"The longest common subsequence is: '{result}'")
