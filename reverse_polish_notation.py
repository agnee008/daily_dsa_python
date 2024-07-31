def rpa(tokens:list[str]):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        if c == "-":
            a,b= stack.pop(), stack.pop()
            stack.append(b-a)
        if c == "*":
            stack.append(stack.pop() * stack.pop())
        if c == "/":
            a,b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[0]