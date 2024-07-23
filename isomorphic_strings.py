def isomorphicStrings(s:str,t:str) -> bool:
    """
    Check if two strings are isomorphic.

    Two strings s and t are isomorphic if there is a one-to-one mapping of 
    characters from s to t such that each character in s maps to exactly one 
    character in t, and each character in t maps to exactly one character in s.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if the strings are isomorphic, False otherwise.
    """
    if len(s) != len(t):
        return False
    
    s_hash = {} # Maps characters from s to t
    t_hash = {} # Maps characters from t to s

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s not in s_hash:
            s_hash[char_s] = char_t
        if char_t not in t_hash:
            t_hash[char_t] = char_s
        
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False
    return True

if __name__ == "__main__":
    print(isomorphicStrings("egg", "add"))  # Output: True
    print(isomorphicStrings("foo", "bar"))  # Output: False
