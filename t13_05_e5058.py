MATCHING_BRACKETS = {"(": ")", "[": "]", "{": "}"}

def is_balanced(expression: str) -> bool:
    stack = []
    for char in expression:
        if char in MATCHING_BRACKETS:
            stack.append(char)
        elif not stack or MATCHING_BRACKETS[stack.pop()] != char:
            return False
    return not stack

if __name__ == '__main__':
    with open("input.txt") as file:
        expr = file.readline().strip()
    print("yes" if is_balanced(expr) else "no")
