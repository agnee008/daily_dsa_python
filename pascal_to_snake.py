def pascalToSnake(s:str):
    snake_str = ""

    for char in s:
        if char.isupper():
            if snake_str:
                snake_str += '_'
            snake_str += char.lower()
        else:
            snake_str+=char
    return snake_str

print(pascalToSnake('PascalCaseString')) 