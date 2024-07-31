def dailyTemperatures(temperatures: list[int]):

    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            if temperatures [j] > temperatures[i]:
                res[i] = j - i
                break
    return res
                

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) 

def dailyTemperaturesM1(temperatures: list[int]):
    n = len(temperatures)
    res= [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i -index
        stack.append(i)
    return res

print(dailyTemperaturesM1([73, 74, 75, 71, 69, 72, 76, 73])) 