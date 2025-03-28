MODULO = 301907

def count_valid_sequences(sequence: str) -> int:
    n = len(sequence)
    if n % 2 == 1:
        return 0  # Непарна кількість символів не може бути правильною дужковою послідовністю
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Базовий випадок: порожня строка є правильною
    
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                continue
            if sequence[i] == '(' or sequence[i] == '?':
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MODULO
            if (sequence[i] == ')' or sequence[i] == '?') and j > 0:
                dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MODULO
                
    return dp[n][0]

if __name__ == "__main__":
    with open("input.txt") as file:
        sequence = file.readline().strip()
    print(count_valid_sequences(sequence))
