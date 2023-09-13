from ArrayStack import ArrayStack
def arithmetic_expression(tokens, variables):
    operators = "+-*/"
    stack = ArrayStack()
    for token in tokens:
        if token not in operators:
            value = int(token) if token.isdigit() else variables[token]
            stack.push(value)
        else:
            y = stack.pop()
            x = stack.pop()
            if token == "-": result = x - y
            elif token == "+": result = x + y
            elif token == "*": result = x * y
            else:
                if y == 0: raise Exception ("not valid function")
                result = x / y
            stack.push(result)
    return stack.pop()

def calculate(tokens, variables):
    if not tokens[0].isdigit() and tokens[0] not in variables:
        variables[tokens[0]] = arithmetic_expression(tokens[2:len(tokens)], variables)
        return tokens[0]
    return arithmetic_expression(tokens, variables)

def main():
    variables = {}
    while (True):
        user_input = input("-->")
        if user_input == "done()":
            quit()
        tokens = user_input.split()
        result = calculate(tokens, variables)
        print(result)


main()

