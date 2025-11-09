n = int(input())
def functia(n):


    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(n + 1):
        dp[0][j] = 1

    for s in range(1, n + 1):
        for last in range(1, s):
            k = last // 2
            dp[s][last] = dp[s][last - 1] + dp[s - last][k]

        for last in range(s, n + 1):
            if last > s:
                dp[s][last] = dp[s][last-1]
            else:
                dp[s][last] = dp[s][last - 1] + 1

    return dp[n][n]
print(functia(n))

n = int(input())
def tralala(n):

    #dp = [[0] * (n+1) for i in range(n+1)]
    pref = [[0] * (n+1) for i in range(n+1)]

    for s in range(n+1):
        for last in range(n+1):
            if s == last:
                dp = 1
            elif s < last:
                dp = 0
            else:
                k = last // 2
                if k >= 1:
                    dp = pref[s - last][ k ]
                else:
                    dp = 0
            pref[s][last] = pref[s][last - 1] + dp

    return (pref[n][n])
print(tralala(n))