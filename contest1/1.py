#dp[y][x]
N, M = map(int, input().split())
x = list(map(int, input().split())) #ресурсы
y = list(map(int, input().split())) #ценность

#print(N,M,x,y)

dp = [[0] * (M+1) for i in range(N+1)]

#for g in dp:
    #print(g)

for i in range(1, N+1): #смотрю рецепт
    for j in range(1, M+1): #смотрю веса
        if x[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - x[i-1]] + y[i-1])

        else:
            dp[i][j] = dp[i-1][j]


print(dp[N][M])