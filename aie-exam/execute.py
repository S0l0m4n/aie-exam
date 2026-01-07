def execute(input):
    try:
        result = eval(input)
        return result
    except (ValueError, SyntaxError):
        return "Invalid input"

# SOLUTION: Use ast.literal_eval()

