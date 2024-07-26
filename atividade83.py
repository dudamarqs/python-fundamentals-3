expr = str(input('Digite uma expressão:\n'))
parentheses = []

for element in expr:
    if element == '(':
        parentheses.append('(')
    elif element == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('\nSua expressão está correta.')
else:
    print('\nSua expressão está errada.')