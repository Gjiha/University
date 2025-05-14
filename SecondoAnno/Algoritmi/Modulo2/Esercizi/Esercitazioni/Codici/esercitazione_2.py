def tabulation(s: str) -> int:
    n = len(s)
    M = [[0] * n for c in range(n)]  # creo la matrice

    for i in range(n):
        M[i][i] = 1

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            if s[i] == s[j]:
                M[i][j] = 2 + M[i + 1][j - 1]
            else:
                M[i][j] = max(M[i + 1][j], M[i][j - 1])

    return M[0][n - 1]


print(tabulation("algoritmo"))


def memoization(s: str, i: int, j: int, cache: dict = dict()) -> int:
    if (i, j) in cache:
        return cache[i, j]

    if i > j:
        cache[i, j] = 0
    elif i == j:
        cache[i, j] = 1
    else:
        if s[i] == s[j]:
            cache[i, j] = 2 + memoization(s, i + 1, j - 1, cache)
        else:
            cache[i, j] = max(
                memoization(s, i + 1, j, cache), memoization(s, j + 1, i, cache)
            )
