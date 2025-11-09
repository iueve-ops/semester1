def meincraftic(n, m, shahta):
    anril = -10000000000
    dp = [[[anril] * 3 for _ in range(m)] for _ in range(n)]

    for d in range(3):
        dp[0][0][d] = shahta[0][0]

    for i in range(n):
        for j in range(m):
            for d in range(3):
                if dp[i][j][d] == anril:
                    continue

                for new_d, (di, dj) in enumerate([(0, 1), (1, 0), (1, 1)]):
                    if new_d == d:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        dp[ni][nj][new_d] = max(
                            dp[ni][nj][new_d],
                            dp[i][j][d] + shahta[ni][nj]
                        )

    return max(dp[n-1][m-1])

n, m = map(int, input().split())
shahta = [list(map(int, input().split())) for _ in range(n)]
print(meincraftic(n, m, shahta))
