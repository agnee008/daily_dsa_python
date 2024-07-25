# Two Pointer + prefix Trie

def searchSuggestionSystem(products: list[str], searchword: str):
    products.sort()
    res = []

    for i in range(len(searchword)):
        c = searchword[i]

        l,r = 0, len(products) -1  # noqa: E741

        while l<=r and (len(products[l]) <= i or products[l][i] != c):
            l+=1  # noqa: E741
        while l<=r and (len(products[r]) <= i or products[l][r] != c):
            r-=1

        suggestions = []
        remain = r-l+1
        for j in range(min(3,remain)):
            suggestions.append([products[l+j]])
        res.append(suggestions)
    return res

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchword = "mouse"
print(searchSuggestionSystem(products, searchword))