def to_base(num_str: str, base_str: str) -> str:
    num = int(num_str)
    base = int(base_str)
    digits = []
    while num > 0:
        remainder = num % base
        num //= base
        digits.append(remainder)
    converted = ""
    while digits:
        converted += format_digit(digits.pop())
    return converted

def format_digit(digit: int) -> str:
    if digit < 10:
        return str(digit)
    else:
        return f"[{digit}]"

if __name__ == '__main__':
    with open("input.txt") as file:
        value = file.readline().strip()
        base = file.readline().strip()
    result = to_base(value, base)
    print(result)
