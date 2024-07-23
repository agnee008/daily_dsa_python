"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

def validAnagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    countT, countS = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

if __name__=="__main__":
    s="anagram"
    t="nagaram"
    print(validAnagram(s,t))



"""
Easy Solution:
1. return counter(s) == counter(t)
2. return sorted(s) == sorted(t)
"""