def snakeToPascal(s:str):
    words = s.split('_')
    capital_words = [word.capitalize() for word in words]
    pascal_str = ''.join(capital_words)
    return pascal_str

print(snakeToPascal('snake_case_string'))