def countSubstrings(s:str):
    res = 0

    for i in range(0, len(s)):
        if s[i] == "1":
            for j in range(i+1, len(s)):
                if s[j] == "1":
                    res += 1
    return res


s = "00100101"
print(countSubstrings(s))