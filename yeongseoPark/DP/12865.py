import sys
input = sys.stdin.readline

n, k = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, len(goods) + 1): # N
    for j in range(1, k+1): # K
        if goods[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-goods[i-1][0]] + goods[i-1][1])

print(dp[-1][-1])