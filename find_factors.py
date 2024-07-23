def findFactors(n:int):
    output = []

    if n < 1:
        return -1

    for i in range(1,n+1):
        if n%i == 0:
            output.append(i)
    return output


if __name__=="__main__":
    n = 20
    print(findFactors(n))